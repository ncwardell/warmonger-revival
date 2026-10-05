---
title: "Crushing Blow"
type: "skill"
id: 10067
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10067", "client: StringAll_Eng SkillComment_10067 (tooltip value tags)"]
name_key: "Skill_10067"
desc_key: "SkillComment_10067"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30058, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 85, "buffs": [{"buff": 30058, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 72
icon: {"file": "Skill_Dolorece_01.png", "index": 12}
used_by:
  - {"weapon_base": 145, "slot": 1, "items": [21003]}
---
<!-- generated:start -->
<!-- generated-keys: title=8e474c type=86a754 id=4bdf46 sources=be74c3 name_key=be25d1 desc_key=596ddd kind=356a19 kind_name=9bc378 target=d1cc1b range=77de68 area=344636 cost=f67772 cooldown=c9c532 effect_kind=da4b92 effects=b005da damage_or_effect=064ca3 tooltip_formula=33e085 visual=c09763 icon=372eb2 used_by=8af0b0 -->
|  |  |
|---|---|
|  | ![Crushing Blow](wiki/assets/skills/10067.png) |
| **Skill id** | `10067` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 72 `PCD_Hammer_04_Q_분쇄` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 12 |

### Tooltip

> [Active] Knocks up all enemies around you deals `{EF_STATIC 70}``{EF_R_MDAM 85}` Damage and silences them.

Tooltip formula: **70 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30058-crushing-blow-silenced-for-2-seconds\|Crushing Blow : Silenced for 2 seconds]] | 100 |

**Reading:** amount **70 + 85% Ability Power**; damage (magic?); applies [[wiki/buffs/30058-crushing-blow-silenced-for-2-seconds|Crushing Blow : Silenced for 2 seconds]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 145: [[wiki/items/21003-magical-crush-hammer|Magical Crush Hammer]]

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
