#!/usr/bin/env bash
# Copy the server's Python modules to the play machine. handlers.py is
# reloaded live there; a change to stub.py or proto.py needs
# `systemctl --user restart warmonger-stub` (drops connected clients).
set -euo pipefail
HOST=${1:?usage: deploy.sh user@host}
cd "$(dirname "$0")"
scp -q ./*.py "$HOST:warmonger/server/"
echo "deployed: $(ls ./*.py | xargs -n1 basename | tr '\n' ' ')"
