---
title: "Heat Stomp"
type: "skill"
id: 5118
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5118", "client: StringAll_Eng SkillComment_5118 (tooltip value tags)"]
name_key: "Skill_5118"
desc_key: "SkillComment_5118"
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
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 251
icon: {"file": "Skill_Dolorece_01.png", "index": 22}
used_by:
  - {"weapon_base": 53, "slot": 3, "items": [20011]}
---
<!-- generated:start -->
<!-- generated-keys: title=340165 type=86a754 id=d5a52f sources=881e68 name_key=2ad148 desc_key=dd5140 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=500aa4 cost=f67772 cooldown=c9c532 effect_kind=356a19 effects=db4d14 damage_or_effect=75d6a2 tooltip_formula=0fc93d visual=d6e3de icon=7055ca used_by=d0a398 -->
|  |  |
|---|---|
|  | ![Heat Stomp](../assets/skills/5118.png) |
| **Skill id** | `5118` |
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

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 90}` Damage to all enemies around you.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **80 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **E** of WeaponBase 53: [[wiki/items/20011-magical-blast-cannon|Magical Blast Cannon]]
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
