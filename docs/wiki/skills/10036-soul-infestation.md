---
title: "Soul Infestation"
type: "skill"
id: 10036
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10036", "client: StringAll_Eng SkillComment_10036 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0124 (names the weapon, not the item id)"]
name_key: "Skill_10036"
desc_key: "SkillComment_10036"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 135}
cooldown: {"ms": 19000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 30034, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 30034, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_MDAM", "value": 65}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 203
icon: {"file": "Skill_Dolorece_01.png", "index": 4}
used_by:
  - {"weapon_base": 143, "slot": 1, "items": [21001]}
---
<!-- generated:start -->
<!-- generated-keys: title=665431 type=86a754 id=9cbdc5 sources=b5185e name_key=70db1a desc_key=a5155d kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 cost=ad8002 cooldown=371007 effect_kind=da4b92 effects=e1bed1 damage_or_effect=265538 tooltip_formula=d1a583 visual=a165fb icon=01c963 used_by=a0633a -->
|  |  |
|---|---|
|  | ![Soul Infestation](../assets/skills/10036.png) |
| **Skill id** | `10036` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 135 MP |
| **Cooldown** | 19 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 203 `PCD_Hammer_02_Q_추타` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 4 |

### Tooltip

> [Active] Your basic attacks deal additional `{EF_STATIC 10}``{EF_R_MDAM 65}``{EF_R_DAM 80}` Damage. You now hit multiple opponents at once.

Tooltip formula: **10 + 65% Ability Power + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30034-soul-infestation-your-basic-attacks-deal-additional-damage\|Soul Infestation : Your basic Attacks deal additional damage]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/30034-soul-infestation-your-basic-attacks-deal-additional-damage|Soul Infestation : Your basic Attacks deal additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 143: [[wiki/items/21001-magical-demolition-hammer|Magical Demolition Hammer]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 106): 0124 · Magical Demolition Hammer · Q Soul Infestation: basic attacks deal 10 + 60% AP + 75% AD magic damage (bonus AD 100% → 75%, AP 30% → 60%), hits several...
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 92): Soul Infestation (Guardian hammer) · turns autoattacks into AoE magic damage while active; 14 s cooldown · player [t774], [t391]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server (line 230): Soul Infestation cooldown · 14 s · 19 s · WM
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 44): Soul Infestation · 19 s · 135 · Basic attacks deal +10 (+0) damage and hit several enemies
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
<!-- generated:end -->

## Notes

- Same-name copy of Soul Infestation (Magical Demolition Hammer item 21001). [WM 0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617) set Soul Infestation to 10 + 60 % AP + 75 % AD magic damage on basic attacks, hitting several targets ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- This copy's client tooltip reads 10 + 65 % AP + 80 % AD, not the 60 % / 75 % of the WM 0124 note (which matches skill 5036). Which item the note meant, and whether 21001 is a higher-tier copy, is not stated.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
