---
title: "Savior's Gift"
type: "skill"
id: 5281
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5281"]
name_key: "Skill_5281"
desc_key: "SkillComment_5281"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 440}
cooldown: {"ms": 80000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10006, "rate": 100}
damage_or_effect: {}
visual: 366
icon: {"file": "Skill_Einsel_01.png", "index": 11}
used_by:
  - {"weapon_base": 64, "slot": 4, "items": [10002]}
---
<!-- generated:start -->
<!-- generated-keys: title=eee00b type=86a754 id=fa81c9 sources=459099 name_key=d84a1b desc_key=bdd9e3 kind=356a19 kind_name=9bc378 target=8871e4 range=fe5dbb area=d82541 cost=15d513 cooldown=dceb3e effect_kind=356a19 effects=54d841 damage_or_effect=bf21a9 visual=b00168 icon=5095da used_by=1647f0 -->
|  |  |
|---|---|
|  | ![Savior's Gift](../assets/skills/5281.png) |
| **Skill id** | `5281` |
| **Kind** | active (1) |
| **Target** | ground; self, party; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 440 MP |
| **Cooldown** | 80 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 366 `시즌1_PCE_Staff_03_R_구원의 선물` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 11 |

### Tooltip

> [Active] Summons a Recovery Zone to a designated location, restoring party members' HP by 5% of their target HP for 6 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,006 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 64: [[wiki/items/10002-magical-life-wand|Magical Life Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/10002-magical-life-wand|Magical Life Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
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
