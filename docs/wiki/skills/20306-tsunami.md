---
title: "Tsunami"
type: "skill"
id: 20306
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20306", "client: StringAll_Eng SkillComment_20306 (tooltip value tags)"]
name_key: "Skill_20306"
desc_key: "SkillComment_20306"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 12
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 15.0, "width_or_angle": 10.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 440}
cooldown: {"ms": 80000, "group": 0}
movement: "dash"
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20305, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 80, "buffs": [{"buff": 20305, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 447
icon: {"file": "Skill_Boss_01.dds", "index": 42}
used_by:
  - {"weapon_base": 76, "slot": 4, "items": [8007, 8507]}
---
<!-- generated:start -->
<!-- generated-keys: title=be5a45 type=86a754 id=e9e67b sources=7119cc name_key=dd759e desc_key=b13e38 kind=356a19 kind_name=9bc378 target=47c86e range=7b5200 area=f735bb cost=15d513 cooldown=dceb3e movement=5f1488 delivery=93a212 effect_kind=da4b92 effects=404646 damage_or_effect=98793a tooltip_formula=c2e772 visual=08d55d icon=749ca9 used_by=3441bf -->
|  |  |
|---|---|
|  | ![Tsunami](../assets/skills/20306.png) |
| **Skill id** | `20306` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 10 |
| **Range** | 12 (world units) |
| **Area** | line / rectangle?, radius 15, width/angle 10 (indicator `stick256x512.png`) |
| **Cost** | 440 MP |
| **Cooldown** | 80 s |
| **Movement** | dash |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 447 `피셔_해일` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 42 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_MDAM 80}` Magical Damage. When you fire a Tsunami, the other characters move with you.

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20305-tsunami-silenced-for-2-seconds\|Tsunami : silenced for 2 seconds]] | 100 |

**Reading:** amount **80 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/20305-tsunami-silenced-for-2-seconds|Tsunami : silenced for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 76: [[wiki/items/8007-tempest-fisher|Tempest Fisher]], [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]]
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
