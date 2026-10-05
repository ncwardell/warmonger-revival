---
title: "Increases drop rate and EXP by 10%."
type: "buff"
id: 2135
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2135", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2135"
duration: {"ticks": 3000, "seconds": 600.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2135
effects:
  - {"code": 273, "stat": "Drop Chance(%)", "value": 10}
  - {"code": 271, "stat": "code 271 (unknown)", "value": 10}
icon: {"file": "Items_15.png", "index": 16}
applied_by:
  - {"item": 689}
---
<!-- generated:start -->
<!-- generated-keys: title=672f41 type=6143a1 id=ff075d sources=fd2289 name_key=59cc02 duration=dc6a42 is_buff=b6589f stack_type=356a19 group=ff075d effects=9a2f92 icon=7b133d applied_by=003da7 -->
|  |  |
|---|---|
|  | ![Increases drop rate and EXP by 10%.](../assets/buffs/2135.png) |
| **Buff id** | `2135` |
| **Duration** | 10 min (3,000 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2135 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_15.png` cell 16 |

### Tooltip

> Increases drop rate and EXP by 10%.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 273 | Drop Chance(%) | 10 |
| 271 | code 271 (unknown) | 10 |

### Applied by

- Using [[wiki/items/689-tier-1-time-energy|Tier 1 : Time energy]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables (line 87): 689 / 690 / 691 · Tier 1 / 2 / 3 : Time energy · 2135 / 2136 / 2137 · Drop chance and EXP +10 / 20 / 30% (opts 273, 271) · 10 min (3000) · currency 10 / 11 /...
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
