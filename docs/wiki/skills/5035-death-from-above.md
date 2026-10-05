---
title: "Death from Above"
type: "skill"
id: 5035
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 5035", "client: StringAll_Eng SkillComment_5035 (tooltip value tags)"]
name_key: "Skill_5035"
desc_key: "SkillComment_5035"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 4, "field_tick": 1.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 400, "rate": 100}
damage_or_effect: {}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 50}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 186
icon: {"file": "Skill_Miriam_01.png", "index": 3}
used_by:
  - {"weapon_base": 22, "slot": 4, "items": [15000]}
---
<!-- generated:start -->
<!-- generated-keys: title=cf5397 type=86a754 id=290ae5 sources=d083b8 name_key=8604e9 desc_key=bab51f kind=356a19 kind_name=9bc378 target=cacd0a range=b1d578 area=6d01a6 cost=ff5a60 cooldown=ad2ac8 delivery=15a656 effect_kind=356a19 effects=689259 damage_or_effect=bf21a9 tooltip_formula=cee90f visual=87d538 icon=50dbdf used_by=efee56 -->
|  |  |
|---|---|
|  | ![Death from Above](../assets/skills/5035.png) |
| **Skill id** | `5035` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX (4), tick 1 |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 186 `PCM_Bow_01_R_죽음의 손아귀` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 3 |

### Tooltip

> [Active] Fire a volley of arrows, inflicting `{EF_STATIC 50}``{EF_R_DAM 80}` Damage per second. Causes enemies still inside the area to tremble with fear.

Tooltip formula: **50 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 400 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 22: [[wiki/items/15000-magical-shadow-bow|Magical Shadow Bow]]

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 96): Client check: Skill_Base cooldowns are Soul Infestation 19 s (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail o...
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
