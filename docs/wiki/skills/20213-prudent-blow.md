---
title: "Prudent blow"
type: "skill"
id: 20213
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20213", "client: StringAll_Eng SkillComment_20213 (tooltip value tags)"]
name_key: "Skill_20213"
desc_key: "SkillComment_20213"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 18
area: {"shape": 1, "shape_name": "circle", "radius": 2.0, "width_or_angle": 0.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 120, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 120}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 120}
visual: 432
icon: {"file": "Skill_Boss_01.dds", "index": 38}
used_by:
  - {"weapon_base": 73, "slot": 8, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=27ef28 type=86a754 id=c97f04 sources=09fcd4 name_key=5ceff6 desc_key=1acd09 kind=356a19 kind_name=9bc378 target=7056fd range=9e6a55 area=711599 cost=ff5a60 cooldown=ad2ac8 delivery=93a212 effect_kind=356a19 effects=016bb8 damage_or_effect=2fc373 tooltip_formula=b0ad8c visual=a2092f icon=b8e91e used_by=63a6cf -->
|  |  |
|---|---|
|  | ![Prudent blow](../assets/skills/20213.png) |
| **Skill id** | `20213` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 18 (world units) |
| **Area** | circle, radius 2, width/angle 0 (indicator `stick256x512.png`) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 432 `아르타모스_신중한 일격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 38 |

### Tooltip

> [Active] Deals `{EF_STATIC 120}``{EF_R_DAM 120}` Physical Damage to enemies.

Tooltip formula: **120 + 120% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 120 | 0 |

**Reading:** amount **120 + 120% Attack**; damage (physical?).

### Used by

- Weapon skill **hero set 4** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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
