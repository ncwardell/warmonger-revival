---
title: "Crystal Nova"
type: "skill"
id: 10016
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10016"]
name_key: "Skill_10016"
desc_key: "SkillComment_10016"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "enemy", "party"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 7.0, "width_or_angle": 7.0}
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 30018, "rate": 100}
  - {"slot": 2, "type": 314, "value": 30018, "rate": 100}
  - {"slot": 3, "type": 314, "value": 30019, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30018, "rate": 100}, {"buff": 30018, "rate": 100}, {"buff": 30019, "rate": 100}]}
visual: 201
icon: {"file": "Skill_Einsel_01.png", "index": 14}
used_by:
  - {"weapon_base": 104, "slot": 3, "items": [11003]}
---
<!-- generated:start -->
<!-- generated-keys: title=1b5868 type=86a754 id=d5483a sources=17dd81 name_key=242cba desc_key=004a7d kind=356a19 kind_name=9bc378 target=94d713 range=902ba3 area=1bac4b cost=da6e22 cooldown=e3989d effect_kind=b6589f effects=38431b damage_or_effect=9e80e2 visual=7f03f3 icon=baee3b used_by=079d66 -->
|  |  |
|---|---|
|  | ![Crystal Nova](../assets/skills/10016.png) |
| **Skill id** | `10016` |
| **Kind** | active (1) |
| **Target** | self; self, enemy, party; units: monster, player; up to 10 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 7, width/angle 7 |
| **Cost** | 90 MP |
| **Cooldown** | 15 s |
| **Visual** | skillVisual 201 `PCE_Staff_04 E 수정파편` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 14 |

### Tooltip

> [Active] Increases the Armor and Magic Resistance of the nearby party by 20% for 5 seconds Decreases Armor and Magic Resistance of nearby enemies by 20% for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30018-crystal-burst-increases-armor-and-magic-resistance\|Crystal Burst: Increases Armor and Magic Resistance]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/30018-crystal-burst-increases-armor-and-magic-resistance\|Crystal Burst: Increases Armor and Magic Resistance]] | 100 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30019-crystal-burst-reduced-armor-and-magic-resistance\|Crystal Burst : Reduced Armor and Magic Resistance]] | 100 |

**Reading:** applies [[wiki/buffs/30018-crystal-burst-increases-armor-and-magic-resistance|Crystal Burst: Increases Armor and Magic Resistance]] (100%); applies [[wiki/buffs/30018-crystal-burst-increases-armor-and-magic-resistance|Crystal Burst: Increases Armor and Magic Resistance]] (100%); applies [[wiki/buffs/30019-crystal-burst-reduced-armor-and-magic-resistance|Crystal Burst : Reduced Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 104: [[wiki/items/11003-magical-cystal-wand|Magical Cystal Wand]]
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
