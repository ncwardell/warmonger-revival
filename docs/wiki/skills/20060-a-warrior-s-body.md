---
title: "A Warrior's Body"
type: "skill"
id: 20060
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20060", "client: StringAll_Eng SkillComment_5196 (tooltip value tags)"]
name_key: "Skill_5196"
desc_key: "SkillComment_5196"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 4, "type_name": "HP %", "amount": 3}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 20061, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 20061, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 50}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 326
icon: {"file": "Skill_Boss_01.dds", "index": 2}
used_by:
  - {"weapon_base": 70, "slot": 3, "items": [8001, 8501]}
---
<!-- generated:start -->
<!-- generated-keys: title=4912df type=86a754 id=103caf sources=be9aed name_key=ee30c5 desc_key=bc3e78 kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 cost=e65f66 cooldown=133145 effect_kind=356a19 effects=2d67ce damage_or_effect=c22ac6 tooltip_formula=66be6c visual=4296ab icon=1a93f3 used_by=d487cc -->
|  |  |
|---|---|
|  | ![A Warrior's Body](../assets/skills/20060.png) |
| **Skill id** | `20060` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 3 HP % |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 326 `수호신장_변신스킬_03_전사의 육체` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 2 |

### Tooltip

> [Active] Basic Attacks deal `{EF_STATIC 50}``{EF_R_DAM 70}` Area Damage.

Tooltip formula: **50 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20061-a-warrior-s-body-deal-additional-damage\|A Warrior's Body. Deal additional damage.]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/20061-a-warrior-s-body-deal-additional-damage|A Warrior's Body. Deal additional damage.]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 70: [[wiki/items/8001-guardian|Guardian]], [[wiki/items/8501-crystal-guardian|Crystal : Guardian]]
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
