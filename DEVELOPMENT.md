# Spider Agent Development

Spider Agent is the CLI, TUI, daemon, RLM runtime, tools, skills, and continual-harness composition root.

## Setup

```bash
npm ci
```

Run from source against a separate working directory:

```bash
/path/to/agent/spider-agent.sh
```

## Validation

```bash
npm run check
```

Follow `AGENTS.md` before changing code. Run focused tests from the relevant workspace package. Do not use real provider credentials in tests.

## Compatibility

User-facing branding is Spider Agent. Existing `PRIME_AGENT_*` environment variables, `.prime/agent` storage, daemon protocol identifiers, ACP metadata, MIME types, and session formats remain compatibility surfaces until an explicit migration is implemented.
