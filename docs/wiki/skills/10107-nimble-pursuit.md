---
title: "Nimble Pursuit"
type: "skill"
id: 10107
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10107", "client: StringAll_Eng SkillComment_10107 (tooltip value tags)"]
name_key: "Skill_10107"
desc_key: "SkillComment_10107"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": [], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 7.0, "width_or_angle": 1.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 30098, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 30098, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 105}
visual: 245
icon: {"file": "Skill_Dolorece_01.png", "index": 16}
used_by:
  - {"weapon_base": 163, "slot": 1, "items": [21021]}
---
<!-- generated:start -->
<!-- generated-keys: title=7cd6eb type=86a754 id=ae208f sources=d723da name_key=d5776d desc_key=0ca5ba kind=356a19 kind_name=9bc378 target=5aa7bd range=902ba3 area=66be61 cost=8b4fa7 cooldown=0156ad movement=5f1488 effect_kind=356a19 effects=a242e0 damage_or_effect=4d252d tooltip_formula=4d8780 visual=3aed9b icon=197b6c used_by=687fe6 -->
|  |  |
|---|---|
|  | ![Nimble Pursuit](../assets/skills/10107.png) |
| **Skill id** | `10107` |
| **Kind** | active (1) |
| **Target** | ground; -; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 7, width/angle 1 (indicator `stick256x512.png`) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 245 `PCD_Cannon_01_Q 유연한 몸놀림` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 16 |

### Tooltip

> [Active]Dashing forward and attacking within 6 seconds will cause Damage to `{EF_STATIC 10}``{EF_R_DAM 105}`, giving additional damage to target health  3% .

Tooltip formula: **10 + 105% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30098-nimble-pursuit-your-next-basic-attack-deals-additional-damag\|Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/30098-nimble-pursuit-your-next-basic-attack-deals-additional-damag|Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 163: [[wiki/items/21021-magical-protect-cannon|Magical Protect Cannon]]

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
