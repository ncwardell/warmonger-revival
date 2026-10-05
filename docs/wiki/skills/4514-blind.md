---
title: "Blind"
type: "skill"
id: 4514
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4514", "client: Skill_TP.cdb row 11"]
name_key: "Skill_4514"
desc_key: "SkillComment_4514"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 324, "value": 13007, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 36}
used_by: []
tp: {"row": 11, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 396, "c7": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=b8d6a9 type=86a754 id=5663c4 sources=e374c5 name_key=dc1cac desc_key=2cf130 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 area=d82541 cost=4e6c0e cooldown=d97414 effect_kind=b6589f effects=568e7e damage_or_effect=bf21a9 icon=494d30 used_by=97d170 tp=0ce064 -->
|  |  |
|---|---|
|  | ![Blind](wiki/assets/skills/4514.png) |
| **Skill id** | `4514` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 11) |
| **Icon** | `ui/icons/Policy_01.png` cell 36 |

### Tooltip

> Blinds all enemies in the targeted area and slows them down.Blind disturbs the sight of your enemies.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 13,007 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 183): Blind · 2,500 / 120 · 1,500 / 120
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
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
