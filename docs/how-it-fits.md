---
title: "How the project fits together"
---

# How the project fits together

Four layers, each with one job. Knowing which layer a fact belongs in is most of contributing.

```
client (Client.exe + Data/*.jpk)
   │  decoded by tools/ and wiki/gamewiki
   ▼
gameplay/  ── evidence ──►  wiki/  ── loaded by ──►  server/
(what the game was)        (what the game is)        (logic only)
                              ▲
contract/ + spec/  ── how the client and server talk (protocol)
```

## gameplay/ — the evidence

What the original Warmonger (2018–19) and Crush Online (2016–17) were, collected from everything that survives: player guides, spreadsheets, the archived official forums, patch notes, screenshots and gameplay videos.

- **Historical.** It records what sources say, including where they disagree with each other or with the client. Crush Online values stay as history even when Warmonger changed them.
- **Always sourced.** Every fact links to its guide, sheet, forum thread or video timestamp.
- **Not read by the server.** It changes only when we find new sources.

Pages: [[gameplay/README|Gameplay]].

## wiki/ — the canonical game data

One page per game entity — every item, monster, NPC, quest, skill, buff, map, zone, dungeon, shop, recipe, upgrade, box and gacha pool — pre-populated from the client and filled in one entity at a time. It is **the current state of the game and the single source of truth for the server**.

- **The intended home for every value the server uses**, whatever its origin (migration status below):
  - *client* — read from the client's own data by the generator (`wiki/gamewiki/`);
  - *evidence* — taken from a gameplay page, citing it (a guide, sheet, video timestamp);
  - *design* — a value we chose because no source has it (marked as such, so it's clear what is a stand-in).
- **Structured data lives in front matter**; behaviour, notes and open questions in the page body. A page's `status` (stub / partial / complete) and `missing:` list show what is still undefined; the section indexes show coverage.
- **Generated and hand-written parts are kept apart.** The generator rewrites only its marked block and its own keys; hand-entered values (and anything under `manual:`) are never overwritten.
- **Conflicts are resolved here, not in code.** When sources disagree, the page picks a value (client data first, then Warmonger sources, then Crush Online) and records the disagreement under *Open questions*.

Pages: the Wiki section.

## server/ — logic only

The replacement server is moving its game data into the wiki. Through `server/gamedata.py` it reads every quest it can verify (1-7 plus seven later ones), the two **Chepa officers (710/711)**, the enabled maps and their gates (`server/maps.py`), town NPC positions, and shop stock and price rates (`server/shops.py`). None of these require extracted client tables. Restart the server after editing wiki data; wiki files are not watched for hot reload.

Level thresholds, skills and loot still use local client tables, and older world placements and combat formulas still contain prototype constants. CI tests the supported wiki quest journey, including selected rewards and reconnects; the quest loader skips unsupported definitions with a recorded reason and fails startup if quests 1-7 cannot load. A project-wide check for hard-coded game values is not implemented yet. Filling out a wiki page outside the supported slice does not enable that system automatically.

## contract/ and spec/ — the protocol

How the client and server talk: every opcode, field layouts, what the client accepts and what the server must reply, reverse engineered from the client. Not game data. Pages: [[spec/index|Protocol overview]] and the contract per system.

## Where does my fact go?

| You found… | Put it in |
|---|---|
| A number in a guide, sheet, forum post or video | **gameplay/** (with its source), then copy it onto the entity's **wiki/** page citing that gameplay page |
| The value the server should use for something | the entity's **wiki/** page |
| A value nobody knows, so you chose one | the **wiki/** page, marked `design` |
| How a packet is laid out or what the client expects back | **contract/** (YAML) or **spec/** |
| A server behaviour bug | **server/** code — but never a game number |

> [!note] Status
> The wiki and its generator exist; moving the server's remaining hard-coded placeholders onto wiki pages, and the CI drift checks, are in progress.
