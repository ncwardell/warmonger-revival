---
title: "Magical Protection: Increased Armor and Magic Resistance."
type: "buff"
id: 10231
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10231", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10231"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10231
effects:
  - {"code": 6, "stat": "Armor", "value": 50}
  - {"code": 7, "stat": "Magic Resist", "value": 50}
icon: {"file": "Skill_Boss_01.dds", "index": 5}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=5b5f73 type=6143a1 id=beb563 sources=634711 name_key=ce1ff8 duration=870e64 is_buff=b6589f stack_type=356a19 group=beb563 effects=afd00b icon=b3dd37 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Magical Protection: Increased Armor and Magic Resistance.](../assets/buffs/10231.png) |
| **Buff id** | `10231` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10231 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 5 |

### Tooltip

> Magical Protection: Increased Armor and Magic Resistance.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 6 | Armor | 50 |
| 7 | Magic Resist | 50 |
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
