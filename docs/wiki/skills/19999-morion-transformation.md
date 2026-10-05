---
title: "Morion Transformation"
type: "skill"
id: 19999
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19999", "guide: [[gameplay/classes-and-legions]] §1 (hero usable only at level 30)", "notes: [[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes (WM 0621 cooldown 10 → 120 s, 0402 durability, 0628 gear share, 1107 Innocence Crystal)"]
name_key: "Skill_19999"
desc_key: "SkillComment_19999"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 20, "type_name": "cost type 20 (unknown)", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 19950, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 19950, "rate": 100}]}
visual: 178
icon: {"file": "Items_20.png", "index": 45}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4e7355 type=86a754 id=7519dd sources=f2c42b name_key=e24b84 desc_key=80d847 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=68d2b6 cooldown=a7242f effect_kind=da4b92 effects=6503a0 damage_or_effect=5e6067 visual=25293f icon=208e98 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Morion Transformation](../assets/skills/19999.png) |
| **Skill id** | `19999` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 cost type 20 (unknown) |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Items_20.png` cell 45 |

### Tooltip

> [Active]Morion Transformation. 
> Consumes durability when transforming.
> When all durability is exhausted, the item is destroyed.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/19950-transformation-120-seconds\|Transformation : 120 Seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/19950-transformation-120-seconds|Transformation : 120 Seconds]] (100%).
<!-- generated:end -->

## Notes

- Hero transformation (key X). Heroes are unlocked from gacha hero pieces and usable only at the max level 30 ([[gameplay/classes-and-legions]] §1, guides). *guide*
- Patch history: transformation cooldown 10 → **120 s** ([WM 0621](https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204)); hero durability 24 → 240 ([WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018)); a hero gets a share of the gear stats, 35 % at T1+0, 45 % at T1+15, 65 % at T2+10, 100 % at T3+15 ([WM 0628](https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838)); Innocence Crystal durability 1,500, −5 per second while transformed, no level limit ([WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)) ([[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes). *notes*

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
