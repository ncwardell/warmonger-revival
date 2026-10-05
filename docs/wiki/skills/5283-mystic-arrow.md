---
title: "Mystic Arrow"
type: "skill"
id: 5283
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5283", "client: StringAll_Eng SkillComment_5283 (tooltip value tags)"]
name_key: "Skill_5283"
desc_key: "SkillComment_5283"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 102, "value": 80, "rate": 0}
  - {"slot": 4, "type": 307, "value": 10340, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "attack_pct": 80, "ability_pct": 80, "buffs": [{"buff": 10340, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
requirements:
  - {"type": 10340, "a": 1, "b": 1}
visual: 368
icon: {"file": "Skill_Miriam_01.png", "index": 8}
used_by:
  - {"weapon_base": 65, "slot": 1, "items": [35002]}
---
<!-- generated:start -->
<!-- generated-keys: title=c57537 type=86a754 id=dd85d4 sources=d80760 name_key=e03027 desc_key=a05f17 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=7e5cd4 cooldown=367d78 delivery=93a212 effect_kind=da4b92 effects=1b0942 damage_or_effect=dacedd tooltip_formula=55d45d requirements=095aef visual=9aaa0b icon=a11afc used_by=80f182 -->
|  |  |
|---|---|
|  | ![Mystic Arrow](wiki/assets/skills/5283.png) |
| **Skill id** | `5283` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 368 `시즌1_PCM_Bow_03_Q_신비한 화살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 8 |

### Tooltip

> [Active] Shoots an energy arrow that deals `{EF_STATIC 80}``{EF_R_DAM 80}``{EF_R_MDAM 80}` Damage. A max of 2 Points can be stacked over 5 seconds.

Tooltip formula: **80 + 80% Attack + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 4 | 307 | applies buff (variant 307) | [[wiki/buffs/10340-mystic-arrow-rockets-in-store\|Mystic Arrow : Rockets in store]] | 100 |

**Reading:** amount **80 + 80% Attack + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10340-mystic-arrow-rockets-in-store|Mystic Arrow : Rockets in store]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10340 | 1 | 1 |

### Used by

- Weapon skill **Q** of WeaponBase 65: [[wiki/items/35002-magical-vision-bow|Magical Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 112): Q · Mystic Arrow · 5 s · 75 · 85 + 0.8 AD + 0.625 AP; on hit, attack speed up for 6 s
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
