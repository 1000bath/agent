# Remaining legacy branding audit

The user-facing TUI headers, installer copy, and CLI usage errors now use **Spider Agent** (with `spider-agent` as the canonical displayed command). The following `dek-agent`/Prime identifiers remain intentionally for compatibility or internal release plumbing:

- `packages/coding-agent/package.json`: package name and `dek-agent` bin alias are preserved; `spider-agent` remains an additional bin.
- `install.sh`, release scripts, and `prime-agent.sh`: `PRIME_AGENT_*` environment variables, download metadata, tarball/package defaults, and launcher names are stable installer/release contracts. The installer still defaults to the `dek-agent` command so existing installations and scripts continue to work.
- Daemon/session code and protocol fixtures retain legacy names where they identify sockets, persisted paths, wire metadata, or compatibility behavior; these must not be renamed as part of a cosmetic rebrand.
- Documentation, tests, and skill text still contain historical Dek Agent/Prime references and should be migrated separately when their public-contract impact is reviewed.
- `prime-logo.ts` keeps legacy export names for downstream imports; the artwork and new TUI call sites use `SPIDER_LOGO`.

This is an inventory, not a claim that all legacy strings are safe to change. Search with `grep -RInE "Dek Agent|dek-agent|PRIME_AGENT|prime-agent" packages/coding-agent/src install.sh scripts` before future branding work and classify each hit as user-facing copy versus compatibility contract.
