---
title: "Mother Nature's Blessing"
type: "skill"
id: 5277
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5277", "client: StringAll_Eng SkillComment_5277 (tooltip value tags)"]
name_key: "Skill_5277"
desc_key: "SkillComment_5277"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 80}
cooldown: {"ms": 8000, "group": 1}
effect_kind: 0
effects:
  - {"slot": 1, "type": 317, "value": 10336, "rate": 100}
  - {"slot": 2, "type": 314, "value": 10337, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10336, "rate": 100}, {"buff": 10337, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 100}
visual: 362
icon: {"file": "Skill_Einsel_01.png", "index": 8}
used_by:
  - {"weapon_base": 64, "slot": 1, "items": [10002]}
---
<!-- generated:start -->
<!-- generated-keys: title=2b3f75 type=86a754 id=68077b sources=ea0a17 name_key=90c0db desc_key=7edfed kind=356a19 kind_name=9bc378 target=644925 range=c1dfd9 cost=e01d1d cooldown=0fb417 effect_kind=b6589f effects=61e228 damage_or_effect=e58f3b tooltip_formula=015e59 visual=8d6f91 icon=1aeac2 used_by=6d692e -->
|  |  |
|---|---|
|  | ![Mother Nature's Blessing](wiki/assets/skills/5277.png) |
| **Skill id** | `5277` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Cost** | 80 MP |
| **Cooldown** | 8 s (group 1) |
| **Visual** | skillVisual 362 `시즌1_PCE_Staff_03_Q_대자연의 가호` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 8 |

### Tooltip

> [Active] Absorb 100 (+ Ability Power 20%) Damage over 4 seconds for you and your allies, and deal `{EF_STATIC 70}``{EF_R_MDAM 100}` Damage to the enemy. When the barrier disappears, Armor and MR will increase 5% over 4 seconds.

Tooltip formula: **70 + 100% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/10336-blessing-of-mother-nature-absorbs-damage\|blessing of Mother Nature : Absorbs damage]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/10337-blessing-of-mother-nature-explosion\|blessing of Mother Nature : Explosion]] | 100 |

**Reading:** applies [[wiki/buffs/10336-blessing-of-mother-nature-absorbs-damage|blessing of Mother Nature : Absorbs damage]] (100%); applies [[wiki/buffs/10337-blessing-of-mother-nature-explosion|blessing of Mother Nature : Explosion]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 64: [[wiki/items/10002-magical-life-wand|Magical Life Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/10002-magical-life-wand|Magical Life Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 38): Saint · 10017 Magical Wrath Blade (Flying Blade) · 10011 Magical adapted Dual Gun (Dual Gun) · 10001 Magical Thunder Wand (Wand) · 10002 Magical Life Wand (n...
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
