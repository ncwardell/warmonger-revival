#!/usr/bin/env bash
# Launch the client under Wine against a server (default: local).
#   GAME_DIR=/path/to/patched/copy scripts/play-wine.sh
# The copy must have a serverlist.sof pointed at your server (tools/sof.py point).
set -euo pipefail
: "${GAME_DIR:?set GAME_DIR to your patched copy of the game}"
WINE=${WINE:-wine}
export WINEPREFIX=${WINEPREFIX:-$HOME/.local/share/warmonger-revival/wineprefix}
export WINEDEBUG=${WINEDEBUG:--all} WINEDLLOVERRIDES=${WINEDLLOVERRIDES:-mscoree,mshtml=}
cd "$GAME_DIR"
exec "$WINE" Client.exe -nosg -windowed -width "${WIDTH:-1600}" -height "${HEIGHT:-900}" "$@"
