#!/usr/bin/env python3
"""Bounded web search/fetch helper with stdlib-only runtime dependencies."""
from __future__ import annotations
import argparse, html, json, os, re, sys
from html.parser import HTMLParser
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

def load_local_env():
    path = os.path.expanduser("~/.config/spider/web-research.env")
    try:
        for line in open(path, encoding="utf-8"):
            line=line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value=line.split("=", 1)
                os.environ.setdefault(key, value)
    except OSError:
        pass

load_local_env()

class SelectorExtractor(HTMLParser):
    def __init__(self, tag=None):
        super().__init__(); self.tag=tag; self.depth=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if self.tag is None or tag == self.tag: self.depth += 1
    def handle_endtag(self, tag):
        if self.tag is None or tag == self.tag: self.depth=max(0,self.depth-1)
    def handle_data(self, data):
        if self.depth: self.parts.append(data)

class TextExtractor(HTMLParser):
    SKIP={"script","style","noscript","nav","footer","header","svg"}
    def __init__(self): super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip+=1
        if tag in {"p","div","li","h1","h2","h3","h4","pre","br"}: self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip-=1
        if tag in {"p","div","li","h1","h2","h3","h4","pre"}: self.parts.append("\n")
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def get(url, timeout):
    req=Request(url, headers={"User-Agent":"spider-web-research/1.0"})
    with urlopen(req, timeout=timeout) as r: return r.headers.get_content_type(), r.read(2_000_000).decode("utf-8","replace"), r.geturl()

def search_tavily(query, limit, timeout):
    key=os.getenv("TAVILY_API_KEY")
    if not key: return []
    data=json.dumps({"api_key":key,"query":query,"max_results":limit,"search_depth":"basic"}).encode()
    req=Request("https://api.tavily.com/search", data=data, headers={"Content-Type":"application/json","User-Agent":"spider-web-research/1.0"}, method="POST")
    with urlopen(req, timeout=timeout) as r: payload=json.load(r)
    return [{"title":x.get("title",""),"url":x.get("url",""),"snippet":x.get("content","")} for x in payload.get("results",[])[:limit]]

def search_brave(query, limit, timeout):
    key=os.getenv("BRAVE_API_KEY")
    if not key: return []
    req=Request("https://api.search.brave.com/res/v1/web/search?q="+quote(query), headers={"Accept":"application/json","X-Subscription-Token":key,"User-Agent":"spider-web-research/1.0"})
    with urlopen(req, timeout=timeout) as r: payload=json.load(r)
    return [{"title":x.get("title",""),"url":x.get("url",""),"snippet":x.get("description","")} for x in payload.get("web",{}).get("results",[])[:limit]]

def search_ddg(query, limit, timeout):
    typ, body, _=get("https://html.duckduckgo.com/html/?q="+quote(query), timeout)
    hits=[]
    for href,title,snippet in re.findall(r'class="result__a" href="([^"]+)"[^>]*>(.*?)</a>.*?class="result__snippet"[^>]*>(.*?)</',body,re.S):
        url=html.unescape(href); title=re.sub("<.*?>","",html.unescape(title)); snippet=re.sub("<.*?>","",html.unescape(snippet))
        if url not in {x["url"] for x in hits}: hits.append({"title":title,"url":url,"snippet":snippet})
        if len(hits)>=limit: break
    return hits

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    s=sub.add_parser("search"); s.add_argument("query"); s.add_argument("--limit",type=int,default=5); s.add_argument("--timeout",type=int,default=20)
    f=sub.add_parser("fetch"); f.add_argument("url"); f.add_argument("--max-chars",type=int,default=12000); f.add_argument("--timeout",type=int,default=20)
    w=sub.add_parser("scrape"); w.add_argument("url"); w.add_argument("--tag",default=None,help="HTML tag to collect, e.g. article, p, h2, a"); w.add_argument("--max-items",type=int,default=50); w.add_argument("--max-chars",type=int,default=20000); w.add_argument("--timeout",type=int,default=20)
    a=p.parse_args()
    try:
        if a.cmd=="search":
            results=[]
            errors=[]
            for provider in (search_tavily, search_brave, search_ddg):
                try:
                    results=provider(a.query,max(1,min(a.limit,20)),a.timeout)
                    if results: break
                except Exception as exc: errors.append(type(exc).__name__)
            payload={"query":a.query,"results":results}
            if errors: payload["provider_errors"]=errors
            print(json.dumps(payload,ensure_ascii=False,indent=2)); return 0
        elif a.cmd=="scrape":
            typ,body,url=get(a.url,a.timeout)
            if "html" not in typ: raise ValueError(f"Expected HTML, got {typ}")
            x=SelectorExtractor(a.tag); x.feed(body)
            chunks=[" ".join(v.split()) for v in " ".join(x.parts).split("\n") if v.strip()]
            chunks=list(dict.fromkeys(chunks))[:max(1,min(a.max_items,500))]
            payload={"url":url,"tag":a.tag,"items":chunks,"count":len(chunks)}
            print(json.dumps(payload,ensure_ascii=False,indent=2)); return 0
        else:
            typ,body,url=get(a.url,a.timeout)
            if "html" in typ:
                x=TextExtractor(); x.feed(body); text=" ".join(" ".join(x.parts).split())
            else: text=body
            print(json.dumps({"url":url,"content_type":typ,"text":text[:max(1,min(a.max_chars,100000))]},ensure_ascii=False,indent=2))
    except Exception as e: print(json.dumps({"error":str(e)}),file=sys.stderr); return 1
    return 0
if __name__=="__main__": raise SystemExit(main())
