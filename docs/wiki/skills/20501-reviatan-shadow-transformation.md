---
title: "Reviatan Shadow Transformation"
type: "skill"
id: 20501
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20501", "guide: [[gameplay/classes-and-legions]] §1 (hero usable only at level 30)", "notes: [[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes (WM 0621 cooldown 10 → 120 s, 0402 durability, 0628 gear share, 1107 Innocence Crystal)"]
name_key: "Skill_20501"
desc_key: "SkillComment_20501"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20501, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20501, "rate": 100}]}
visual: 442
icon: {"file": "Items_20.png", "index": 31}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=e3ae77 type=86a754 id=10387f sources=db3142 name_key=3e6d58 desc_key=d42120 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=4aa5a5 effect_kind=da4b92 effects=652f85 damage_or_effect=6b1179 visual=e076fa icon=e5f8ba used_by=97d170 -->
|  |  |
|---|---|
|  | ![Reviatan Shadow Transformation](wiki/assets/skills/20501.png) |
| **Skill id** | `20501` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 442 `아르타모스_변신` |
| **Icon** | `ui/icons/Items_20.png` cell 31 |

### Tooltip

> [Active] Reviatan Shadow Transformation transformed.
> It consumes experience when transforming

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20501\|Buff 20501]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20501|Buff 20501]] (100%).
<!-- generated:end -->

## Notes

- Hero transformation (key X). Heroes are unlocked from gacha hero pieces and usable only at the max level 30 ([[gameplay/classes-and-legions]] §1, guides). *guide*
- Patch history: transformation cooldown 10 → **120 s** ([WM 0621](https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204)); hero durability 24 → 240 ([WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018)); a hero gets a share of the gear stats, 35 % at T1+0, 45 % at T1+15, 65 % at T2+10, 100 % at T3+15 ([WM 0628](https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838)); Innocence Crystal durability 1,500, −5 per second while transformed, no level limit ([WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)) ([[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §1, §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes.

## Open questions

- Cooldown: WM 0621 set transformation cooldown to 120 s, but this client row still has 10 s (the first seven heroes have 120 s). Client kept; the later heroes may simply have missed the change.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
