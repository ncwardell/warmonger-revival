---
title: "Head Butt"
type: "skill"
id: 5295
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5295", "client: StringAll_Eng SkillComment_5295 (tooltip value tags)"]
name_key: "Skill_5295"
desc_key: "SkillComment_5295"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
movement: "dash"
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 102, "value": 100, "rate": 0}
  - {"slot": 3, "type": 301, "value": 10350, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 75, "ability_pct": 100, "buffs": [{"buff": 10350, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_MDAM", "value": 100}
visual: 380
icon: {"file": "Skill_Dolorece_01.png", "index": 13}
used_by:
  - {"weapon_base": 67, "slot": 2, "items": [40003]}
---
<!-- generated:start -->
<!-- generated-keys: title=0c3928 type=86a754 id=93a90a sources=66a187 name_key=0e80b4 desc_key=f5f712 kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=da6e22 cooldown=4aa5a5 movement=5f1488 effect_kind=da4b92 effects=71cbfb damage_or_effect=ccae22 tooltip_formula=b1e6b5 visual=c30749 icon=dd02d3 used_by=a9b211 -->
|  |  |
|---|---|
|  | ![Head Butt](../assets/skills/5295.png) |
| **Skill id** | `5295` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Movement** | dash |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 380 `시즌1_PCD_Hammer_04_W_박치기` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 13 |

### Tooltip

> [Active] Headbutt the targeted enemy, dealing `{EF_STATIC 75}``{EF_R_MDAM 100}` Damage.

Tooltip formula: **75 + 100% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 100 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/10350\|Buff 10350]] | 100 |

**Reading:** amount **75 + 100% Ability Power**; damage (magic?); applies [[wiki/buffs/10350|Buff 10350]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 67: [[wiki/items/40003-magical-crush-hammer|Magical Crush Hammer]]

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
