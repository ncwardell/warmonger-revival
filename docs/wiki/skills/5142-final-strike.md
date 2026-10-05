---
title: "Final Strike"
type: "skill"
id: 5142
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5142", "client: StringAll_Eng SkillComment_5142 (tooltip value tags)"]
name_key: "Skill_5142"
desc_key: "SkillComment_5142"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 9
cost: {"type": 5, "type_name": "MP", "amount": 590}
cooldown: {"ms": 110000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 308, "value": 10163, "rate": 100}
  - {"slot": 4, "type": 301, "value": 10167, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 70, "buffs": [{"buff": 10163, "rate": 100}, {"buff": 10167, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 70}
requirements:
  - {"type": 10167, "a": 5, "b": 5143}
visual: 283
icon: {"file": "Skill_Miriam_01.png", "index": 27}
used_by:
  - {"weapon_base": 31, "slot": 4, "items": [35009]}
---
<!-- generated:start -->
<!-- generated-keys: title=602099 type=86a754 id=373d74 sources=41b865 name_key=6a6067 desc_key=50dd48 kind=356a19 kind_name=9bc378 target=069ef3 range=0ade7c cost=5baaf6 cooldown=e0e4dd movement=5f1488 effect_kind=356a19 effects=e5e17a damage_or_effect=b5f770 tooltip_formula=9ce175 requirements=0bd0d3 visual=3032a4 icon=b1d574 used_by=bd5ffe -->
|  |  |
|---|---|
|  | ![Final Strike](../assets/skills/5142.png) |
| **Skill id** | `5142` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 9 (world units) |
| **Cost** | 590 MP |
| **Cooldown** | 110 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 283 `PCM_Knife_05_R_최후의 한 방` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 27 |

### Tooltip

> [Active] Rushes to an enemy and dealing `{EF_STATIC 85}``{EF_R_DAM 70}` Damage. Grants you a Shield that absorbs 300 Damage.

Tooltip formula: **85 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 308 | applies buff (variant 308) | [[wiki/buffs/10163-final-strike-creates-a-shield-that-absorbs-damage-for-10-sec\|Final Strike: Creates a shield that absorbs Damage for 10 seconds.]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10167-final-strikes-possible-to-perform-the-final-strike-now\|Final Strikes : Possible to perform the Final Strike now]] | 100 |

**Reading:** amount **85 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10163-final-strike-creates-a-shield-that-absorbs-damage-for-10-sec|Final Strike: Creates a shield that absorbs Damage for 10 seconds.]] (100%); applies [[wiki/buffs/10167-final-strikes-possible-to-perform-the-final-strike-now|Final Strikes : Possible to perform the Final Strike now]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10167 | 5 | 5143 |

### Used by

- Weapon skill **R** of WeaponBase 31: [[wiki/items/35009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
