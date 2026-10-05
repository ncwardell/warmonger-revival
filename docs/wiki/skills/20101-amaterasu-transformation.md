---
title: "Amaterasu Transformation"
type: "skill"
id: 20101
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20101", "guide: [[gameplay/classes-and-legions]] §1 (hero usable only at level 30)", "notes: [[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes (WM 0621 cooldown 10 → 120 s, 0402 durability, 0628 gear share, 1107 Innocence Crystal)"]
name_key: "Skill_20101"
desc_key: "SkillComment_20101"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20101, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20101, "rate": 100}]}
visual: 440
icon: {"file": "Items_20.png", "index": 29}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=481724 type=86a754 id=007e0d sources=b3c371 name_key=0c45c8 desc_key=63e91a kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=a7242f effect_kind=da4b92 effects=53ced5 damage_or_effect=2d120b visual=6d0e10 icon=ab7449 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Amaterasu Transformation](wiki/assets/skills/20101.png) |
| **Skill id** | `20101` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 440 `아마테라스 변신` |
| **Icon** | `ui/icons/Items_20.png` cell 29 |

### Tooltip

> [Active] Amaterasu Transformation. 
> Consumes EXP when transforming.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20101-transformation-120-seconds\|Transformation : 120 Seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20101-transformation-120-seconds|Transformation : 120 Seconds]] (100%).
<!-- generated:end -->

## Notes

- Hero transformation (key X). Heroes are unlocked from gacha hero pieces and usable only at the max level 30 ([[gameplay/classes-and-legions]] §1, guides). *guide*
- Patch history: transformation cooldown 10 → **120 s** ([WM 0621](https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204)); hero durability 24 → 240 ([WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018)); a hero gets a share of the gear stats, 35 % at T1+0, 45 % at T1+15, 65 % at T2+10, 100 % at T3+15 ([WM 0628](https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838)); Innocence Crystal durability 1,500, −5 per second while transformed, no level limit ([WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)) ([[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes). *notes*
- Amaterasu hero balance: MP → AP conversion 10 % → 15 % ([WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359)), back to 10 % ([WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397)) ([[gameplay/classes-and-legions]] §5 Heroes). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §1, §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
