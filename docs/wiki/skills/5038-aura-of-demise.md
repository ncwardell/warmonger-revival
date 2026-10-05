---
title: "Aura of Demise"
type: "skill"
id: 5038
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5038", "client: StringAll_Eng SkillComment_5038 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 Character creation, 1:50 (cooldown, mana and effect text at level 1; match client)", "video: [[gameplay/video-tutorial-walkthrough]] step 1, 1:38 (Guardian skill preview)"]
name_key: "Skill_5038"
desc_key: "SkillComment_5038"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 180}
cooldown: {"ms": 28000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10035, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10035, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 45}
  - {"tag": "EF_R_MDAM", "value": 50}
visual: 205
icon: {"file": "Skill_Dolorece_01.png", "index": 5}
used_by:
  - {"weapon_base": 43, "slot": 2, "items": [20001]}
---
<!-- generated:start -->
<!-- generated-keys: title=c55ca4 type=86a754 id=fecbfc sources=8c40d0 name_key=8d73fd desc_key=0727d3 kind=356a19 kind_name=9bc378 target=31fde0 range=356a19 cost=fe884b cooldown=5e50e2 effect_kind=da4b92 effects=759f8d damage_or_effect=23e45e tooltip_formula=122dd9 visual=5f1cd7 icon=f51da1 used_by=5b5072 -->
|  |  |
|---|---|
|  | ![Aura of Demise](wiki/assets/skills/5038.png) |
| **Skill id** | `5038` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 12 |
| **Range** | 1 (world units) |
| **Cost** | 180 MP |
| **Cooldown** | 28 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 205 `PCD_Hammer_02_W_귀화 시전` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 5 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 45}``{EF_R_MDAM 50}` damage to all enemies close to you for 10 seconds. Aura of Demise damages for an additional 1% of your maximum health per second.

Tooltip formula: **45 + 50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10035-aura-of-demise-damages-enemies-around-you\|Aura of Demise : Damages enemies around you]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10035-aura-of-demise-damages-enemies-around-you|Aura of Demise : Damages enemies around you]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 43: [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 45): Aura of Demise · 28 s · 180 · 45 (+0) damage to nearby enemies over 10 s, plus 1 % of own max HP per second
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
<!-- generated:end -->

## Notes

- Shown on the character-creation screen of the June 2018 relaunch as the W skill of the starting Guardian weapon Magical Demolition Hammer (item 20001), at level 1: 28 s cooldown, 180 mana, "45 (+0) damage to nearby enemies over 10 s, plus 1 % of own max HP per second" ([[gameplay/video-character-creation-and-tutorial]] §1, [1:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=110s)). Cooldown and mana cost match the client. *video*
- The Arslan tutorial video shows the same Guardian preview (Q Soul Infestation, W Aura of Demise, E Severe Blow, R Dark Transformation) ([[gameplay/video-tutorial-walkthrough]] step 1, [1:38](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=98s)). *video*
- The "1 % of own max HP per second" part is also in the client tooltip text, but not in its value tags or effect slots. *client*

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
