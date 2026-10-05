---
title: "Blow of water"
type: "skill"
id: 20158
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20158", "client: StringAll_Eng SkillComment_20158 (tooltip value tags)"]
name_key: "Skill_20158"
desc_key: "SkillComment_20158"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 20156, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20156, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 427
icon: {"file": "Skill_Boss_01.dds", "index": 28}
used_by:
  - {"weapon_base": 72, "slot": 6, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=94c3d3 type=86a754 id=f16bc1 sources=89c70d name_key=c43d48 desc_key=ec28b5 kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 cost=58a4ca cooldown=133145 effect_kind=356a19 effects=663fe9 damage_or_effect=fdaf06 tooltip_formula=5aa272 visual=fba7b6 icon=e4f418 used_by=dace8f -->
|  |  |
|---|---|
|  | ![Blow of water](../assets/skills/20158.png) |
| **Skill id** | `20158` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 427 `사라스바티_물의 강타` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 28 |

### Tooltip

> [Active]During a basic attack, it deals damage to nearby enemies for 6 seconds, in addition to the base damage, as much as `{EF_STATIC 60}``{EF_R_DAM 70}`.

Tooltip formula: **60 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20156-blow-of-water-your-basic-attacks-deal-additional-damage\|Blow of water : Your basic Attacks deal additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20156-blow-of-water-your-basic-attacks-deal-additional-damage|Blow of water : Your basic Attacks deal additional damage]] (100%).

### Used by

- Weapon skill **hero set 2** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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
