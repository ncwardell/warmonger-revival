---
title: "A Warrior's Body"
type: "skill"
id: 5197
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5197"]
name_key: "Skill_5197"
desc_key: "SkillComment_5197"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 50, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 50, "attack_pct": 70}
visual: 327
icon: {"file": "Skill_Boss_01.dds", "index": 2}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4912df type=86a754 id=498aa1 sources=92f0b3 name_key=533d78 desc_key=dca9dc kind=ac3478 kind_name=65782b target=04e8ed range=77de68 area=6d01a6 cost=2be88c cooldown=4a6a0b effect_kind=356a19 effects=be7f53 damage_or_effect=645941 visual=076e5a icon=1a93f3 used_by=97d170 -->
|  |  |
|---|---|
|  | ![A Warrior's Body](wiki/assets/skills/5197.png) |
| **Skill id** | `5197` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cooldown** | 1 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 327 `수호신장_변신스킬_03_전사의 육체 피격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 2 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 50 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |

**Reading:** amount **50 + 70% Attack**; damage (physical?).
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
