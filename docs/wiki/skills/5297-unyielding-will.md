---
title: "Unyielding Will"
type: "skill"
id: 5297
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5297"]
name_key: "Skill_5297"
desc_key: "SkillComment_5297"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10352, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10352, "rate": 100}]}
visual: 382
icon: {"file": "Skill_Dolorece_01.png", "index": 15}
used_by:
  - {"weapon_base": 67, "slot": 4, "items": [40003]}
---
<!-- generated:start -->
<!-- generated-keys: title=066fdc type=86a754 id=71e05e sources=a8de9b name_key=ca6e77 desc_key=a5ac52 kind=356a19 kind_name=9bc378 target=d99f6c range=ac3478 cost=ff5a60 cooldown=ad2ac8 effect_kind=b6589f effects=a1bfac damage_or_effect=64b893 visual=d0226f icon=a431e0 used_by=ff0a85 -->
|  |  |
|---|---|
|  | ![Unyielding Will](wiki/assets/skills/5297.png) |
| **Skill id** | `5297` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Visual** | skillVisual 382 `시즌1_PCD_Hammer_04_R_꺾을 수 없는 의지` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 15 |

### Tooltip

> [Active] Reduces your Damage taken by 50% over 5 seconds. You gain 40 Attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10352-unyielding-will-reduce-50-all-type-of-damage-during-5-secs-a\|Unyielding Will : Reduce 50% all type of damage during 5 secs and get 40 Attack.]] | 100 |

**Reading:** applies [[wiki/buffs/10352-unyielding-will-reduce-50-all-type-of-damage-during-5-secs-a|Unyielding Will : Reduce 50% all type of damage during 5 secs and get 40 Attack.]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 67: [[wiki/items/40003-magical-crush-hammer|Magical Crush Hammer]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
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
