#!/usr/bin/env bash
# Spider Agent source launcher.
# Kept separate from dek-agent.sh and prime-agent.sh for compatibility.
set -euo pipefail
exec "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/prime-agent.sh" "$@"
