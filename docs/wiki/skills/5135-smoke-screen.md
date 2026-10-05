---
title: "Smoke Screen"
type: "skill"
id: 5135
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5135"]
name_key: "Skill_5135"
desc_key: "SkillComment_5135"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: null
cooldown: {"ms": 22000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 40, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10158, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 40, "buffs": [{"buff": 10158, "rate": 100}]}
icon: {"file": "Skill_Dolorece_01.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=567d08 type=86a754 id=62d002 sources=98af03 name_key=660d4c desc_key=bf3c03 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=2be88c cooldown=ba8361 effect_kind=356a19 effects=bde9c9 damage_or_effect=becdbe icon=b75792 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Smoke Screen](../assets/skills/5135.png) |
| **Skill id** | `5135` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cooldown** | 22 s |
| **Effect kind** | damage (physical?) (1) |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 0 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 40 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10158-smoke-screen-reduces-movement-and-attack-speed\|Smoke Screen: Reduces Movement and Attack Speed]] | 100 |

**Reading:** amount **70 + 40% Attack**; damage (physical?); applies [[wiki/buffs/10158-smoke-screen-reduces-movement-and-attack-speed|Smoke Screen: Reduces Movement and Attack Speed]] (100%).
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
