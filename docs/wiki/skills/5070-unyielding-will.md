---
title: "Unyielding Will"
type: "skill"
id: 5070
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5070", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5070"
desc_key: "SkillComment_5070"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10061, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10061, "rate": 100}]}
visual: 75
icon: {"file": "Skill_Dolorece_01.png", "index": 15}
used_by:
  - {"weapon_base": 45, "slot": 4, "items": [20003]}
---
<!-- generated:start -->
<!-- generated-keys: title=066fdc type=86a754 id=a91063 sources=b270f2 name_key=85042c desc_key=4af7ac kind=356a19 kind_name=9bc378 target=d99f6c range=ac3478 cost=ff5a60 cooldown=ad2ac8 effect_kind=b6589f effects=0b49c5 damage_or_effect=a30f8e visual=450dde icon=a431e0 used_by=535fcd -->
|  |  |
|---|---|
|  | ![Unyielding Will](../assets/skills/5070.png) |
| **Skill id** | `5070` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Visual** | skillVisual 75 `PCD_Hammer_04_R_꺽을 수 없는 의지` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 15 |

### Tooltip

> [Active] Reduces Damage of all types by 50% for 5 seconds and gives 40 Attack.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10061-unyielding-will-reduce-50-all-type-of-damage-during-5-second\|Unyielding Will : Reduce 50% all type of damage during 5 seconds and get 40 Attack.]] | 100 |

**Reading:** applies [[wiki/buffs/10061-unyielding-will-reduce-50-all-type-of-damage-during-5-second|Unyielding Will : Reduce 50% all type of damage during 5 seconds and get 40 Attack.]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 45: [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
<!-- generated:end -->

## Notes

- Skill R of Magical Crush Hammer (item 20003), one of the Guardian's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
