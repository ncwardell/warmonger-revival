---
title: "Soul Infestation : You deal additional damage"
type: "skill"
id: 5124
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5124"]
name_key: "Skill_5124"
desc_key: "SkillComment_5124"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 120, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 120}
weapon_type: 9
visual: 257
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=d4db71 type=86a754 id=f88269 sources=552673 name_key=acf5a8 desc_key=45d311 kind=ac3478 kind_name=65782b target=069ef3 range=902ba3 area=500aa4 cost=2be88c cooldown=4a6a0b effect_kind=356a19 effects=284dfc damage_or_effect=05a8a5 weapon_type=0ade7c visual=c439c6 icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `5124` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Cooldown** | 1 s |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 9 |
| **Visual** | skillVisual 257 `PCE_Gun_01_W_재빠른장전 피격` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 120 | 0 |

**Reading:** amount **10 + 120% Attack**; damage (physical?).
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
