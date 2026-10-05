---
title: "Wild Launch"
type: "skill"
id: 5138
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5138", "client: StringAll_Eng SkillComment_5138 (tooltip value tags)"]
name_key: "Skill_5138"
desc_key: "SkillComment_5138"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 18
area: {"shape": 1, "shape_name": "circle", "radius": 2.0, "width_or_angle": 0.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 5137}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 100, "attack_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_DAM", "value": 80}
requirements:
  - {"type": 10161, "a": 1, "b": 1}
visual: 285
icon: {"file": "Skill_Dolorece_01.png", "index": 32}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=0bc1de type=86a754 id=bc9b51 sources=d20d72 name_key=7932da desc_key=60f983 kind=356a19 kind_name=9bc378 target=7056fd range=9e6a55 area=711599 cost=7e5cd4 cooldown=38a66e delivery=93a212 effect_kind=356a19 effects=537c72 damage_or_effect=750cb8 tooltip_formula=b3aee4 requirements=71de73 visual=367ac6 icon=4eabfa used_by=97d170 -->
|  |  |
|---|---|
|  | ![Wild Launch](wiki/assets/skills/5138.png) |
| **Skill id** | `5138` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 18 (world units) |
| **Area** | circle, radius 2, width/angle 0 (indicator `stick256x512.png`) |
| **Cost** | 50 MP |
| **Cooldown** | 2 s (group 5137) |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 285 `PCD_Cannon_05_R_무차별 발사2` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 32 |

### Tooltip

> [Active] Launch a missile that deals `{EF_STATIC 100}``{EF_R_DAM 80}` Damage. Every third missile deals considerably more Damage. Missiles are stored over time up to a maximum of 7.

Tooltip formula: **100 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |

**Reading:** amount **100 + 80% Attack**; damage (physical?).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10161 | 1 | 1 |
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
