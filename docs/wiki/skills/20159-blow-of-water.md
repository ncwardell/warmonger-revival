---
title: "Blow of water"
type: "skill"
id: 20159
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20159"]
name_key: "Skill_20159"
desc_key: "SkillComment_20159"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 60, "attack_pct": 70}
visual: 428
icon: {"file": "Skill_Boss_01.dds", "index": 28}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=94c3d3 type=86a754 id=e1c8cc sources=e719cf name_key=ebc26b desc_key=be9fe1 kind=ac3478 kind_name=65782b target=04e8ed range=77de68 area=500aa4 cost=2be88c cooldown=4a6a0b effect_kind=356a19 effects=9f1771 damage_or_effect=fea1e6 visual=2aed8c icon=e4f418 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Blow of water](wiki/assets/skills/20159.png) |
| **Skill id** | `20159` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Cooldown** | 1 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 428 `사라스바티_물의 강타_피격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 28 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |

**Reading:** amount **60 + 70% Attack**; damage (physical?).
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
