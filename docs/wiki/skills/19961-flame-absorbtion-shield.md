---
title: "Flame Absorbtion Shield"
type: "skill"
id: 19961
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19961"]
name_key: "Skill_19961"
desc_key: "SkillComment_19961"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 415}
cooldown: {"ms": 75000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 304, "value": 19960, "rate": 100}
  - {"slot": 2, "type": 301, "value": 19961, "rate": 100}
  - {"slot": 3, "type": 317, "value": 19960, "rate": 100}
  - {"slot": 4, "type": 314, "value": 19961, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 19960, "rate": 100}, {"buff": 19961, "rate": 100}, {"buff": 19960, "rate": 100}, {"buff": 19961, "rate": 100}]}
visual: 411
icon: {"file": "Skill_Boss_01.dds", "index": 11}
used_by:
  - {"weapon_base": 74, "slot": 8, "items": [8005, 8505]}
---
<!-- generated:start -->
<!-- generated-keys: title=0f12db type=86a754 id=f4d46d sources=85e825 name_key=cafb06 desc_key=ee5478 kind=356a19 kind_name=9bc378 target=55b685 range=1b6453 area=6d01a6 cost=d55bc7 cooldown=cf1f8c effect_kind=356a19 effects=e6a946 damage_or_effect=ca0678 visual=83fdc3 icon=e77ed7 used_by=917eaf -->
|  |  |
|---|---|
|  | ![Flame Absorbtion Shield](wiki/assets/skills/19961.png) |
| **Skill id** | `19961` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 415 MP |
| **Cooldown** | 75 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 411 `모리온_화염 장막` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 11 |

### Tooltip

> [Active] Creates a shield for your nearby allies, greatly increasing Armor and Resistance.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 304 | applies buff (variant 304) | [[wiki/buffs/19960-flame-absorb-shield-creates-a-absorvs-damage-for-4-seconds\|Flame Absorb shield : Creates a absorvs damage for 4 seconds]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/19961-flame-absorb-shield-you-gain-30-armor-and-magic-resistance\|Flame Absorb shield : You gain 30% Armor and Magic Resistance]] | 100 |
| 3 | 317 | applies buff (variant 317) | [[wiki/buffs/19960-flame-absorb-shield-creates-a-absorvs-damage-for-4-seconds\|Flame Absorb shield : Creates a absorvs damage for 4 seconds]] | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/19961-flame-absorb-shield-you-gain-30-armor-and-magic-resistance\|Flame Absorb shield : You gain 30% Armor and Magic Resistance]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/19960-flame-absorb-shield-creates-a-absorvs-damage-for-4-seconds|Flame Absorb shield : Creates a absorvs damage for 4 seconds]] (100%); applies [[wiki/buffs/19961-flame-absorb-shield-you-gain-30-armor-and-magic-resistance|Flame Absorb shield : You gain 30% Armor and Magic Resistance]] (100%); applies [[wiki/buffs/19960-flame-absorb-shield-creates-a-absorvs-damage-for-4-seconds|Flame Absorb shield : Creates a absorvs damage for 4 seconds]] (100%); applies [[wiki/buffs/19961-flame-absorb-shield-you-gain-30-armor-and-magic-resistance|Flame Absorb shield : You gain 30% Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **hero set 4** of WeaponBase 74: [[wiki/items/8005-morion|Morion]], [[wiki/items/8505-crystal-morion|Crystal : Morion]]
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
