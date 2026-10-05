---
title: "Bless of Crystal"
type: "skill"
id: 5015
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5015"]
name_key: "Skill_5015"
desc_key: "SkillComment_5015"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10017, "rate": 100}
  - {"slot": 2, "type": 314, "value": 10017, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10017, "rate": 100}, {"buff": 10017, "rate": 100}]}
visual: 200
icon: {"file": "Skill_Einsel_01.png", "index": 13}
used_by:
  - {"weapon_base": 4, "slot": 2, "items": [10003]}
---
<!-- generated:start -->
<!-- generated-keys: title=5b2ac8 type=86a754 id=95cde8 sources=f1b10b name_key=b7451d desc_key=295b2b kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=e4e7cf cooldown=e3989d effect_kind=da4b92 effects=c68868 damage_or_effect=3ca87d visual=9f9af0 icon=6b1db9 used_by=df9228 -->
|  |  |
|---|---|
|  | ![Bless of Crystal](wiki/assets/skills/5015.png) |
| **Skill id** | `5015` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 200 `PCE_Staff_04 W 수정의 기운` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 13 |

### Tooltip

> [Active] Draws power from the Crystal, increasing the Attack Speed and Movement Speed of yourself and a nearby ally for 14 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10017-draw-power-increases-attack-and-movement-speed\|Draw Power: Increases Attack and Movement Speed]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/10017-draw-power-increases-attack-and-movement-speed\|Draw Power: Increases Attack and Movement Speed]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10017-draw-power-increases-attack-and-movement-speed|Draw Power: Increases Attack and Movement Speed]] (100%); applies [[wiki/buffs/10017-draw-power-increases-attack-and-movement-speed|Draw Power: Increases Attack and Movement Speed]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 4: [[wiki/items/10003-magical-cystal-wand|Magical Cystal Wand]]
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
