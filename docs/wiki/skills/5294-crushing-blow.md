---
title: "Crushing Blow"
type: "skill"
id: 5294
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5294", "client: StringAll_Eng SkillComment_5294 (tooltip value tags)"]
name_key: "Skill_5294"
desc_key: "SkillComment_5294"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10349, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 80, "buffs": [{"buff": 10349, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 379
icon: {"file": "Skill_Dolorece_01.png", "index": 12}
used_by:
  - {"weapon_base": 67, "slot": 1, "items": [40003]}
---
<!-- generated:start -->
<!-- generated-keys: title=8e474c type=86a754 id=20f173 sources=d9f16d name_key=c15f1c desc_key=03a0b9 kind=356a19 kind_name=9bc378 target=d1cc1b range=77de68 area=6d01a6 cost=f67772 cooldown=c9c532 effect_kind=da4b92 effects=5a33f8 damage_or_effect=9d47ff tooltip_formula=e4dbdd visual=c829eb icon=372eb2 used_by=b64062 -->
|  |  |
|---|---|
|  | ![Crushing Blow](wiki/assets/skills/5294.png) |
| **Skill id** | `5294` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 379 `시즌1_PCD_Hammer_04_Q_분쇄` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 12 |

### Tooltip

> [Active] Knocks away all nearby enemies, dealing `{EF_STATIC 70}``{EF_R_MDAM 80}` Damage and silences them.

Tooltip formula: **70 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10349-crushing-blow-silenced\|Crushing Blow : Silenced]] | 100 |

**Reading:** amount **70 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10349-crushing-blow-silenced|Crushing Blow : Silenced]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 67: [[wiki/items/40003-magical-crush-hammer|Magical Crush Hammer]]

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
