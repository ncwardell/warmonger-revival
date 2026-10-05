---
title: "Aura of Demise"
type: "skill"
id: 10038
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10038", "client: StringAll_Eng SkillComment_10038 (tooltip value tags)"]
name_key: "Skill_10038"
desc_key: "SkillComment_10038"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 180}
cooldown: {"ms": 28000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 30035, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 30035, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 45}
  - {"tag": "EF_R_MDAM", "value": 55}
visual: 205
icon: {"file": "Skill_Dolorece_01.png", "index": 5}
used_by:
  - {"weapon_base": 143, "slot": 2, "items": [21001]}
---
<!-- generated:start -->
<!-- generated-keys: title=c55ca4 type=86a754 id=2c384a sources=7d6119 name_key=e91e7f desc_key=171e7c kind=356a19 kind_name=9bc378 target=31fde0 range=356a19 cost=fe884b cooldown=5e50e2 effect_kind=da4b92 effects=14f5d1 damage_or_effect=481276 tooltip_formula=090a3f visual=5f1cd7 icon=f51da1 used_by=30eb08 -->
|  |  |
|---|---|
|  | ![Aura of Demise](../assets/skills/10038.png) |
| **Skill id** | `10038` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 12 |
| **Range** | 1 (world units) |
| **Cost** | 180 MP |
| **Cooldown** | 28 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 205 `PCD_Hammer_02_W_귀화 시전` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 5 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 45}``{EF_R_MDAM 55}` damage to all enemies close to you for 10 seconds. Aura of Demise damages for an additional 1% of your maximum health per second.

Tooltip formula: **45 + 55% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30035-aura-of-demise-damages-enemies-around-you\|Aura of Demise : Damages enemies around you]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/30035-aura-of-demise-damages-enemies-around-you|Aura of Demise : Damages enemies around you]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 143: [[wiki/items/21001-magical-demolition-hammer|Magical Demolition Hammer]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 45): Aura of Demise · 28 s · 180 · 45 (+0) damage to nearby enemies over 10 s, plus 1 % of own max HP per second
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
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
