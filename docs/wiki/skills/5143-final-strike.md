---
title: "Final Strike"
type: "skill"
id: 5143
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5143", "client: StringAll_Eng SkillComment_5143 (tooltip value tags)"]
name_key: "Skill_5143"
desc_key: "SkillComment_5143"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 590}
cooldown: {"ms": 110000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10166, "rate": 100}
  - {"slot": 4, "type": 302, "value": 10163, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 90, "attack_pct": 80, "buffs": [{"buff": 10166, "rate": 100}, {"buff": 10163, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 287
icon: {"file": "Skill_Miriam_01.png", "index": 28}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=602099 type=86a754 id=77eb85 sources=d97785 name_key=8484c0 desc_key=cffc3f kind=356a19 kind_name=9bc378 target=6ca14a range=ac3478 area=e8b0ea cost=5baaf6 cooldown=e0e4dd effect_kind=356a19 effects=3e6162 damage_or_effect=c29afe tooltip_formula=827f56 visual=f0a4ac icon=70aa6a used_by=97d170 -->
|  |  |
|---|---|
|  | ![Final Strike](../assets/skills/5143.png) |
| **Skill id** | `5143` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 7 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 590 MP |
| **Cooldown** | 110 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 287 `PCM_Knife_05_R_최후의 한 방 : 띄우기` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 28 |

### Tooltip

> [Active] Knocks up all surrounding enemies dealing `{EF_STATIC 90}``{EF_R_DAM 80}` Damage. Removes your absorbing Shield.

Tooltip formula: **90 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10166-final-strikes-silences-for-2-seconds\|Final Strikes: Silences for 2 seconds.]] | 100 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10163-final-strike-creates-a-shield-that-absorbs-damage-for-10-sec\|Final Strike: Creates a shield that absorbs Damage for 10 seconds.]] | 100 |

**Reading:** amount **90 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10166-final-strikes-silences-for-2-seconds|Final Strikes: Silences for 2 seconds.]] (100%); applies [[wiki/buffs/10163-final-strike-creates-a-shield-that-absorbs-damage-for-10-sec|Final Strike: Creates a shield that absorbs Damage for 10 seconds.]] (100%).
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
