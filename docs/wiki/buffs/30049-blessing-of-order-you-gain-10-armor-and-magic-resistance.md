---
title: "Blessing of Order : You gain 10% Armor and Magic Resistance"
type: "buff"
id: 30049
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 30049", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10049"
duration: {"ticks": 25, "seconds": 5.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 10049
effects:
  - {"code": 106, "stat": "Armor(%)", "value": 10}
  - {"code": 107, "stat": "Magic Resist(%)", "value": 10}
icon: {"file": "Skill_Einsel_01.png", "index": 22}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=acbaa2 type=6143a1 id=30bc61 sources=b94ae2 name_key=b7963c duration=870e64 is_buff=b6589f stack_type=356a19 group=6fa07a effects=a2c63c icon=6b4fc5 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Blessing of Order : You gain 10% Armor and Magic Resistance](../assets/buffs/30049.png) |
| **Buff id** | `30049` |
| **Duration** | 5 s (25 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 10049 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 22 |

### Tooltip

> Blessing of Order : You gain 10% Armor and Magic Resistance

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 106 | Armor(%) | 10 |
| 107 | Magic Resist(%) | 10 |
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
