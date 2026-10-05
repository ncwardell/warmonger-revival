---
title: "Divine"
type: "skill"
id: 20309
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20309", "client: StringAll_Eng SkillComment_20309 (tooltip value tags)"]
name_key: "Skill_20309"
desc_key: "SkillComment_20309"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 165}
cooldown: {"ms": 25000, "group": 0}
delivery: {"type": 4, "field_tick": 1.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 450
icon: {"file": "Skill_Boss_01.dds", "index": 45}
used_by:
  - {"weapon_base": 76, "slot": 7, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=ef4fc3 type=86a754 id=06682b sources=006ce5 name_key=43cf4e desc_key=3666f9 kind=356a19 kind_name=9bc378 target=47c86e range=b1d578 area=6d01a6 cost=966b26 cooldown=fec9d6 delivery=15a656 effect_kind=da4b92 effects=8a20a8 damage_or_effect=bf1784 tooltip_formula=c2e772 visual=d96adb icon=a6730c used_by=911e2f -->
|  |  |
|---|---|
|  | ![Divine](wiki/assets/skills/20309.png) |
| **Skill id** | `20309` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 10 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 165 MP |
| **Cooldown** | 25 s |
| **Delivery** | projectile / SFX (4), tick 1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 450 `피셔_천벌` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 45 |

### Tooltip

> [Active] Thunder strikes the targeted area, dealing `{EF_STATIC 80}``{EF_R_MDAM 80}` Damage.

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |

**Reading:** amount **80 + 80% Ability Power**; damage (magic?).

### Used by

- Weapon skill **hero set 3** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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
