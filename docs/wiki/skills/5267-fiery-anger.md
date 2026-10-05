---
title: "Fiery Anger"
type: "skill"
id: 5267
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5267", "client: StringAll_Eng SkillComment_5267 (tooltip value tags)"]
name_key: "Skill_5267"
desc_key: "SkillComment_5267"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 305, "value": 10329, "rate": 100}
  - {"slot": 4, "type": 305, "value": 10330, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 70, "buffs": [{"buff": 10329, "rate": 100}, {"buff": 10330, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 387
icon: {"file": "Skill_Einsel_01.png", "index": 36}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=c0a935 type=86a754 id=83c3b6 sources=5e94c1 name_key=9541df desc_key=1954bb kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=060055 cooldown=5b7687 effect_kind=356a19 effects=23080e damage_or_effect=be595e tooltip_formula=9ce175 visual=f7e191 icon=574aef used_by=97d170 -->
|  |  |
|---|---|
|  | ![Fiery Anger](../assets/skills/5267.png) |
| **Skill id** | `5267` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 387 `PCE_SwordShd_01_Q_불의 진노_폭발` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 36 |

### Tooltip

> [Active] Second use: Shield and additional Movement Speed will be removed, deals`{EF_STATIC 85}``{EF_R_DAM 70}` Damage to the enemy.

Tooltip formula: **85 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 305 | applies buff (variant 305) | [[wiki/buffs/10329-anger-of-fire-movement-70-4secs\|Anger of fire : Movement +70 (4Secs)]] | 100 |
| 4 | 305 | applies buff (variant 305) | [[wiki/buffs/10330-anger-of-fire-creates-a-absorvs-damage-for-10-seconds\|Anger of fire : Creates a absorvs damage for 10 seconds]] | 100 |

**Reading:** amount **85 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10329-anger-of-fire-movement-70-4secs|Anger of fire : Movement +70 (4Secs)]] (100%); applies [[wiki/buffs/10330-anger-of-fire-creates-a-absorvs-damage-for-10-seconds|Anger of fire : Creates a absorvs damage for 10 seconds]] (100%).
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
