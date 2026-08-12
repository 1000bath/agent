# Spider Agent Rebrand and Migration Notes

## Release note

This release introduces **Spider Agent** as the user-facing name for the agent CLI, TUI, runtime documentation, and core package documentation. The runtime behavior and supported workflows are unchanged.

## Compatibility

The rebrand is documentation-only. Existing installs and integrations continue to use their established compatibility identifiers:

- The `dek-agent` command remains the documented launcher for this release.
- `prime-agent.sh`, `prime-agent-runtime/`, inherited package manifests, and package names are unchanged.
- `PRIME_AGENT_*` environment variables, `.prime/agent` storage, daemon protocol identifiers, ACP metadata, MIME types, and session formats remain valid.
- No source/runtime API or package namespace migration is included.

## Upgrade guidance

Users can continue upgrading and invoking the agent exactly as before. New documentation refers to Spider Agent; scripts and integrations should not be renamed as part of this release. A future namespace migration, if undertaken, must provide an explicit compatibility period and separate release notes.

## Scope

Only user-facing Markdown documentation is rebranded. No source files, runtime identifiers, package manifests, lockfiles, or release scripts are changed.
