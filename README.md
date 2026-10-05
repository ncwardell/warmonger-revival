# Warmonger Revival

**Wiki: https://ncwardell.github.io/warmonger-revival/** — everything known about the game, with sources.

A community replacement server for **Warmonger** (formerly **Crush Online**), the free-to-play MOBA-style PvP MMO by GAMESinFLAMES / Joyimpact. Its official servers closed on 1 April 2019. This project rebuilds the server from the game client so the game can be played again.

> This repository contains **no game files**. You need your own copy of the client (it is still downloadable from Steam if it is in your library: *Warmonger Chronicles*, app 718790). Never commit the client, its archives, or anything extracted from them.

## Status

Working against the real client:

- Login, character list, character creation, entering the world
- Movement in the tutorial island (Village and warp packets are documented separately)
- Weapon skills on the skill bar; basic attacks; skill hits with damage numbers
- Monsters: spawn, simple AI (aggro, chase, attack, leash), death and respawn
- Loot straight into the bag (the game has no ground items), gold

Implemented for testing: separate player sessions, mutual player spawning, movement and combat relay, a shared monster world, private loot, and despawning on leave. Synthetic two-client socket tests pass; see `docs/spec/world.md` for the current client verification status.

New for testing: durable inventory, equipment, gold, quick-bar and quest saves, plus an optional first-four-quests experiment. See [solo testing](docs/testing.md) for the steps and current limits.

Not yet: the remaining quests and NPC services, shops, party/guild/chat, matches and fort war, and real stats/damage formulas. See [Contributing](CONTRIBUTING.md) and the issue tracker.

## How it works

The short version: `docs/gameplay/` is sourced evidence of what the original game was; `docs/wiki/` is the game's canonical data (one page per item, monster, NPC, quest, skill, map, shop…) and the server's only source of numbers; `server/` holds logic; `contract/` is the protocol. Details: [How the project fits together](https://ncwardell.github.io/warmonger-revival/how-it-fits).


- `server/` — a small Python 3 asyncio server. `stub.py` owns the sockets (login 8815, game 8813, web 8080); `handlers.py` maps opcodes to reply functions and is **reloaded on save**, so you can change replies while a client stays connected. `world.py`, `ai.py`, `skills.py` and `loot.py` hold game systems.
- `tools/` — `sof.py` (the client's encrypted config, incl. `point` to aim it at a server), `jpk.py` (the game's archives: renamed MPQ), `navmesh.py` (walkability checks).
- `docs/` — the wiki (Obsidian-style Markdown, published to GitHub Pages): gameplay facts with sources in `docs/gameplay/`, and in `docs/spec/` what has been reverse engineered: packet layouts per opcode, world loading, combat, skills, monsters, matches, archive and navmesh formats.
- `contract/` — the protocol contract: every opcode, field layouts, required replies and flows (being generated).
- `ghidra/` — the Ghidra script used to decompile the client for analysis (output stays local).

Wire format, in brief: every packet starts with a 16-byte header `u16 length | u16 0xA53C | u16 opcode | u16 extra | u32 tick | u32 key`; in-world client payloads are obfuscated as `~(word - key)` per 32-bit word. Details in `docs/spec/`.

## Quick start

Requirements: Python 3.10+, the game client, and Wine/Proton on Linux (or Windows).

1. **Copy the game** somewhere writable (keep the Steam install untouched if you like):
   `cp -r "<Steam>/steamapps/common/Warmonger Chronicles" ~/warmonger-client`
2. **Point it at your server**:
   `python3 tools/sof.py point ~/warmonger-client/Data/config/serverlist.sof 127.0.0.1`
3. **Extract game data** the server reads (quest drops, skill checks, navmesh), into `./data` (gitignored):
   `python3 tools/jpk.py extract ~/warmonger-client/Data/setting.jpk data`
4. **Run the server**: `cd server && python3 stub.py` (pass a bind address as the first argument to serve your LAN).
5. **Run the client** with `-nosg -windowed`, which starts `Client.exe` directly and skips the dead patcher:
   - Wine: `GAME_DIR=~/warmonger-client scripts/play-wine.sh`
   - Steam (Proton): patch the Steam copy's `serverlist.sof` instead (keep a backup), then set Launch Options to
     `bash -c 'exec "${@/Launcher.exe/Client.exe}" -nosg -windowed' _ %command%`

Log in (any credentials), create a character, enter the world.

### Windows testing

Copy your own Steam `Warmonger Chronicles` folder into the gitignored `client/` directory. The archive already contains a `setting/` folder, so extract it into `data/`, not `data/setting/`:

```powershell
python tools/jpk.py extract "client/Data/setting.jpk" data
python server/stub.py
```

In another PowerShell window, launch the game:

```powershell
.\scripts\play-windows.ps1
```

The launcher backs up the local server configuration, points it at localhost, and starts the client with `-ologin=player`. Pass `-GameDir` to use a different writable copy. The default `player` is a named test identity. Empty-token legacy logins continue to use `server/characters.json`; named identities use `server/accounts/`.

For two-player testing, use different test identities:

```powershell
.\scripts\play-windows.ps1 -Account alice
.\scripts\play-windows.ps1 -Account bob
```

These names are development tokens, not passwords; each gets separate character slots under the gitignored `server/accounts/`. On another computer, pass `-ServerAddress <server-LAN-IP>` and run the server bound to that address. Some client builds may permit only one instance per computer. Character creation and progress are saved per character. Inventory, equipment, gold, quick slots, quest state and experience/level survive reconnects and server restarts; position and current HP/MP reset. Progress saves are under the gitignored `server/progress/`. See [the solo test checklist](docs/testing.md) for save, quest and weapon tests.

Server state can be isolated with `WARMONGER_STATE=<directory>`; game data can be located separately with `WARMONGER_DATA=<directory>`.

### Known issues

- **Walking stutters ("stop and hop") on machines with long uptime.** The client keeps time as a float of seconds since boot, which loses precision after about a week. A real reboot fixes it; a client-side fix is open work (see `docs/spec/movement.md`).
- The client needs 32-bit graphics drivers under plain Wine; Proton or a WoW64 Wine build avoids that.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: pick a packet or system from `contract/` or the issues, capture what the client sends from the server log, implement the reply, cite your evidence, open a PR.

## Legal

This is an independent, non-commercial preservation project, not affiliated with GAMESinFLAMES, Joyimpact or Valve. It contains only original code and documentation produced by studying the client for interoperability. All game names, assets and content belong to their owners; bring your own copy of the game.

Licensed under the [GNU AGPL-3.0](LICENSE): if you run a modified server for others, share your changes.
