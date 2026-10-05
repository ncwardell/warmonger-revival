---
title: "Explosion of Fury"
type: "skill"
id: 5003
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5003", "client: StringAll_Eng SkillComment_5003 (tooltip value tags)"]
name_key: "Skill_5003"
desc_key: "SkillComment_5003"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 102, "value": 75, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10004, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "ability_pct": 75, "buffs": [{"buff": 10004, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 75}
visual: 102
icon: {"file": "Skill_Dolorece_01.png", "index": 3}
used_by:
  - {"weapon_base": 62, "slot": 4, "items": [20020]}
---
<!-- generated:start -->
<!-- generated-keys: title=8d4a0e type=86a754 id=ac826c sources=22bb98 name_key=1957d5 desc_key=a86ea2 kind=356a19 kind_name=9bc378 target=7056fd range=902ba3 area=bade13 cost=9e049c cooldown=7d0c8c delivery=93a212 effect_kind=da4b92 effects=bd8c29 damage_or_effect=a62c96 tooltip_formula=2dadfc visual=c8306a icon=c919f8 used_by=02d332 -->
|  |  |
|---|---|
|  | ![Explosion of Fury](../assets/skills/5003.png) |
| **Skill id** | `5003` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 102 `PCD_Hammer_01_R_격노의 폭발` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 3 |

### Tooltip

> [Active] Sends out an explosion that deals `{EF_STATIC 100}``{EF_R_MDAM 75}` damage Decreases the Movement Speed of every target in the area.

Tooltip formula: **100 + 75% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 75 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10004-wrath-explosion-reduces-movement-speed\|Wrath Explosion: Reduces Movement Speed]] | 100 |

**Reading:** amount **100 + 75% Ability Power**; damage (magic?); applies [[wiki/buffs/10004-wrath-explosion-reduces-movement-speed|Wrath Explosion: Reduces Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 62: [[wiki/items/20020-magical-protect-hammer|Magical Protect Hammer]]
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
