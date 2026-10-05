---
title: "Essential Blessing"
type: "skill"
id: 10280
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10280", "client: StringAll_Eng SkillComment_10280 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420 (E AP 90 → 60)"]
name_key: "Skill_10280"
desc_key: "SkillComment_10280"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 33
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 55, "rate": 0}
damage_or_effect: {"kind": "restore MP", "base": 85, "ability_pct": 55}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 55}
visual: 365
icon: {"file": "Skill_Einsel_01.png", "index": 10}
used_by:
  - {"weapon_base": 164, "slot": 3, "items": [11002]}
---
<!-- generated:start -->
<!-- generated-keys: title=8d9fe9 type=86a754 id=6f4c97 sources=4ee82e name_key=147bed desc_key=f0c111 kind=356a19 kind_name=9bc378 target=8b0de6 range=fe5dbb cost=58a4ca cooldown=133145 effect_kind=b6692e effects=b5d837 damage_or_effect=361f5b tooltip_formula=1e2666 visual=a0d043 icon=3e4948 used_by=b29ef8 -->
|  |  |
|---|---|
|  | ![Essential Blessing](../assets/skills/10280.png) |
| **Skill id** | `10280` |
| **Kind** | active (1) |
| **Target** | unit; ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | restore MP (33) |
| **Visual** | skillVisual 365 `시즌1_PCE_Staff_03_E_정기의 물결` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 10 |

### Tooltip

> [Active] Remedy Mana of the target with `{EF_STATIC 85}``{EF_R_MDAM 55}`

Tooltip formula: **85 + 55% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 55 | 0 |

**Reading:** amount **85 + 55% Ability Power**; restore MP.

### Used by

- Weapon skill **E** of WeaponBase 164: [[wiki/items/11002-magical-life-wand|Magical Life Wand]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) cut Magical Life Wand's E AP multiplier 90 → 60. The client tooltip reads 50 % AP (10280: 55 %). ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- AP multiplier: WM 0420 gives 60 %; the client tooltip gives 50 % (55 % on 10280). Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
