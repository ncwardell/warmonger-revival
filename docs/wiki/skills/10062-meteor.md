---
title: "Meteor"
type: "skill"
id: 10062
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10062", "client: StringAll_Eng SkillComment_10062 (tooltip value tags)"]
name_key: "Skill_10062"
desc_key: "SkillComment_10062"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 365}
cooldown: {"ms": 65000, "group": 0}
delivery: {"type": 4, "field_tick": 0.5}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 101, "value": 115, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30056, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 100, "attack_pct": 115, "buffs": [{"buff": 30056, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_DAM", "value": 115}
visual: 140
icon: {"file": "Skill_Dolorece_01.png", "index": 11}
used_by:
  - {"weapon_base": 144, "slot": 4, "items": [21002]}
---
<!-- generated:start -->
<!-- generated-keys: title=28626e type=86a754 id=18123d sources=6f16d9 name_key=e1f0cb desc_key=d12328 kind=356a19 kind_name=9bc378 target=e84f24 range=b1d578 area=e8b0ea cost=8c2feb cooldown=15bf08 delivery=6a22dc effect_kind=356a19 effects=d6c42e damage_or_effect=ee321a tooltip_formula=d98b57 visual=c28aca icon=be26ec used_by=d1b07b -->
|  |  |
|---|---|
|  | ![Meteor](wiki/assets/skills/10062.png) |
| **Skill id** | `10062` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 365 MP |
| **Cooldown** | 65 s |
| **Delivery** | projectile / SFX (4), tick 0.5 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 140 `PCD_Hammer_03_R_메테오 폭발` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 11 |

### Tooltip

> [Active] Calls down a meteor, dealing `{EF_STATIC 100}``{EF_R_DAM 115}` Damage. The force of the impact stuns all enemies for 2 seconds.

Tooltip formula: **100 + 115% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 115 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30056-meteor-stunned-for-2-seconds\|Meteor : Stunned for 2 seconds]] | 100 |

**Reading:** amount **100 + 115% Attack**; damage (physical?); applies [[wiki/buffs/30056-meteor-stunned-for-2-seconds|Meteor : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 144: [[wiki/items/21002-magical-dash-hammer|Magical Dash Hammer]]
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
