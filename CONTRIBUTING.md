# Contributing

Thanks for helping bring Warmonger back. Everything here is learned from the client, so the most valuable contributions are **evidence-backed packet work**.

## Ground rules

- **No game files in the repo.** No client binaries, `.jpk`/`.cdb` files, extracted data tables, assets, or decompiled/disassembled code. Describe what code does (addresses, offsets, behaviour) in your own words instead.
- **Cite evidence** for every layout or rule: a handler or send-site address, a captured packet from the server log, or a client-internal example (debug/GM commands that build server packets locally).
- **Mark guesses as guesses.** Server-only rules (damage formulas, drop rates, AI, matchmaking) were never in the client; say when a value is a design choice.

## Workflow

1. **Find work.** `contract/README.md` lists uncovered opcodes and flows; issues are labelled by system.
2. **Capture.** Run the server and play; every packet is logged, e.g.
   `[game] <- op=0x0416 extra=0x0001 key=0x0001 len=32 body=...` (payloads are shown de-obfuscated).
3. **Read the client.** Decompile your own copy (Ghidra 12, see `ghidra/DumpDecomp.java`); `docs/spec/` and `contract/` name the handler and send-site functions for each opcode.
4. **Implement.** Reply functions take the de-obfuscated packet bytes and return bytes to send (several packets may be concatenated) or `None`. Register them in a module's `REPLIES` table; periodic work goes in `tick()`. `sessions.current()` selects the caller's state; use `skills.state()`, `world.player()`, and `loot.state()` inside packet helpers. The shared world ticks once regardless of player count. Handlers and gameplay modules reload on save; edits to `stub.py`, `proto.py`, or `sessions.py` need a restart.
5. **Test.** Each module has a `__main__` self-test that must run without game data:
   `cd server && for m in world ai skills loot; do python3 $m.py; done`
   Also run `python3 -m unittest -v test_multiplayer` for packet framing, independent sessions, player visibility, shared monsters, private loot, hot reload, and the two-client socket journey.
   Then try it in the real client and say what you saw in the PR.
6. **Document.** Update `contract/<system>.yaml` and/or the wiki (`docs/`) with what you learned.

## The wiki

`docs/` is the wiki: open it as an Obsidian vault, link pages with `[[wikilinks]]`, and cite a source for every fact (see `docs/wiki-style.md`). Game knowledge from guides, videos and memory is as welcome as code — put it in `docs/gameplay/`. Pushes to `main` publish it to https://ncwardell.github.io/warmonger-revival/.

## Style

Match the surrounding code: small functions, a docstring giving the packet's offsets (`+0x10 u16 ...`), `struct.pack_into` on a `bytearray`, constants at the top of the module, no frameworks.

## Setting up analysis

- Ghidra 12.1.4 + JDK 21; import `Client.exe` (32-bit PE, MSVC 2010, RTTI present) and run `ghidra/DumpDecomp.java` to dump every function to one searchable file.
- The archives are MPQ with renamed magic (`NPK\x1a`); `tools/jpk.py list|extract`.
- Keep all output outside the repo or under the gitignored `data/` and `out/` folders.
