---
title: "Petrification"
type: "skill"
id: 5180
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5180"]
name_key: "Skill_5180"
desc_key: "SkillComment_5180"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10214, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10214, "rate": 100}]}
visual: 315
icon: {"file": "Skill_Einsel_01.png", "index": 33}
used_by:
  - {"weapon_base": 21, "slot": 2, "items": [10020]}
---
<!-- generated:start -->
<!-- generated-keys: title=c10363 type=86a754 id=209e73 sources=161ae6 name_key=a1513a desc_key=0ab9a1 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=deac18 cooldown=a93f07 delivery=93a212 effect_kind=b6589f effects=814e08 damage_or_effect=5a65c8 visual=f6b9b6 icon=072780 used_by=617e6e -->
|  |  |
|---|---|
|  | ![Petrification](../assets/skills/5180.png) |
| **Skill id** | `5180` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Delivery** | projectile / SFX |
| **Visual** | skillVisual 315 `PCE_Staff_08_W_변신해!` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 33 |

### Tooltip

> [Active] Turns the enemy into stone for 2 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10214-petrification-stunned-for-2-seconds\|Petrification : Stunned for 2 seconds]] | 100 |

**Reading:** applies [[wiki/buffs/10214-petrification-stunned-for-2-seconds|Petrification : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 21: [[wiki/items/10020-magical-devil-wand|Magical Devil Wand]]
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
