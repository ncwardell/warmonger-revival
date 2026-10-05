---
title: "Unused gacha pool"
type: "gacha"
id: 6
status: "partial"
missing: ["price", "odds"]
sources: ["client: Gacha_06.cdb", "client strings: GUI_Herobind_GachaText_6", "contract: items.yaml hero_gacha 0x4aa, server_rules gacha_odds", "notes: [[gameplay/events-and-schedules]] §10 (WM 1018 lists five paid cards)"]
pool: 6
contents:
  - {"item": 0, "grade": 0}
  - {"item": 0, "grade": 0}
bag_slots_needed: 10
kind: "gacha_pool"
---
<!-- generated:start -->
<!-- generated-keys: title=48ea57 type=0814f8 id=c1dfd9 sources=417a15 pool=c1dfd9 contents=53cd1f bag_slots_needed=b1d578 kind=a22c27 -->
|  |  |
|---|---|
| **Pool** | `6` (`Gacha_06.cdb`, 0x4aa gacha_type 6) |
| **Bag slots needed** | 10 |
| **Odds** | unknown (server side, never published) |
| **Entries** | 2 (1 distinct items) |

### Card text

> Unused

### Contents

`grade` and `c3` are the table's own columns. In the paid pools grade 3 rows have `c3` 0, grade 2 rows `c3` 1 and grade 1 rows `c3` 2, and the Rainbow stones 641/643 appear once per rarity; so `c3` looks like the rarity (0 normal, 1 superior, 2 rare) and `grade` like a draw class, 3 the commonest (*guess*). Pools 4 and 5 set an unknown column `c4` = 1 on every row.

#### Grade 0 (2)

|  | item | kind | c3 |
|---|---|---|---|
|  | item 0 (not in `Item_Base`) | – | 0 |
|  | item 0 (not in `Item_Base`) | – | 0 |

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

The WM 1018 price list has five paid cards (1,000 / 2,000 / 2,000 / 4,000 / 5,000 jewels) and none of them matches this pool ([[gameplay/events-and-schedules|Events and schedules]] §10, *image*).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- notes: [[gameplay/events-and-schedules]] §10 (WM 1018 lists five paid cards)

## Open questions

No source gives this pool's price or shows it in game; it may be unused. Odds were never published and the client pools have no odds column ([[gameplay/events-and-schedules|Events and schedules]] §10); the contract's gacha_odds are invented. Counting draws in a video is the only lead ([[gameplay/sources|Sources]], open item 10).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
