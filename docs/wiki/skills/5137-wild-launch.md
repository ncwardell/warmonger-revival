---
title: "Wild Launch"
type: "skill"
id: 5137
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5137", "client: StringAll_Eng SkillComment_5137 (tooltip value tags)"]
name_key: "Skill_5137"
desc_key: "SkillComment_5137"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 18
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 0.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 5137}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 307, "value": 10161, "rate": 100}
  - {"slot": 4, "type": 307, "value": 10162, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 90, "attack_pct": 70, "buffs": [{"buff": 10161, "rate": 100}, {"buff": 10162, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_DAM", "value": 70}
requirements:
  - {"type": 10161, "a": 1, "b": 1}
  - {"type": 10162, "a": 2, "b": 0}
visual: 279
icon: {"file": "Skill_Dolorece_01.png", "index": 31}
used_by:
  - {"weapon_base": 56, "slot": 4, "items": [40014]}
---
<!-- generated:start -->
<!-- generated-keys: title=0bc1de type=86a754 id=b52f3d sources=8da047 name_key=b3fce3 desc_key=bd716e kind=356a19 kind_name=9bc378 target=e84f24 range=9e6a55 area=44a509 cost=7e5cd4 cooldown=38a66e delivery=93a212 effect_kind=356a19 effects=71ffbf damage_or_effect=113f0e tooltip_formula=8b4625 requirements=f16d2b visual=1407c2 icon=14a444 used_by=c3a0dc -->
|  |  |
|---|---|
|  | ![Wild Launch](wiki/assets/skills/5137.png) |
| **Skill id** | `5137` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 18 (world units) |
| **Area** | circle, radius 1, width/angle 0 (indicator `stick256x512.png`) |
| **Cost** | 50 MP |
| **Cooldown** | 2 s (group 5137) |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 279 `PCD_Cannon_05_R_무차별 발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 31 |

### Tooltip

> [Active] Launch a missile that deals `{EF_STATIC 90}``{EF_R_DAM 70}` Damage. Every third missile deals considerably more Damage. Missiles are stored over time up to a maximum of 7.

Tooltip formula: **90 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 307 | applies buff (variant 307) | [[wiki/buffs/10161-indiscriminate-launch-rockets-available-in-the-store\|Indiscriminate Launch: Rockets available in the Store]] | 100 |
| 4 | 307 | applies buff (variant 307) | [[wiki/buffs/10162-indiscriminate-launch-third-hit\|Indiscriminate Launch : Third hit]] | 100 |

**Reading:** amount **90 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10161-indiscriminate-launch-rockets-available-in-the-store|Indiscriminate Launch: Rockets available in the Store]] (100%); applies [[wiki/buffs/10162-indiscriminate-launch-third-hit|Indiscriminate Launch : Third hit]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10161 | 1 | 1 |
| 10162 | 2 | 0 |

### Used by

- Weapon skill **R** of WeaponBase 56: [[wiki/items/40014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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
