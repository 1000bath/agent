# Spider Agent Rebrand and Migration Notes

## Release note

This release introduces **Spider Agent** as the user-facing name for the agent CLI, TUI, runtime documentation, and core package documentation, and adds `spider-agent` as a command alias for the same binary. The runtime behavior and supported workflows are unchanged.

## Compatibility

Existing installs and integrations continue to use their established compatibility identifiers. The rebrand adds a `spider-agent` command alias rather than renaming existing ones:

- The npm package installs `pi`, `dek-agent`, and `spider-agent` as command aliases for the same binary. `dek-agent` remains the documented default command; the shell launchers delegate to the same entry point.
- `prime-agent.sh`, `prime-agent-runtime/`, npm package names, and runtime identifiers are unchanged.
- `PRIME_AGENT_*` and legacy `PI_*` environment variables remain valid. Optional aliases include `SPIDER_AGENT_CODING_AGENT_DIR` (preferred by the rebranded runtime, with PRIME/PI fallbacks) and the existing `PRIME_AGENT_CMD`, `PRIME_AGENT_PACKAGE`, and `PRIME_AGENT_PACKAGE_NAME` installer/release overrides.
- `.prime/agent` storage, daemon protocol identifiers, ACP metadata, MIME types, and session formats remain valid.
- No source/runtime API or package namespace migration is included.

## Upgrade guidance

Users can continue upgrading and invoking the agent exactly as before; `dek-agent` remains the documented command, while `spider-agent` (and `pi`) are available as equivalent aliases. New documentation refers to Spider Agent; scripts and integrations should not be renamed as part of this release. A future namespace migration, if undertaken, must provide an explicit compatibility period and separate release notes.

## Scope

User-facing Markdown documentation is rebranded and a `spider-agent` command alias is added. Runtime behavior, daemon protocol identifiers, ACP metadata, MIME types, session formats, `.prime/agent` storage, npm package names, lockfiles, and release scripts are unchanged; no existing runtime or protocol identifier is renamed.
