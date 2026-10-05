---
title: "Squall"
type: "skill"
id: 10008
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10008", "client: StringAll_Eng SkillComment_10008 (tooltip value tags)"]
name_key: "Skill_10008"
desc_key: "SkillComment_10008"
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
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30011, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 85, "buffs": [{"buff": 30011, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 85
icon: {"file": "Skill_Einsel_01.png", "index": 0}
used_by:
  - {"weapon_base": 101, "slot": 1, "items": [11000]}
---
<!-- generated:start -->
<!-- generated-keys: title=d8beb2 type=86a754 id=e3a530 sources=d049e2 name_key=87c469 desc_key=b28792 kind=356a19 kind_name=9bc378 target=e84f24 range=fe5dbb area=29932d cost=d57e66 cooldown=f8ee77 delivery=93a212 effect_kind=da4b92 effects=546ce4 damage_or_effect=1d9912 tooltip_formula=67f65b visual=135224 icon=68aaec used_by=df48cb -->
|  |  |
|---|---|
|  | ![Squall](../assets/skills/10008.png) |
| **Skill id** | `10008` |
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

> [Active] Summon a strong squall inflicting `{EF_STATIC 80}``{EF_R_MDAM 85}` damage. Knocks up all targets it passes.

Tooltip formula: **80 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30011-breeze-increased-hp-and-mana-regeneration\|Breeze: Increased HP and Mana Regeneration]] | 100 |

**Reading:** amount **80 + 85% Ability Power**; damage (magic?); applies [[wiki/buffs/30011-breeze-increased-hp-and-mana-regeneration|Breeze: Increased HP and Mana Regeneration]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 101: [[wiki/items/11000-magical-storm-wand|Magical Storm Wand]]
- Nation policy 9 `PolicyName_9` (Policy.cdb, server-only; buff_or_skill)
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
