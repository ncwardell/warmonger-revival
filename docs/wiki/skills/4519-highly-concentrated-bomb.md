---
title: "Highly Concentrated Bomb"
type: "skill"
id: 4519
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4519", "client: Skill_TP.cdb row 14"]
name_key: "Skill_4519"
desc_key: "SkillComment_4519"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 10000, "from": "Skill_TP"}
cooldown: {"ms": 180000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 464, "value": 14007, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 16}
used_by: []
tp: {"row": 14, "tp_cost": 10000, "cooldown_s": 180, "need_flags": 2, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=31d608 type=86a754 id=2238a0 sources=d702ea name_key=c71dc3 desc_key=c0d564 kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=593709 cooldown=c44d13 effect_kind=b6589f effects=f8e924 damage_or_effect=bf21a9 icon=51436c used_by=97d170 tp=4534ca -->
|  |  |
|---|---|
|  | ![Highly Concentrated Bomb](wiki/assets/skills/4519.png) |
| **Skill id** | `4519` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 10,000 TP |
| **Cooldown** | 180 s |
| **TP skill** | 10,000 TP, 180 s cooldown (Skill_TP row 14) |
| **Icon** | `ui/icons/Policy_01.png` cell 16 |

### Tooltip

> Attack the middle boss and the boss. If there is an Middle boss, attack the middle boss first

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 464 | unknown | 14,007 | 100 |

### Mentioned in

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
