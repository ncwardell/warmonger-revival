---
title: "Blessing of Light"
type: "skill"
id: 10279
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10279", "client: StringAll_Eng SkillComment_10279 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420 (W AP 80 → 60)"]
name_key: "Skill_10279"
desc_key: "SkillComment_10279"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 55, "rate": 0}
damage_or_effect: {"kind": "heal HP", "base": 80, "ability_pct": 55}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 55}
visual: 364
icon: {"file": "Skill_Einsel_01.png", "index": 9}
used_by:
  - {"weapon_base": 164, "slot": 2, "items": [11002]}
---
<!-- generated:start -->
<!-- generated-keys: title=2cbe2e type=86a754 id=3bd335 sources=0429d3 name_key=ec4d52 desc_key=cf254a kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=15298d damage_or_effect=d394c6 tooltip_formula=388a94 visual=56e43a icon=aaa141 used_by=cd3d50 -->
|  |  |
|---|---|
|  | ![Blessing of Light](wiki/assets/skills/10279.png) |
| **Skill id** | `10279` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 364 `시즌1_PCE_Staff_03_W_소생의 숨결` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 9 |

### Tooltip

> [Active] Heal the target with `{EF_STATIC 80}``{EF_R_MDAM 55}`

Tooltip formula: **80 + 55% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 55 | 0 |

**Reading:** amount **80 + 55% Ability Power**; heal HP.

### Used by

- Weapon skill **W** of WeaponBase 164: [[wiki/items/11002-magical-life-wand|Magical Life Wand]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) cut Magical Life Wand's W AP multiplier 80 → 60. The client tooltip reads 50 % AP (10279: 55 %). ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- AP multiplier: WM 0420 gives 60 %; the client tooltip gives 50 % (55 % on 10279). Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
