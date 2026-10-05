---
title: "Advent"
type: "skill"
id: 5199
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5199", "client: StringAll_Eng SkillComment_5199 (tooltip value tags)"]
name_key: "Skill_5199"
desc_key: "SkillComment_5199"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 6}
range: 9
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: {"type": 4, "type_name": "HP %", "amount": 3}
cooldown: {"ms": 15000, "group": 0}
cast_ms: 500
movement: "dash"
delivery: {"type": 5, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10242, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 80, "buffs": [{"buff": 10242, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 324
icon: {"file": "Skill_Boss_01.dds", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=04a6fb type=86a754 id=6553d0 sources=470d01 name_key=1324b2 desc_key=ce87ae kind=356a19 kind_name=9bc378 target=6850f9 range=0ade7c area=344636 cost=e65f66 cooldown=e3989d cast_ms=f83a38 movement=5f1488 delivery=dfe77c effect_kind=356a19 effects=90ade6 damage_or_effect=57b005 tooltip_formula=4d3643 visual=914127 icon=43a46d used_by=97d170 -->
|  |  |
|---|---|
|  | ![Advent](wiki/assets/skills/5199.png) |
| **Skill id** | `5199` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 6 |
| **Range** | 9 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Cost** | 3 HP % |
| **Cooldown** | 15 s |
| **Cast time** | 0.5 s |
| **Movement** | dash |
| **Delivery** | ground field (ticks) |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 324 `수호신장_변신스킬_01_강림` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 0 |

### Tooltip

> [Active] A body shot that inflicts `{EF_STATIC 70}``{EF_R_DAM 80}` Damage. Knocks up all enemies around your target.

Tooltip formula: **70 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10242-advent-silenced-for-2-seconds\|Advent : Silenced for 2 seconds.]] | 100 |

**Reading:** amount **70 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10242-advent-silenced-for-2-seconds|Advent : Silenced for 2 seconds.]] (100%).
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
