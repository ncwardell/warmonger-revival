---
title: "Severe Blow"
type: "skill"
id: 5040
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5040", "client: StringAll_Eng SkillComment_5040 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 Character creation, 1:50 (cooldown, mana and effect text at level 1; match client)", "video: [[gameplay/video-tutorial-walkthrough]] step 1, 1:38 (Guardian skill preview)"]
name_key: "Skill_5040"
desc_key: "SkillComment_5040"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 30, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10036, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 30, "buffs": [{"buff": 10036, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 30}
visual: 212
icon: {"file": "Skill_Dolorece_01.png", "index": 6}
used_by:
  - {"weapon_base": 43, "slot": 3, "items": [20001]}
---
<!-- generated:start -->
<!-- generated-keys: title=7121e4 type=86a754 id=4afe98 sources=47a312 name_key=97400f desc_key=2a19bf kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=911ade cooldown=628d31 effect_kind=da4b92 effects=4aad31 damage_or_effect=2edaa5 tooltip_formula=3d3959 visual=e2154f icon=c391b2 used_by=888416 -->
|  |  |
|---|---|
|  | ![Severe Blow](../assets/skills/5040.png) |
| **Skill id** | `5040` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 212 `PCD_Hammer_02_E_ 삼릉창` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 6 |

### Tooltip

> [Active] Deals `{EF_STATIC 70}``{EF_R_MDAM 30}` Damage knocking the enemy up in the air.

Tooltip formula: **70 + 30% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 30 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10036-shadow-walk-silences-for-2-seconds\|Shadow Walk: Silences for 2 seconds]] | 100 |

**Reading:** amount **70 + 30% Ability Power**; damage (magic?); applies [[wiki/buffs/10036-shadow-walk-silences-for-2-seconds|Shadow Walk: Silences for 2 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 43: [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/20001-magical-demolition-hammer|Magical Demolition Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 46): Severe Blow · 20 s · 140 · 70 (+0) damage and knock-up
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
<!-- generated:end -->

## Notes

- Shown on the character-creation screen of the June 2018 relaunch as the E skill of the starting Guardian weapon Magical Demolition Hammer (item 20001), at level 1: 20 s cooldown, 140 mana, "70 (+0) damage and knock-up" ([[gameplay/video-character-creation-and-tutorial]] §1, [1:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=110s)). Cooldown and mana cost match the client. *video*
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
