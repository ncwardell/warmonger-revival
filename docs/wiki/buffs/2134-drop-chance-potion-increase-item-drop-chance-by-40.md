---
title: "Drop Chance Potion: Increase Item Drop Chance by 40%."
type: "buff"
id: 2134
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2134", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2134"
duration: {"ticks": 18000, "seconds": 3600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2034
effects:
  - {"code": 273, "stat": "Drop Chance(%)", "value": 40}
icon: {"file": "Items_07.png", "index": 59}
applied_by:
  - {"item": 764}
---
<!-- generated:start -->
<!-- generated-keys: title=5ee340 type=6143a1 id=9e1f50 sources=fad400 name_key=388a0a duration=23bd3e is_buff=b6589f stack_type=356a19 group=3d8ae2 effects=c1dcef icon=37da9a applied_by=042886 -->
|  |  |
|---|---|
|  | ![Drop Chance Potion: Increase Item Drop Chance by 40%.](wiki/assets/buffs/2134.png) |
| **Buff id** | `2134` |
| **Duration** | 60 min (18,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2034 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_07.png` cell 59 |

### Tooltip

> Drop Chance Potion: Increase Item Drop Chance by 40%.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 273 | Drop Chance(%) | 40 |

### Applied by

- Using [[wiki/items/764-drop-chance-potion|Drop Chance Potion]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 86): 764 · Drop Chance Potion · 2134 · Item drop chance +40% (opt 273) · 1 h (18000) · gold 10 base; in Npc_Carry list 401
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
