---
title: "Heat Stomp"
type: "skill"
id: 10118
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10118", "client: StringAll_Eng SkillComment_10118 (tooltip value tags)"]
name_key: "Skill_10118"
desc_key: "SkillComment_10118"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 95}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 95}
visual: 251
icon: {"file": "Skill_Dolorece_01.png", "index": 22}
used_by:
  - {"weapon_base": 153, "slot": 3, "items": [21011]}
---
<!-- generated:start -->
<!-- generated-keys: title=340165 type=86a754 id=39cb4b sources=eed6ea name_key=ce3739 desc_key=a8018b kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=500aa4 cost=f67772 cooldown=c9c532 effect_kind=356a19 effects=d84d69 damage_or_effect=d4c414 tooltip_formula=42ecac visual=d6e3de icon=7055ca used_by=5c7691 -->
|  |  |
|---|---|
|  | ![Heat Stomp](wiki/assets/skills/10118.png) |
| **Skill id** | `10118` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 251 `PCD_Cannon_02_E 둔탁한폭발` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 22 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 95}` Damage to all enemies around you.

Tooltip formula: **80 + 95% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |

**Reading:** amount **80 + 95% Attack**; damage (physical?).

### Used by

- Weapon skill **E** of WeaponBase 153: [[wiki/items/21011-magical-blast-cannon|Magical Blast Cannon]]
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
