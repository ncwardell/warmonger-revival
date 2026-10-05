---
title: "Improved Fortification"
type: "skill"
id: 5229
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5229"]
name_key: "Skill_5229"
desc_key: "SkillComment_5229"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "NPC", "player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 1400, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 1400}
visual: 360
icon: {"file": "Policy_01.png", "index": 39}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=c76de6 type=86a754 id=f96989 sources=a361a4 name_key=61b317 desc_key=e45339 kind=356a19 kind_name=9bc378 target=479d25 range=b1d578 area=6d01a6 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=8e8d05 damage_or_effect=65b890 visual=a1773d icon=30da17 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Improved Fortification](../assets/skills/5229.png) |
| **Skill id** | `5229` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, NPC, player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 360 `TP스킬_타워강화` |
| **Icon** | `ui/icons/Policy_01.png` cell 39 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 1,400 | 100 |

**Reading:** amount **1,400**; damage (physical?).
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
