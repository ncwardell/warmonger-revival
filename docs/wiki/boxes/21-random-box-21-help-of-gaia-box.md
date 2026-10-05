---
title: "Random box 21 (Help of Gaia Box?)"
type: "box"
id: 21
status: "partial"
missing: ["odds", "opened_by"]
sources: ["client: RandomBox.cdb id 21", "contract: items.yaml use_item 0x42d (random box -> 0x427 reason 0x46 per item)", "guide + client: [[gameplay/lords-of-the-land]] §3 (stack level 1–6 → box items 1023–1028; contents not known) + notes: [[gameplay/events-and-schedules]] §2 (WM 0426 reward became Blue/Yellow crystals by buff level; opening cost 300,000 → 200,000 gold in WM 0920)"]
contents:
  - {"slot": 0, "item": 601, "count": 50, "p": 0}
  - {"slot": 1, "item": 611, "count": 50, "p": 0}
  - {"slot": 2, "item": 700, "count": 30, "p": 0}
  - {"slot": 3, "item": 700, "count": 40, "p": 0}
  - {"slot": 4, "item": 700, "count": 60, "p": 0}
  - {"slot": 5, "item": 700, "count": 80, "p": 0}
  - {"slot": 6, "item": 601, "count": 100, "p": 0}
  - {"slot": 7, "item": 611, "count": 100, "p": 0}
  - {"slot": 8, "item": 601, "count": 100, "p": 0}
  - {"slot": 9, "item": 611, "count": 100, "p": 0}
value_4c: 10000
opened_by_guess: 1024
kind: "random_box"
---
<!-- generated:start -->
<!-- generated-keys: title=96ee34 type=24f03d id=472b07 sources=79a1df contents=356d3a value_4c=8a12a3 opened_by_guess=128351 kind=364c90 -->
|  |  |
|---|---|
|  | ![](../assets/items/1024.png) |
| **RandomBox id** | `21` |
| **Opened by** | [[wiki/items/1024-help-of-gaia-box\|Help of Gaia Box]] (*guess*, not confirmed) |
| **Value @4c** | 10,000 (unknown; decoder guesses gold. The Lord of the Land reward box cost 300,000 gold to open, later 200,000 — [[gameplay/server-rules\|server rules]], WM 0426 / 0920 — so this may be the gold cost of opening: *guess*) |
| **Odds** | unknown (server side) |

### Contents

One of these is given when the box is used (contract `use_item`; *guess*: one roll per use). `p` is an unknown per-entry value (0–5; in rows 40–45 it rises with the box tier).

| slot |  | item | count | p |
|---|---|---|---|---|
| 0 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 50 |  |
| 1 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 50 |  |
| 2 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 30 |  |
| 3 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 40 |  |
| 4 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 60 |  |
| 5 | ![](../assets/items/700.png) | [[wiki/items/700-crystal-blue\|Crystal : Blue]] | 80 |  |
| 6 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 100 |  |
| 7 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 100 |  |
| 8 | ![](../assets/items/601.png) | [[wiki/items/601-blue-passion-fragments-d\|Blue Passion Fragments (D)]] | 100 |  |
| 9 | ![](../assets/items/611.png) | [[wiki/items/611-red-passion-fragments-d\|Red Passion Fragments (D)]] | 100 |  |

### Why this box item

No client column links a box item to a RandomBox row. The guess pairs rows and box items by number and contents: rows 20–25 ↔ Gaia boxes 1023–1028, 30–35 ↔ Box of the Victorious, 40–45 ↔ Box of the Participant, 46–50 ↔ the medal reward boxes, 51 ↔ the Halloween box (it holds the Jack transform scroll), 81–83 ↔ the dye boxes. Set `opened_by:` once a source confirms it.

### Seen in

- Seen in [[gameplay/lords-of-the-land|Lords of the Land buff and quest]], section *3. Stack level → buff → box (`WinAffect`)*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Added from the source hunt (see ((gameplay/sources/Sources and gaps)))*
<!-- generated:end -->

## Notes

The Lords of the Land war buff pays one box per stack level: level 2 → box item 1024 ([[gameplay/lords-of-the-land|Lords of the Land]] §3, *client* `WinAffect`). Kelsey's quests 117/763/764/765 also reward boxes 1024–1027 ([[gameplay/lords-of-the-land|Lords of the Land]] §4). From WM 0426 the box reward became Blue or Yellow crystals depending on the buff level, which fits this row's passion and crystal contents; from WM 0920 opening the box costs **200,000 gold** (was 300,000) ([[gameplay/events-and-schedules|Events and schedules]] §2, *notes*).

## Behaviour

Claiming a box resets the buff and the compensation row to zero ([[gameplay/lords-of-the-land|Lords of the Land]] §1, *image*). Only the winning team got the buff and the box in Crush Online (Nov 2016), and the box contents were changed on 22 Dec 2016 (image lost) ([[gameplay/crush-patch-notes|Crush patch notes]], *staff*).

## Sources

- guide + client: [[gameplay/lords-of-the-land]] §3 (stack level 1–6 → box items 1023–1028; contents not known) + notes: [[gameplay/events-and-schedules]] §2 (WM 0426 reward became Blue/Yellow crystals by buff level; opening cost 300,000 → 200,000 gold in WM 0920)

## Open questions

[[gameplay/lords-of-the-land|Lords of the Land]] §3 says no `RandomBox` row lists the box items 1023–1028, so their contents are unknown; this row matching box 1024 stays a guess. The opening cost (200,000 / 300,000 gold) does not match this row's `value_4c` (10,000).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
