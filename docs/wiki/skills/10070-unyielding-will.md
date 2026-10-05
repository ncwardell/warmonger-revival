---
title: "Unyielding Will"
type: "skill"
id: 10070
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10070"]
name_key: "Skill_10070"
desc_key: "SkillComment_10070"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 30061, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30061, "rate": 100}]}
visual: 75
icon: {"file": "Skill_Dolorece_01.png", "index": 15}
used_by:
  - {"weapon_base": 145, "slot": 4, "items": [21003]}
---
<!-- generated:start -->
<!-- generated-keys: title=066fdc type=86a754 id=2b1207 sources=765ea4 name_key=593d28 desc_key=712fd8 kind=356a19 kind_name=9bc378 target=d99f6c range=ac3478 cost=ff5a60 cooldown=ad2ac8 effect_kind=b6589f effects=bc6d3c damage_or_effect=0f2fe8 visual=450dde icon=a431e0 used_by=553953 -->
|  |  |
|---|---|
|  | ![Unyielding Will](../assets/skills/10070.png) |
| **Skill id** | `10070` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Visual** | skillVisual 75 `PCD_Hammer_04_R_꺽을 수 없는 의지` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 15 |

### Tooltip

> [Active] Reduces Damage of all types by 50% for 5 seconds and gives 40 Attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/30061-unyielding-will-reduce-50-all-type-of-damage-during-5-second\|Unyielding Will : Reduce 50% all type of damage during 5 seconds and get 40 Attack.]] | 100 |

**Reading:** applies [[wiki/buffs/30061-unyielding-will-reduce-50-all-type-of-damage-during-5-second|Unyielding Will : Reduce 50% all type of damage during 5 seconds and get 40 Attack.]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 145: [[wiki/items/21003-magical-crush-hammer|Magical Crush Hammer]]

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
