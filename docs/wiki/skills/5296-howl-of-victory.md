---
title: "Howl of Victory"
type: "skill"
id: 5296
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5296", "client: StringAll_Eng SkillComment_5296 (tooltip value tags)"]
name_key: "Skill_5296"
desc_key: "SkillComment_5296"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 0
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10351, "rate": 100}
  - {"slot": 4, "type": 131, "value": 1, "rate": 0}
damage_or_effect: {"kind": "heal HP", "base": 80, "ability_pct": 80, "buffs": [{"buff": 10351, "rate": 100}], "stats": [{"code": 131, "value": 1}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 381
icon: {"file": "Skill_Dolorece_01.png", "index": 14}
used_by:
  - {"weapon_base": 67, "slot": 3, "items": [40003]}
---
<!-- generated:start -->
<!-- generated-keys: title=68d82e type=86a754 id=307ed7 sources=c51db6 name_key=4cc0bc desc_key=16d0b5 kind=356a19 kind_name=9bc378 target=55b685 range=b6589f area=e9876d cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=17dcde damage_or_effect=4faf33 tooltip_formula=c2e772 visual=00f7ee icon=384e30 used_by=a9d40a -->
|  |  |
|---|---|
|  | ![Howl of Victory](../assets/skills/5296.png) |
| **Skill id** | `5296` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 0 (world units) |
| **Area** | circle, radius 6, width/angle 0 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 381 `시즌1_PCD_Hammer_04_E_승리의 포효` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 14 |

### Tooltip

> [Active] Heals all nearby party for `{EF_STATIC 80}``{EF_R_MDAM 80}`. Increases your HP Regeneration by 20% for 8 seconds

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10351-howl-of-victory-increased-health-regeneration\|Howl of Victory : Increased Health Regeneration]] | 100 |
| 4 | 131 | stat? Health(%) | 1 | 0 |

**Reading:** amount **80 + 80% Ability Power**; heal HP; applies [[wiki/buffs/10351-howl-of-victory-increased-health-regeneration|Howl of Victory : Increased Health Regeneration]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 67: [[wiki/items/40003-magical-crush-hammer|Magical Crush Hammer]]

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
