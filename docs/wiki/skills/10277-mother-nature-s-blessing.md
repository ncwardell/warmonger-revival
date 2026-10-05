---
title: "Mother Nature's Blessing"
type: "skill"
id: 10277
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10277", "client: StringAll_Eng SkillComment_10277 (tooltip value tags)"]
name_key: "Skill_10277"
desc_key: "SkillComment_10277"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 80}
cooldown: {"ms": 8000, "group": 1}
effect_kind: 0
effects:
  - {"slot": 1, "type": 317, "value": 30336, "rate": 100}
  - {"slot": 2, "type": 314, "value": 30337, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30336, "rate": 100}, {"buff": 30337, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 105}
visual: 362
icon: {"file": "Skill_Einsel_01.png", "index": 8}
used_by:
  - {"weapon_base": 164, "slot": 1, "items": [11002]}
---
<!-- generated:start -->
<!-- generated-keys: title=2b3f75 type=86a754 id=a7f6c0 sources=3210bb name_key=dc9423 desc_key=c74054 kind=356a19 kind_name=9bc378 target=644925 range=c1dfd9 cost=e01d1d cooldown=0fb417 effect_kind=b6589f effects=4f188d damage_or_effect=1f5d9c tooltip_formula=d3c4f1 visual=8d6f91 icon=1aeac2 used_by=c6dfe9 -->
|  |  |
|---|---|
|  | ![Mother Nature's Blessing](../assets/skills/10277.png) |
| **Skill id** | `10277` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Cost** | 80 MP |
| **Cooldown** | 8 s (group 1) |
| **Visual** | skillVisual 362 `시즌1_PCE_Staff_03_Q_대자연의 가호` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 8 |

### Tooltip

> [Active] Absorb 100 (+ Ability Power 20%) Damage over 4 seconds for you and your allies, and deal `{EF_STATIC 70}``{EF_R_MDAM 105}` Damage to the enemy. When the barrier disappears, Armor and MR will increase 5% over 4 seconds.

Tooltip formula: **70 + 105% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/30336-blessing-of-mother-nature-absorbs-damage\|blessing of Mother Nature : Absorbs damage]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/30337-blessing-of-mother-nature-explosion\|blessing of Mother Nature : Explosion]] | 100 |

**Reading:** applies [[wiki/buffs/30336-blessing-of-mother-nature-absorbs-damage|blessing of Mother Nature : Absorbs damage]] (100%); applies [[wiki/buffs/30337-blessing-of-mother-nature-explosion|blessing of Mother Nature : Explosion]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 164: [[wiki/items/11002-magical-life-wand|Magical Life Wand]]

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
