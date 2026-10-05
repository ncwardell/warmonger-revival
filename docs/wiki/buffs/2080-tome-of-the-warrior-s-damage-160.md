---
title: "Tome of the Warrior [S] : Damage +160"
type: "buff"
id: 2080
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2080", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2080"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2077
effects:
  - {"code": 1, "stat": "Attack", "value": 160}
icon: {"file": "Items_03.png", "index": 55}
applied_by:
  - {"item": 707}
---
<!-- generated:start -->
<!-- generated-keys: title=f5bc53 type=6143a1 id=28dbd2 sources=3dd679 name_key=715db2 duration=995f11 is_buff=b6589f stack_type=356a19 group=009cf5 effects=76463d icon=fd0064 applied_by=adb3e7 -->
|  |  |
|---|---|
|  | ![Tome of the Warrior (S) : Damage +160](wiki/assets/buffs/2080.png) |
| **Buff id** | `2080` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2077 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_03.png` cell 55 |

### Tooltip

> Tome of the Warrior [S] : Damage +160

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 1 | Attack | 160 |

### Applied by

- Using [[wiki/items/707-scroll-of-the-warrior-s|Scroll of the Warrior (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 51): Scroll · Scroll of the Warrior · 704–707 · 2077–2080 · Attack +32 / 64 / 96 / 160
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
