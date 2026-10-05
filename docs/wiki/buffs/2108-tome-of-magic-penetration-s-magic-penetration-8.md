---
title: "Tome of Magic Penetration [S] : Magic Penetration +8"
type: "buff"
id: 2108
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2108", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2108"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 14, "stat": "Magic resist Penetration", "value": 8}
icon: {"file": "Items_04.png", "index": 19}
applied_by:
  - {"item": 735}
---
<!-- generated:start -->
<!-- generated-keys: title=ca9ecd type=6143a1 id=58457f sources=f0bbae name_key=584937 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=4c3a6d icon=208a91 applied_by=509c6e -->
|  |  |
|---|---|
|  | ![Tome of Magic Penetration (S) : Magic Penetration +8](wiki/assets/buffs/2108.png) |
| **Buff id** | `2108` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_04.png` cell 19 |

### Tooltip

> Tome of Magic Penetration [S] : Magic Penetration +8

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 14 | Magic resist Penetration | 8 |

### Applied by

- Using [[wiki/items/735-scroll-of-magic-pnt-s|Scroll of Magic PNT (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 54): Scroll · Scroll of Magic PNT · 732–735 · 2105–2108 · Magic penetration +2 / 4 / 6 / 8
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 78): Scroll S · Attack 35, Ability 35, Armor pen 16, Magic pen 16 · Warrior +160 Attack (2080), Magician +120 AP (2084), Armor Pen +8 (2104), Magic Pen +8 (2108)...
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
