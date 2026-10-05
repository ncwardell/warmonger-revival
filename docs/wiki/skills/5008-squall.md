---
title: "Squall"
type: "skill"
id: 5008
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5008", "client: StringAll_Eng SkillComment_5008 (tooltip value tags)"]
name_key: "Skill_5008"
desc_key: "SkillComment_5008"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 8
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 3.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 105}
cooldown: {"ms": 13000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10011, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 80, "buffs": [{"buff": 10011, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 85
icon: {"file": "Skill_Einsel_01.png", "index": 0}
used_by:
  - {"weapon_base": 1, "slot": 1, "items": [10000]}
---
<!-- generated:start -->
<!-- generated-keys: title=d8beb2 type=86a754 id=1e86f9 sources=cd5bdd name_key=53b00c desc_key=fe9fd3 kind=356a19 kind_name=9bc378 target=e84f24 range=fe5dbb area=29932d cost=d57e66 cooldown=f8ee77 delivery=93a212 effect_kind=da4b92 effects=66f792 damage_or_effect=9e402a tooltip_formula=c2e772 visual=135224 icon=68aaec used_by=3b33da -->
|  |  |
|---|---|
|  | ![Squall](wiki/assets/skills/5008.png) |
| **Skill id** | `5008` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 8 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 3 (indicator `stick256x512.png`) |
| **Cost** | 105 MP |
| **Cooldown** | 13 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 85 `PCE_Staff_01_Q_고요한 돌풍` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 0 |

### Tooltip

> [Active] Summon a strong squall inflicting `{EF_STATIC 80}``{EF_R_MDAM 80}` damage. Knocks up all targets it passes.

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10011-breeze-increased-hp-and-mana-regeneration\|Breeze: Increased HP and Mana Regeneration]] | 100 |

**Reading:** amount **80 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10011-breeze-increased-hp-and-mana-regeneration|Breeze: Increased HP and Mana Regeneration]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 1: [[wiki/items/10000-magical-storm-wand|Magical Storm Wand]]
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
