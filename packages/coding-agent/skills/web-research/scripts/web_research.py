#!/usr/bin/env python3
"""Bounded web search/fetch helper with stdlib-only runtime dependencies."""
from __future__ import annotations
import argparse, html, json, os, re, sys
from html.parser import HTMLParser
from urllib.parse import quote, urljoin
from urllib.request import Request, urlopen

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
    a=p.parse_args()
    try:
        if a.cmd=="search": print(json.dumps({"query":a.query,"results":search_ddg(a.query,max(1,min(a.limit,20)),a.timeout)},ensure_ascii=False,indent=2))
        else:
            typ,body,url=get(a.url,a.timeout)
            if "html" in typ:
                x=TextExtractor(); x.feed(body); text=" ".join(" ".join(x.parts).split())
            else: text=body
            print(json.dumps({"url":url,"content_type":typ,"text":text[:max(1,min(a.max_chars,100000))]},ensure_ascii=False,indent=2))
    except Exception as e: print(json.dumps({"error":str(e)}),file=sys.stderr); return 1
    return 0
if __name__=="__main__": raise SystemExit(main())
