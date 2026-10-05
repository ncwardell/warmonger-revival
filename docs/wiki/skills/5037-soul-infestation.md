---
title: "Soul Infestation"
type: "skill"
id: 5037
status: "partial"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5037", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0124 (Soul Infestation basic-attack damage; link to 5037 via buff 10034 is inferred)"]
name_key: "Skill_5037"
desc_key: "SkillComment_5037"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: null
cooldown: {"ms": 1000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 102, "value": 60, "rate": 0}
  - {"slot": 3, "type": 101, "value": 75, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 10, "ability_pct": 60, "attack_pct": 75}
weapon_type: 6
visual: 204
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=665431 type=86a754 id=a71fd9 sources=2d9d0c name_key=3f6699 desc_key=c2c2de kind=ac3478 kind_name=65782b target=04e8ed range=77de68 area=500aa4 cost=2be88c cooldown=4a6a0b effect_kind=da4b92 effects=3507e2 damage_or_effect=910d0e weapon_type=c1dfd9 visual=1cc641 icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `5037` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Cooldown** | 1 s |
| **Effect kind** | damage (magic?) (2) |
| **Needs weapon type** | 6 |
| **Visual** | skillVisual 204 `PCD_Hammer_02_Q_추타 피격` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 60 | 0 |
| 3 | 101 | % of Attack (tooltip `EF_R_DAM`) | 75 | 0 |

**Reading:** amount **10 + 75% Attack + 60% Ability Power**; damage (magic?).

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 106): 0124 · Magical Demolition Hammer · Q Soul Infestation: basic attacks deal 10 + 60% AP + 75% AD magic damage (bonus AD 100% → 75%, AP 30% → 60%), hits several...
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 92): Soul Infestation (Guardian hammer) · turns autoattacks into AoE magic damage while active; 14 s cooldown · player [t774], [t391]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server (line 230): Soul Infestation cooldown · 14 s · 19 s · WM
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 44): Soul Infestation · 19 s · 135 · Basic attacks deal +10 (+0) damage and hit several enemies
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
<!-- generated:end -->

## Notes

- The basic attack that [[wiki/skills/5036-soul-infestation|Soul Infestation]] swaps in through buff 10034 (*client*). [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) describes it: basic attacks deal 10 + 60 % AP + 75 % AD magic damage and hit several targets ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
