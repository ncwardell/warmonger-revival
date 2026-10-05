---
title: "Fang of Knives"
type: "skill"
id: 5141
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5141", "client: StringAll_Eng SkillComment_5141 (tooltip value tags)"]
name_key: "Skill_5141"
desc_key: "SkillComment_5141"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10165, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 70, "buffs": [{"buff": 10165, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 282
icon: {"file": "Skill_Miriam_01.png", "index": 26}
used_by:
  - {"weapon_base": 31, "slot": 3, "items": [35009]}
---
<!-- generated:start -->
<!-- generated-keys: title=09def0 type=86a754 id=a50a84 sources=a5fab6 name_key=5fd707 desc_key=40cfc6 kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=e8b0ea cost=911ade cooldown=628d31 effect_kind=356a19 effects=b688b8 damage_or_effect=29c970 tooltip_formula=321def visual=267b97 icon=5f1bf5 used_by=9dfb0b -->
|  |  |
|---|---|
|  | ![Fang of Knives](../assets/skills/5141.png) |
| **Skill id** | `5141` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 282 `PCM_Knife_05_E_정면승부` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 26 |

### Tooltip

> [Active] Damages all nearby enemies with `{EF_STATIC 80}``{EF_R_DAM 70}` and decreases their Movement Speed briefly by 30%.

Tooltip formula: **80 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10165-fang-of-knives-reduces-movement-speed\|Fang of Knives: Reduces Movement Speed]] | 100 |

**Reading:** amount **80 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10165-fang-of-knives-reduces-movement-speed|Fang of Knives: Reduces Movement Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 31: [[wiki/items/35009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
