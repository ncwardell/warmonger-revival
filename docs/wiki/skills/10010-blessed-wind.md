---
title: "Blessed Wind"
type: "skill"
id: 10010
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10010", "client: StringAll_Eng SkillComment_10010 (tooltip value tags)"]
name_key: "Skill_10010"
desc_key: "SkillComment_10010"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 95}
cooldown: {"ms": 11000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 317, "value": 30010, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 30010, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_MDAM", "value": 40}
visual: 87
icon: {"file": "Skill_Einsel_01.png", "index": 2}
used_by:
  - {"weapon_base": 101, "slot": 3, "items": [11000]}
---
<!-- generated:start -->
<!-- generated-keys: title=4209a6 type=86a754 id=b66ddc sources=d6bf33 name_key=8e284f desc_key=6dbedb kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=f9e152 cooldown=5d3cc6 effect_kind=da4b92 effects=9a7fe0 damage_or_effect=9cdfda tooltip_formula=3c6081 visual=e62d7f icon=1fd7a3 used_by=71768e -->
|  |  |
|---|---|
|  | ![Blessed Wind](../assets/skills/10010.png) |
| **Skill id** | `10010` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 95 MP |
| **Cooldown** | 11 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 87 `PCE_Staff_01_E_축복의 바람` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 2 |

### Tooltip

> [Active] Conjures a helpful wind spirit that shields yourself and your allies from incoming Damage. 200`{EF_R_MDAM 40}`

Tooltip formula: **40% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/30010-blessed-wind-creates-a-shield-that-absorbs-damage-for-10-sec\|Blessed Wind: Creates a shield that absorbs Damage for 10 seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/30010-blessed-wind-creates-a-shield-that-absorbs-damage-for-10-sec|Blessed Wind: Creates a shield that absorbs Damage for 10 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 101: [[wiki/items/11000-magical-storm-wand|Magical Storm Wand]]
- Nation policy 11 `PolicyName_11` (Policy.cdb, server-only; buff_or_skill)
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
