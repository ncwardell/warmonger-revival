---
title: "Tome of the Warrior [C] : Damage +32"
type: "buff"
id: 2077
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2077", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2077"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 1, "stat": "Attack", "value": 32}
icon: {"file": "Items_03.png", "index": 52}
applied_by:
  - {"item": 704}
---
<!-- generated:start -->
<!-- generated-keys: title=ad827e type=6143a1 id=009cf5 sources=a8b65b name_key=35e98e duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=43a99b icon=327fb9 applied_by=d2f60d -->
|  |  |
|---|---|
|  | ![Tome of the Warrior (C) : Damage +32](../assets/buffs/2077.png) |
| **Buff id** | `2077` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 52 |

### Tooltip

> Tome of the Warrior [C] : Damage +32

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 32 |

### Applied by

- Using [[wiki/items/704-scroll-of-the-warrior-c|Scroll of the Warrior (C)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 51): Scroll · Scroll of the Warrior · 704–707 · 2077–2080 · Attack +32 / 64 / 96 / 160
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
