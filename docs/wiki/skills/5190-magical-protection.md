---
title: "Magical Protection"
type: "skill"
id: 5190
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5190", "client: StringAll_Eng SkillComment_5190 (tooltip value tags)"]
name_key: "Skill_5190"
desc_key: "SkillComment_5190"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 4, "type_name": "HP %", "amount": 4}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 308, "value": 10230, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10230, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_R_DAM", "value": 10}
visual: 331
icon: {"file": "Skill_Boss_01.dds", "index": 5}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=ce3f49 type=86a754 id=c7300e sources=314043 name_key=9fd77a desc_key=a35547 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=a3f1df cooldown=628d31 effect_kind=b6589f effects=c10111 damage_or_effect=42f60e tooltip_formula=c66bd8 visual=c28097 icon=b3dd37 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Magical Protection](../assets/skills/5190.png) |
| **Skill id** | `5190` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 4 HP % |
| **Cooldown** | 20 s |
| **Visual** | skillVisual 331 `수호신장_변신스킬_06_마력의 보호` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 5 |

### Tooltip

> [Active] Conjure a 300`{EF_R_DAM 10}` protective barrier. When the barrier fades, you gain Armor and Magic Resistance.

Tooltip formula: **10% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 308 | applies buff (variant 308) | [[wiki/buffs/10230-magical-protection-creates-a-absorvs-damage-for-8-seconds\|Magical Protection : Creates a absorvs damage for 8 seconds]] | 100 |

**Reading:** applies [[wiki/buffs/10230-magical-protection-creates-a-absorvs-damage-for-8-seconds|Magical Protection : Creates a absorvs damage for 8 seconds]] (100%).
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
