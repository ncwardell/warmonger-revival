---
title: "Wild Threat"
type: "skill"
id: 5056
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5056", "client: StringAll_Eng SkillComment_5056 (tooltip value tags)"]
name_key: "Skill_5056"
desc_key: "SkillComment_5056"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 30, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10052, "rate": 100}
  - {"slot": 4, "type": 314, "value": 10141, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 85, "ability_pct": 30, "buffs": [{"buff": 10052, "rate": 100}, {"buff": 10141, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 30}
visual: 108
icon: {"file": "Skill_Miriam_01.png", "index": 21}
used_by:
  - {"weapon_base": 28, "slot": 2, "items": [15006]}
---
<!-- generated:start -->
<!-- generated-keys: title=02f32f type=86a754 id=fe9e18 sources=ef8400 name_key=ee2fa4 desc_key=15589c kind=356a19 kind_name=9bc378 target=d1cc1b range=77de68 area=27cf35 cost=060055 cooldown=5b7687 effect_kind=da4b92 effects=2fc8f8 damage_or_effect=1126de tooltip_formula=af13a8 visual=17503a icon=a6e82f used_by=12a41f -->
|  |  |
|---|---|
|  | ![Wild Threat](../assets/skills/5056.png) |
| **Skill id** | `5056` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 4, width/angle 0 |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 108 `PCM_Knife_02_W_맹수의 위협` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 21 |

### Tooltip

> [Active] Brandish your blades, inflicting `{EF_STATIC 85}``{EF_R_MDAM 30}` Damage. All enemies that are hit tremble in fear.

Tooltip formula: **85 + 30% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 30 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10052-wild-threat-damage-over-time\|Wild Threat : Damage over time]] | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/10141-wild-threat-in-panic\|Wild Threat : In Panic]] | 100 |

**Reading:** amount **85 + 30% Ability Power**; damage (magic?); applies [[wiki/buffs/10052-wild-threat-damage-over-time|Wild Threat : Damage over time]] (100%); applies [[wiki/buffs/10141-wild-threat-in-panic|Wild Threat : In Panic]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 28: [[wiki/items/15006-magical-blood-dagger|Magical Blood Dagger]]
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
