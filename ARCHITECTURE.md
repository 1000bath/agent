# Spider Agent Architecture

## Responsibilities

- CLI and terminal UI
- Agent/session lifecycle
- Daemon and worker processes
- Persistent IPython/RLM runtime
- Tools, skills, subagents, goals, schedules, and continual harness
- Integration points for model gateways and persistent memory

## Main Areas

```text
packages/
├── agent/         # Agent core
├── ai/            # Model/provider abstractions
├── coding-agent/  # CLI, TUI, daemon and sessions
└── tui/           # Terminal UI primitives
prime-agent-runtime/ # Python RLM runtime
```

## Dependency Direction

Frontend and daemon layers may consume runtime interfaces. Runtime code must not depend on interactive UI components. Provider routing belongs in `dek-gateway`; persistent retrieval belongs in `dek-memory`.

## Compatibility Boundaries

Treat daemon protocol, session storage, config paths, environment variables, ACP metadata, and public commands as versioned interfaces.
