---
title: "Severe Blow"
type: "skill"
id: 10040
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10040", "client: StringAll_Eng SkillComment_10040 (tooltip value tags)"]
name_key: "Skill_10040"
desc_key: "SkillComment_10040"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 35, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30036, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 35, "buffs": [{"buff": 30036, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 35}
visual: 212
icon: {"file": "Skill_Dolorece_01.png", "index": 6}
used_by:
  - {"weapon_base": 143, "slot": 3, "items": [21001]}
---
<!-- generated:start -->
<!-- generated-keys: title=7121e4 type=86a754 id=c92291 sources=7c7dee name_key=2bfa7c desc_key=6f38e2 kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=911ade cooldown=628d31 effect_kind=da4b92 effects=f223e4 damage_or_effect=22189a tooltip_formula=1c26c6 visual=e2154f icon=c391b2 used_by=68101b -->
|  |  |
|---|---|
|  | ![Severe Blow](wiki/assets/skills/10040.png) |
| **Skill id** | `10040` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 212 `PCD_Hammer_02_E_ 삼릉창` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 6 |

### Tooltip

> [Active] Deals `{EF_STATIC 70}``{EF_R_MDAM 35}` Damage knocking the enemy up in the air.

Tooltip formula: **70 + 35% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 35 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30036-shadow-walk-silences-for-2-seconds\|Shadow Walk: Silences for 2 seconds]] | 100 |

**Reading:** amount **70 + 35% Ability Power**; damage (magic?); applies [[wiki/buffs/30036-shadow-walk-silences-for-2-seconds|Shadow Walk: Silences for 2 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 143: [[wiki/items/21001-magical-demolition-hammer|Magical Demolition Hammer]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 46): Severe Blow · 20 s · 140 · 70 (+0) damage and knock-up
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
