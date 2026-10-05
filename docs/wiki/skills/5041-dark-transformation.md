---
title: "Dark Transformation"
type: "skill"
id: 5041
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5041", "video: [[gameplay/video-character-creation-and-tutorial]] §1 Character creation, 1:50 (cooldown, mana and effect text at level 1; match client)", "video: [[gameplay/video-tutorial-walkthrough]] step 1, 1:38 (Guardian skill preview)"]
name_key: "Skill_5041"
desc_key: "SkillComment_5041"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10037, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10038, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10037, "rate": 100}, {"buff": 10038, "rate": 100}]}
visual: 213
icon: {"file": "Skill_Dolorece_01.png", "index": 7}
used_by:
  - {"weapon_base": 43, "slot": 4, "items": [20001]}
---
<!-- generated:start -->
<!-- generated-keys: title=128bcd type=86a754 id=6fcba6 sources=40a70a name_key=9fa9d6 desc_key=21f141 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=9e049c cooldown=7d0c8c effect_kind=da4b92 effects=eaafb8 damage_or_effect=9044dc visual=19187d icon=3af2a9 used_by=8b1e19 -->
|  |  |
|---|---|
|  | ![Dark Transformation](wiki/assets/skills/5041.png) |
| **Skill id** | `5041` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 213 `PCD_Hammer_02_R_독각 대왕` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 7 |

### Tooltip

> [Active] During the state of transformation you gain increased HP Regeneration and Movement Speed for 10 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10037-dark-transformation-gain-40-health-regeneration\|Dark Transformation : Gain 40% Health Regeneration]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10038-dark-transformation-gain-100-movement-speed\|Dark Transformation : Gain 100 Movement Speed]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10037-dark-transformation-gain-40-health-regeneration|Dark Transformation : Gain 40% Health Regeneration]] (100%); applies [[wiki/buffs/10038-dark-transformation-gain-100-movement-speed|Dark Transformation : Gain 100 Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 43: [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 47): Dark Transformation · 60 s · 340 · More HP regeneration and movement speed for 10 s
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
<!-- generated:end -->

## Notes

- Shown on the character-creation screen of the June 2018 relaunch as the R skill of the starting Guardian weapon Magical Demolition Hammer (item 20001), at level 1: 60 s cooldown, 340 mana, "more HP regeneration and movement speed for 10 s" ([[gameplay/video-character-creation-and-tutorial]] §1, [1:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=110s)). Cooldown and mana cost match the client. *video*
- The Arslan tutorial video shows the same Guardian preview (Q Soul Infestation, W Aura of Demise, E Severe Blow, R Dark Transformation) ([[gameplay/video-tutorial-walkthrough]] step 1, [1:38](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=98s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1 (ZonderCoRe, June 2018), [[gameplay/video-tutorial-walkthrough]] step 1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
