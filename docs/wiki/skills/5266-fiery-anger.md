---
title: "Fiery Anger"
type: "skill"
id: 5266
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5266", "client: StringAll_Eng SkillComment_5266 (tooltip value tags)"]
name_key: "Skill_5266"
desc_key: "SkillComment_5266"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10329, "rate": 100}
  - {"slot": 2, "type": 308, "value": 10330, "rate": 100}
  - {"slot": 3, "type": 301, "value": 10331, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10329, "rate": 100}, {"buff": 10330, "rate": 100}, {"buff": 10331, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_DAM", "value": 10}
requirements:
  - {"type": 10331, "a": 5, "b": 5267}
visual: 471
icon: {"file": "Skill_Einsel_01.png", "index": 36}
used_by:
  - {"weapon_base": 6, "slot": 1, "items": [10005]}
---
<!-- generated:start -->
<!-- generated-keys: title=c0a935 type=86a754 id=04c7c3 sources=4d3779 name_key=2e2b7d desc_key=f699b4 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=060055 cooldown=5b7687 effect_kind=356a19 effects=26fed8 damage_or_effect=87c7ab tooltip_formula=c66bd8 requirements=e13712 visual=5e5ad0 icon=574aef used_by=49f7a6 -->
|  |  |
|---|---|
|  | ![Fiery Anger](../assets/skills/5266.png) |
| **Skill id** | `5266` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 471 `PCE_SwordShd_01_Q_불의 진노_시전` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 36 |

### Tooltip

> [Active] First use: Increases your Movement Speed by +70 and generates a Shield that absorbs 300`{EF_R_DAM 10}` Damage.

Tooltip formula: **10% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10329-anger-of-fire-movement-70-4secs\|Anger of fire : Movement +70 (4Secs)]] | 100 |
| 2 | 308 | applies buff (variant 308) | [[wiki/buffs/10330-anger-of-fire-creates-a-absorvs-damage-for-10-seconds\|Anger of fire : Creates a absorvs damage for 10 seconds]] | 100 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/10331\|Buff 10331]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10329-anger-of-fire-movement-70-4secs|Anger of fire : Movement +70 (4Secs)]] (100%); applies [[wiki/buffs/10330-anger-of-fire-creates-a-absorvs-damage-for-10-seconds|Anger of fire : Creates a absorvs damage for 10 seconds]] (100%); applies [[wiki/buffs/10331|Buff 10331]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10331 | 5 | 5267 |

### Used by

- Weapon skill **Q** of WeaponBase 6: [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]]
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
