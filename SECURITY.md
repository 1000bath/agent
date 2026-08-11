# Dek Agent Security

See the [workspace security policy](../SECURITY.md).

Dek Agent executes model-generated Python and project commands with the current user's permissions. Worker/kernel separation is not a complete security sandbox. Use a disposable clone or recoverable worktree and isolate untrusted workloads externally.

Preserve credential redaction in logs, traces, sessions, and tool output. Report vulnerabilities privately using the channel configured in the workspace policy.
