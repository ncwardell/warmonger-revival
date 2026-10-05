---
title: "Crushing Blow"
type: "skill"
id: 5067
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5067", "client: StringAll_Eng SkillComment_5067 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5067"
desc_key: "SkillComment_5067"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10058, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 80, "buffs": [{"buff": 10058, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 72
icon: {"file": "Skill_Dolorece_01.png", "index": 12}
used_by:
  - {"weapon_base": 45, "slot": 1, "items": [20003]}
---
<!-- generated:start -->
<!-- generated-keys: title=8e474c type=86a754 id=06dd5b sources=7311c1 name_key=0a93d0 desc_key=ec8f92 kind=356a19 kind_name=9bc378 target=d1cc1b range=77de68 area=344636 cost=f67772 cooldown=c9c532 effect_kind=da4b92 effects=ad72e3 damage_or_effect=1782fc tooltip_formula=e4dbdd visual=c09763 icon=372eb2 used_by=c35a53 -->
|  |  |
|---|---|
|  | ![Crushing Blow](wiki/assets/skills/5067.png) |
| **Skill id** | `5067` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 72 `PCD_Hammer_04_Q_분쇄` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 12 |

### Tooltip

> [Active] Knocks up all enemies around you deals `{EF_STATIC 70}``{EF_R_MDAM 80}` Damage and silences them.

Tooltip formula: **70 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10058-crushing-blow-silenced-for-2-seconds\|Crushing Blow : Silenced for 2 seconds]] | 100 |

**Reading:** amount **70 + 80% Ability Power**; damage (magic?); applies [[wiki/buffs/10058-crushing-blow-silenced-for-2-seconds|Crushing Blow : Silenced for 2 seconds]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 45: [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
<!-- generated:end -->

## Notes

- Skill Q of Magical Crush Hammer (item 20003), one of the Guardian's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

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
