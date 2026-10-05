---
title: "Fisher's cries"
type: "skill"
id: 20310
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20310", "client: StringAll_Eng SkillComment_20310 (tooltip value tags)"]
name_key: "Skill_20310"
desc_key: "SkillComment_20310"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: null
cooldown: {"ms": 80000, "group": 0}
effect_kind: 134
effects:
  - {"slot": 1, "type": 317, "value": 20308, "rate": 100}
  - {"slot": 2, "type": 308, "value": 20308, "rate": 100}
  - {"slot": 3, "type": 134, "value": 20, "rate": 100}
damage_or_effect: {"kind": "effect kind 134", "buffs": [{"buff": 20308, "rate": 100}, {"buff": 20308, "rate": 100}], "stats": [{"code": 134, "value": 20}]}
tooltip_formula:
  - {"tag": "EF_R_MANA", "value": 20}
visual: 451
icon: {"file": "Skill_Boss_01.dds", "index": 46}
used_by:
  - {"weapon_base": 76, "slot": 8, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=8372a5 type=86a754 id=79b42e sources=22df42 name_key=6cd115 desc_key=d2a3ad kind=356a19 kind_name=9bc378 target=55b685 range=356a19 area=d82541 cost=2be88c cooldown=dceb3e effect_kind=95e815 effects=fd29fa damage_or_effect=546439 tooltip_formula=2c35bf visual=9d4650 icon=f9031f used_by=90e00c -->
|  |  |
|---|---|
|  | ![Fisher's cries](wiki/assets/skills/20310.png) |
| **Skill id** | `20310` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cooldown** | 80 s |
| **Effect kind** | ? (134) |
| **Visual** | skillVisual 451 `피셔_피셔의 울부짖음` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 46 |

### Tooltip

> [Active] It now consumes 20% of Mana and creates 200 `{EF_R_MANA 20}` shields of Mana for you and your allies.

Tooltip formula: **20% Mana** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/20308-fisher-s-cries-creates-a-absorvs-damage-for-5-seconds\|Fisher's cries : Creates a absorvs damage for 5 seconds]] | 100 |
| 2 | 308 | applies buff (variant 308) | [[wiki/buffs/20308-fisher-s-cries-creates-a-absorvs-damage-for-5-seconds\|Fisher's cries : Creates a absorvs damage for 5 seconds]] | 100 |
| 3 | 134 | stat? Mana Regeneration(%) | 20 | 100 |

**Reading:** effect kind 134; applies [[wiki/buffs/20308-fisher-s-cries-creates-a-absorvs-damage-for-5-seconds|Fisher's cries : Creates a absorvs damage for 5 seconds]] (100%); applies [[wiki/buffs/20308-fisher-s-cries-creates-a-absorvs-damage-for-5-seconds|Fisher's cries : Creates a absorvs damage for 5 seconds]] (100%).

### Used by

- Weapon skill **hero set 4** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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
