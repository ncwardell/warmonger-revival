---
title: "Final Strike"
type: "skill"
id: 5291
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5291", "client: StringAll_Eng SkillComment_5291 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0712 (R silence 2 → 3 s)"]
name_key: "Skill_5291"
desc_key: "SkillComment_5291"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 9
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
movement: "dash"
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
  - {"slot": 3, "type": 308, "value": 10346, "rate": 100}
  - {"slot": 4, "type": 301, "value": 10347, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 85, "buffs": [{"buff": 10346, "rate": 100}, {"buff": 10347, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 85}
  - {"tag": "EF_R_DAM", "value": 10}
requirements:
  - {"type": 10347, "a": 5, "b": 5292}
visual: 376
icon: {"file": "Skill_Miriam_01.png", "index": 27}
used_by:
  - {"weapon_base": 66, "slot": 4, "items": [15009]}
---
<!-- generated:start -->
<!-- generated-keys: title=602099 type=86a754 id=96307f sources=85c973 name_key=0eb8d5 desc_key=6470c7 kind=356a19 kind_name=9bc378 target=069ef3 range=0ade7c cost=ff5a60 cooldown=ad2ac8 movement=5f1488 effect_kind=da4b92 effects=cf88d1 damage_or_effect=bfba72 tooltip_formula=e747c0 requirements=ec474b visual=b6e2ef icon=b1d574 used_by=c5cf95 -->
|  |  |
|---|---|
|  | ![Final Strike](../assets/skills/5291.png) |
| **Skill id** | `5291` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 9 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Movement** | dash |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 376 `시즌1_PCM_Knife_05_R_최후의 한방` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 27 |

### Tooltip

> [Active] Rushes to an enemy, dealing `{EF_STATIC 85}``{EF_R_MDAM 85}` Damage. Grants you a Shield that absorbs 300 `{EF_R_DAM 10}` Damage.

Tooltip formula: **85 + 85% Ability Power + 10% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |
| 3 | 308 | applies buff (variant 308) | [[wiki/buffs/10346-final-strikes-creates-a-absorvs-damage-for-10-seconds\|Final Strikes : Creates a absorvs damage for 10 seconds]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10347-final-strikes-possible-to-perform-the-final-strike-now\|Final Strikes : Possible to perform the Final Strike now]] | 100 |

**Reading:** amount **85 + 85% Ability Power**; damage (magic?); applies [[wiki/buffs/10346-final-strikes-creates-a-absorvs-damage-for-10-seconds|Final Strikes : Creates a absorvs damage for 10 seconds]] (100%); applies [[wiki/buffs/10347-final-strikes-possible-to-perform-the-final-strike-now|Final Strikes : Possible to perform the Final Strike now]] (100%).

> [!warning] The tooltip (85 + 85% Ability Power + 10% Attack) and the effect slots (85 + 85% Ability Power) disagree; one of them was out of date in the shipped client.

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10347 | 5 | 5292 |

### Used by

- Weapon skill **R** of WeaponBase 66: [[wiki/items/15009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0712](https://steamcommunity.com/games/718790/announcements/detail/2838841185432966428) raised Skeleton King's Magic Dagger's R silence 2 → 3 s. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- The client R tooltip (Final Strike) mentions a shield, not a silence; the client's silence buffs ("Assassination : Silenced") last 2 s and come from the W. Which skill the 0712 note meant is unclear.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
