---
title: "Innocence gacha"
type: "gacha"
id: 3
status: "stub"
missing: ["odds"]
sources: ["client: Gacha_03.cdb", "client strings: GUI_Herobind_GachaText_3", "contract: items.yaml hero_gacha 0x4aa, server_rules gacha_odds", "docs: [[gameplay/events-and-schedules]] §10 (WM 1018 image 2: card prices in jewels; pool-to-card match inferred from contents and GUI_Herobind_GachaText_N)"]
pool: 3
contents:
  - {"item": 9000, "grade": 1}
  - {"item": 9001, "grade": 1}
  - {"item": 9002, "grade": 1}
  - {"item": 9003, "grade": 1}
  - {"item": 9004, "grade": 1}
  - {"item": 9005, "grade": 1}
  - {"item": 9006, "grade": 1}
  - {"item": 9007, "grade": 1}
  - {"item": 8500, "grade": 1, "c3": 1}
  - {"item": 8501, "grade": 1, "c3": 1}
  - {"item": 8502, "grade": 1, "c3": 1}
  - {"item": 8503, "grade": 1, "c3": 1}
  - {"item": 8504, "grade": 1, "c3": 1}
  - {"item": 8505, "grade": 1, "c3": 1}
  - {"item": 8506, "grade": 1, "c3": 1}
  - {"item": 8507, "grade": 1, "c3": 1}
  - {"item": 8000, "grade": 1, "c3": 2}
  - {"item": 8001, "grade": 1, "c3": 2}
  - {"item": 8002, "grade": 1, "c3": 2}
  - {"item": 8003, "grade": 1, "c3": 2}
  - {"item": 8004, "grade": 1, "c3": 2}
  - {"item": 8005, "grade": 1, "c3": 2}
  - {"item": 8006, "grade": 1, "c3": 2}
  - {"item": 8007, "grade": 1, "c3": 2}
price: {"amount": 2000, "currency": 13, "currency_name": "Jewels (yellow + purple)"}
bag_slots_needed: 5
kind: "gacha_pool"
---
<!-- generated:start -->
<!-- generated-keys: title=1768f4 type=0814f8 id=77de68 sources=4659dc pool=77de68 contents=733f2c price=66fc63 bag_slots_needed=ac3478 kind=a22c27 -->
|  |  |
|---|---|
| **Pool** | `3` (`Gacha_03.cdb`, 0x4aa gacha_type 3) |
| **Card name** | Innocence (`GUI_Herobind_Type3`) |
| **Price** | 2,000 Jewels (yellow + purple) |
| **Bag slots needed** | 5 |
| **Odds** | unknown (server side, never published) |
| **Entries** | 24 (24 distinct items) |

### Card text

> You can earn items between 1 and 3 tiers

### What the 2018 card listed

[[gameplay/events-and-schedules|Events and schedules]] §10 (WM 1018 image): Normal / Superior / Rare Innocence (1), Crystal: Innocence (1), Piece: Innocence. The match of this client pool to that card is *inferred* from the tiers and contents.

### Contents

`grade` and `c3` are the table's own columns. In the paid pools grade 3 rows have `c3` 0, grade 2 rows `c3` 1 and grade 1 rows `c3` 2, and the Rainbow stones 641/643 appear once per rarity; so `c3` looks like the rarity (0 normal, 1 superior, 2 rare) and `grade` like a draw class, 3 the commonest (*guess*). Pools 4 and 5 set an unknown column `c4` = 1 on every row.

#### Grade 1 (24)

|  | item | kind | c3 |
|---|---|---|---|
| ![](wiki/assets/items/9000.png) | [[wiki/items/9000-piece-dark-knight-skull\|Piece : Dark knight Skull]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9001.png) | [[wiki/items/9001-piece-guardian\|Piece : Guardian]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9002.png) | [[wiki/items/9002-piece-amaterasu\|Piece : Amaterasu]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9003.png) | [[wiki/items/9003-piece-sarasvati\|Piece : Sarasvati]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9004.png) | [[wiki/items/9004-piece-artamos\|Piece : Artamos]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9005.png) | [[wiki/items/9005-piece-morion\|Piece : Morion]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9006.png) | [[wiki/items/9006-piece-king-deathhead\|Piece : King Deathhead]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/9007.png) | [[wiki/items/9007-piece-tempest-fisher\|Piece : Tempest Fisher]] | Innocence Piece (36) | 0 |
| ![](wiki/assets/items/8500.png) | [[wiki/items/8500-crystal-dark-knight-skull\|Crystal : Dark knight Skull]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8501.png) | [[wiki/items/8501-crystal-guardian\|Crystal : Guardian]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8502.png) | [[wiki/items/8502-crystal-amaterasu\|Crystal : Amaterasu]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8503.png) | [[wiki/items/8503-crystal-sarasvati\|Crystal : Sarasvati]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8504.png) | [[wiki/items/8504-crystal-artamos\|Crystal : Artamos]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8505.png) | [[wiki/items/8505-crystal-morion\|Crystal : Morion]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8506.png) | [[wiki/items/8506-crystal-king-deathhead\|Crystal : King Deathhead]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8507.png) | [[wiki/items/8507-crystal-tempest-fisher\|Crystal : Tempest Fisher]] | Innocence (18) | 1 |
| ![](wiki/assets/items/8000.png) | [[wiki/items/8000-dark-knight-skull\|Dark knight Skull]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8001.png) | [[wiki/items/8001-guardian\|Guardian]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8002.png) | [[wiki/items/8002-amaterasu\|Amaterasu]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8003.png) | [[wiki/items/8003-sarasvati\|Sarasvati]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8004.png) | [[wiki/items/8004-artamos\|Artamos]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8005.png) | [[wiki/items/8005-morion\|Morion]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8006.png) | [[wiki/items/8006-king-deathhead\|King Deathhead]] | Innocence (18) | 2 |
| ![](wiki/assets/items/8007.png) | [[wiki/items/8007-tempest-fisher\|Tempest Fisher]] | Innocence (18) | 2 |

### Odds

Not in the client (`Gacha_NN` has items and grades only). The contract's `gacha_odds` suggestion (uniform within a grade, grade weights 70/25/5) is invented, not original data. Put real odds in `odds:` with a source.

### Seen in

- Seen in [[gameplay/README|Gameplay]], section *Pages*
- Seen in [[gameplay/classes-and-legions|Classes, nations and legions]], section *1. Classes*
- Seen in [[gameplay/events-and-schedules|Events, schedules and PvP rewards]], section *9. Other timers and limits*
- Seen in [[gameplay/items-and-crafting|Items, upgrades and crafting]], section *5. Where gear comes from*
- Seen in [[gameplay/patch-history|Patch notes and other sources]], section *Economy and timeline*
- Seen in [[gameplay/progression-and-economy|Progression and economy]], section *3. Currencies*
- Seen in [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]], section *4. Gear reinforce and tier-up*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Economy*
- Seen in [[gameplay/sources|Sources and gaps]], section *9. What is still missing*
- Seen in [[gameplay/videos|Videos]], section *Wars, forts and matches*
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
