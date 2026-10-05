---
title: "Vision explosion"
type: "skill"
id: 5492
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5492", "client: StringAll_Eng SkillComment_5492 (tooltip value tags)", "gameplay: [[gameplay/classes-and-legions]]"]
name_key: "Skill_5492"
desc_key: "SkillComment_5492"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 95}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
  - {"slot": 3, "type": 102, "value": 70, "rate": 0}
  - {"slot": 4, "type": 362, "value": 1, "rate": 20}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 85, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 70}
requirements:
  - {"type": 10442, "a": 6, "b": 0}
visual: 482
icon: {"file": "Skill_Miriam_01.png", "index": 35}
used_by:
  - {"weapon_base": 86, "slot": 2, "items": [15005]}
observed:
  - {"cooldown_s": 17, "mana": 95, "effect": "85 + 0.83 AD + 0.6875 AP around you, plus more per Vision stack used (stacks from basic attacks, max 10, last 7 s)", "source": "gameplay/classes-and-legions line 113"}
---
<!-- generated:start -->
<!-- generated-keys: title=45db83 type=86a754 id=1409f5 sources=53fce8 name_key=eec96e desc_key=8bef0b kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=e8b0ea cost=f9e152 cooldown=c9c532 effect_kind=356a19 effects=1fd037 damage_or_effect=ca2dd2 tooltip_formula=1aeae1 requirements=9fd74a visual=d051bf icon=8527d3 used_by=cdbebe observed=8a6610 -->
|  |  |
|---|---|
|  | ![Vision explosion](wiki/assets/skills/5492.png) |
| **Skill id** | `5492` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 95 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 482 `해골왕의 비젼 활_비전 폭발` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 35 |

### Tooltip

> [Active]Use up all the stacks and cause as much damage as `{EF_STATIC 85}``{EF_R_DAM 85}``{EF_R_MDAM 70}`. Depending on the number of stacks, add additional damage. 
> The stack is increased on the base attack and up to 10 stacks are created. Stack hold time is 7 seconds.

Tooltip formula: **85 + 85% Attack + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 4 | 362 | unknown | 1 | 20 |

**Reading:** amount **85 + 85% Attack + 70% Ability Power**; damage (physical?).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10442 | 6 | 0 |

### Used by

- Weapon skill **W** of WeaponBase 86: [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]]

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 17 | 95 |  | 85 + 0.83 AD + 0.6875 AP around you, plus more per Vision stack used (stacks from basic attacks, max 10, last 7 s) | [[gameplay/classes-and-legions]] line 113 |

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 113): W · Vision Explosion · 17 s · 95 · 85 + 0.83 AD + 0.6875 AP around you, plus more per Vision stack used (stacks from basic attacks, max 10, last 7 s)
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
