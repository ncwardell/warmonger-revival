---
title: "Merciless Chaser"
type: "skill"
id: 10032
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10032", "client: StringAll_Eng SkillComment_10032 (tooltip value tags)"]
name_key: "Skill_10032"
desc_key: "SkillComment_10032"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": [], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 30029, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 30029, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 105}
visual: 182
icon: {"file": "Skill_Miriam_01.png", "index": 0}
used_by:
  - {"weapon_base": 122, "slot": 1, "items": [16000]}
---
<!-- generated:start -->
<!-- generated-keys: title=cfa33d type=86a754 id=b98a97 sources=151635 name_key=a34286 desc_key=7205b4 kind=356a19 kind_name=9bc378 target=5aa7bd range=902ba3 cost=8b4fa7 cooldown=0156ad movement=5f1488 effect_kind=356a19 effects=59d53e damage_or_effect=d87dca tooltip_formula=4d8780 visual=58f074 icon=bfcc89 used_by=bc1e8c -->
|  |  |
|---|---|
|  | ![Merciless Chaser](wiki/assets/skills/10032.png) |
| **Skill id** | `10032` |
| **Kind** | active (1) |
| **Target** | ground; -; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 182 `PCM_Bow_01_Q_냉혹한 추격자` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 0 |

### Tooltip

> [Active] You jump forward, increasing the damage of your next basic attack by `{EF_STATIC 10}``{EF_R_DAM 105}` The damage bonus gets increased by 3% of the enemy's current health.

Tooltip formula: **10 + 105% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30029-merciless-chase-your-next-basic-attack-deals-additional-dama\|Merciless Chase : Your next basic attack deals additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/30029-merciless-chase-your-next-basic-attack-deals-additional-dama|Merciless Chase : Your next basic attack deals additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 122: [[wiki/items/16000-magical-shadow-bow|Magical Shadow Bow]]
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
