---
title: "Water of deceleration"
type: "skill"
id: 20302
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20302", "client: StringAll_Eng SkillComment_20302 (tooltip value tags)"]
name_key: "Skill_20302"
desc_key: "SkillComment_20302"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20302, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 60, "ability_pct": 70, "buffs": [{"buff": 20302, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 445
icon: {"file": "Skill_Boss_01.dds", "index": 39}
used_by:
  - {"weapon_base": 76, "slot": 1, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=fb9b2b type=86a754 id=6f7911 sources=957b62 name_key=dcd4e5 desc_key=9658ab kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=728214 cost=060055 cooldown=5b7687 delivery=93a212 effect_kind=da4b92 effects=be4665 damage_or_effect=5faef5 tooltip_formula=6b7157 visual=ac9c95 icon=e1b084 used_by=cbbac9 -->
|  |  |
|---|---|
|  | ![Water of deceleration](../assets/skills/20302.png) |
| **Skill id** | `20302` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 445 `피셔_감속의 물방울` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 39 |

### Tooltip

> [Active] Fires a water drop in a specified direction, inflicts `{EF_STATIC 60}``{EF_R_MDAM 70}` Magic Damage to enemies and reduces their Movement Speed.

Tooltip formula: **60 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20302-water-of-deceleration-reduced-moovement-speed-3-secs\|Water of deceleration : Reduced Moovement Speed (3 Secs)]] | 100 |

**Reading:** amount **60 + 70% Ability Power**; damage (magic?); applies [[wiki/buffs/20302-water-of-deceleration-reduced-moovement-speed-3-secs|Water of deceleration : Reduced Moovement Speed (3 Secs)]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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
