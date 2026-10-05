---
title: "Essence Wave"
type: "skill"
id: 10066
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10066", "client: StringAll_Eng SkillComment_10066 (tooltip value tags)"]
name_key: "Skill_10066"
desc_key: "SkillComment_10066"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 17
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 18.0, "width_or_angle": 3.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 315}
cooldown: {"ms": 55000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
  - {"slot": 3, "type": 102, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 95, "ability_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 95}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 78
icon: {"file": "Skill_Miriam_01.png", "index": 11}
used_by:
  - {"weapon_base": 124, "slot": 4, "items": [16002]}
---
<!-- generated:start -->
<!-- generated-keys: title=ebf099 type=86a754 id=f44072 sources=1a60a1 name_key=715588 desc_key=e3ada4 kind=356a19 kind_name=9bc378 target=e84f24 range=0716d9 area=34415f cost=ebaf92 cooldown=8825ab delivery=93a212 effect_kind=356a19 effects=2719ea damage_or_effect=fe6745 tooltip_formula=05d6db visual=eb4ac3 icon=5f7b06 used_by=9b9e06 -->
|  |  |
|---|---|
|  | ![Essence Wave](../assets/skills/10066.png) |
| **Skill id** | `10066` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 17 (world units) |
| **Area** | line / rectangle?, radius 18, width/angle 3 (indicator `stick256x512.png`) |
| **Cost** | 315 MP |
| **Cooldown** | 55 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 78 `PCM_Bow_03_R_정조준 일격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 11 |

### Tooltip

> [Active] Shoots a large wave of pure energy, inflicting `{EF_STATIC 120}``{EF_R_DAM 95}``{EF_R_MDAM 85}` Damage to all enemies it passes.

Tooltip formula: **120 + 95% Attack + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |

**Reading:** amount **120 + 95% Attack + 85% Ability Power**; damage (physical?).

### Used by

- Weapon skill **R** of WeaponBase 124: [[wiki/items/16002-magical-vision-bow|Magical Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 115): R · Essence Wave · 55 s · 330 · 120 + 1.0 AD + 0.875 AP to all hit; +1 Vision stack per enemy hit
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
