---
title: "Essence Wave"
type: "skill"
id: 5286
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5286", "client: StringAll_Eng SkillComment_5286 (tooltip value tags)"]
name_key: "Skill_5286"
desc_key: "SkillComment_5286"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 17
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 18.0, "width_or_angle": 3.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 315}
cooldown: {"ms": 55000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
  - {"slot": 3, "type": 102, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "attack_pct": 90, "ability_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 90}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 371
icon: {"file": "Skill_Miriam_01.png", "index": 11}
used_by:
  - {"weapon_base": 65, "slot": 4, "items": [35002]}
---
<!-- generated:start -->
<!-- generated-keys: title=ebf099 type=86a754 id=929372 sources=4fee0f name_key=d464ee desc_key=adef8a kind=356a19 kind_name=9bc378 target=e84f24 range=0716d9 area=34415f cost=ebaf92 cooldown=8825ab delivery=93a212 effect_kind=da4b92 effects=cb03ad damage_or_effect=3cfc94 tooltip_formula=ed8c8f visual=3554dc icon=5f7b06 used_by=b60abd -->
|  |  |
|---|---|
|  | ![Essence Wave](../assets/skills/5286.png) |
| **Skill id** | `5286` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 17 (world units) |
| **Area** | line / rectangle?, radius 18, width/angle 3 (indicator `stick256x512.png`) |
| **Cost** | 315 MP |
| **Cooldown** | 55 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 371 `시즌1_PCM_Bow_03_R_정조준 일격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 11 |

### Tooltip

> [Active] Shoots a large wave of pure energy, inflicting `{EF_STATIC 120}``{EF_R_DAM 90}``{EF_R_MDAM 80}` Damage to all enemies it passes.

Tooltip formula: **120 + 90% Attack + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |

**Reading:** amount **120 + 90% Attack + 80% Ability Power**; damage (magic?).

### Used by

- Weapon skill **R** of WeaponBase 65: [[wiki/items/35002-magical-vision-bow|Magical Vision Bow]]

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
