---
title: "Tome of Armor Penetration [C] : Armor Penetration +2"
type: "buff"
id: 2101
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2101", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2101"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 13, "stat": "Armor Penetration", "value": 2}
icon: {"file": "Items_04.png", "index": 12}
applied_by:
  - {"item": 728}
---
<!-- generated:start -->
<!-- generated-keys: title=09a983 type=6143a1 id=86e1d3 sources=0a57af name_key=011bad duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=45c2f3 icon=81e226 applied_by=9e7f08 -->
|  |  |
|---|---|
|  | ![Tome of Armor Penetration (C) : Armor Penetration +2](../assets/buffs/2101.png) |
| **Buff id** | `2101` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_04.png` cell 12 |

### Tooltip

> Tome of Armor Penetration [C] : Armor Penetration +2

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 13 | Armor Penetration | 2 |

### Applied by

- Using [[wiki/items/728-scroll-of-armor-pnt-c|Scroll of Armor PNT (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 53): Scroll · Scroll of Armor PNT · 728–731 · 2101–2104 · Armor penetration +2 / 4 / 6 / 8
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
