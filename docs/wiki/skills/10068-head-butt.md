---
title: "Head Butt"
type: "skill"
id: 10068
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10068", "client: StringAll_Eng SkillComment_10068 (tooltip value tags)"]
name_key: "Skill_10068"
desc_key: "SkillComment_10068"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 105, "rate": 0}
  - {"slot": 3, "type": 301, "value": 30059, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 105, "buffs": [{"buff": 30059, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 105}
visual: 73
icon: {"file": "Skill_Dolorece_01.png", "index": 13}
used_by:
  - {"weapon_base": 145, "slot": 2, "items": [21003]}
---
<!-- generated:start -->
<!-- generated-keys: title=0c3928 type=86a754 id=932b68 sources=d303e9 name_key=d395a7 desc_key=987209 kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=da6e22 cooldown=4aa5a5 movement=5f1488 effect_kind=356a19 effects=0a3301 damage_or_effect=e0c39c tooltip_formula=3f9719 visual=35e995 icon=dd02d3 used_by=ecf528 -->
|  |  |
|---|---|
|  | ![Head Butt](wiki/assets/skills/10068.png) |
| **Skill id** | `10068` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 73 `PCD_Hammer_04_W_박치기` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 13 |

### Tooltip

> [Active] Headbutt the targeted enemy dealing `{EF_STATIC 75}``{EF_R_DAM 105}` Damage.

Tooltip formula: **75 + 105% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 105 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/30059-head-butt-pushback\|Head Butt : Pushback]] | 100 |

**Reading:** amount **75 + 105% Attack**; damage (physical?); applies [[wiki/buffs/30059-head-butt-pushback|Head Butt : Pushback]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 145: [[wiki/items/21003-magical-crush-hammer|Magical Crush Hammer]]

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
