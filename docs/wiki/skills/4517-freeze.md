---
title: "Freeze"
type: "skill"
id: 4517
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4517"]
name_key: "Skill_4517"
desc_key: "SkillComment_4517"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally", "enemy"], "unit_classes": ["player"], "max_targets": 15}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 314, "value": 4515, "rate": 100}
  - {"slot": 2, "type": 314, "value": 4516, "rate": 100}
  - {"slot": 3, "type": 314, "value": 4517, "rate": 100}
  - {"slot": 4, "type": 314, "value": 4518, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 4515, "rate": 100}, {"buff": 4516, "rate": 100}, {"buff": 4517, "rate": 100}, {"buff": 4518, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 44}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=903854 type=86a754 id=898453 sources=90e0aa name_key=b9ea03 desc_key=4ec9b8 kind=356a19 kind_name=9bc378 target=2f9b00 range=fe5dbb area=950fc9 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=066730 damage_or_effect=4fcb65 icon=897d76 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Freeze](wiki/assets/skills/4517.png) |
| **Skill id** | `4517` |
| **Kind** | active (1) |
| **Target** | self; self, ally, enemy; units: player; up to 15 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Effect kind** | damage (magic?) (2) |
| **Icon** | `ui/icons/Policy_01.png` cell 44 |

### Tooltip

> Freezes friends and foes alike for 4 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/4515\|Buff 4515]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/4516\|Buff 4516]] | 100 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/4517\|Buff 4517]] | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/4518\|Buff 4518]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/4515|Buff 4515]] (100%); applies [[wiki/buffs/4516|Buff 4516]] (100%); applies [[wiki/buffs/4517|Buff 4517]] (100%); applies [[wiki/buffs/4518|Buff 4518]] (100%).

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 185): Freeze · 2,500 / 120 · 1,500 / 120
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
