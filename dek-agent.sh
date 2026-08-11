#!/usr/bin/env bash
# Dek Agent source launcher. prime-agent.sh remains for source compatibility.
exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/prime-agent.sh" "$@"
