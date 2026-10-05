---
title: "Dark Knight Skull Transformation"
type: "skill"
id: 20001
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20001", "guide: [[gameplay/classes-and-legions]] §1 (hero usable only at level 30)", "notes: [[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes (WM 0621 cooldown 10 → 120 s, 0402 durability, 0628 gear share, 1107 Innocence Crystal)", "video: [[gameplay/video-fort-war]] §1 Hero form, P2 0:07 (HP/MP ×2.2, HP 50 % on transform, ≥ 8.5 min, X countdown ~10 s)"]
name_key: "Skill_20001"
desc_key: "SkillComment_20001"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20001, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20020, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20001, "rate": 100}, {"buff": 20020, "rate": 100}]}
visual: 178
icon: {"file": "Items_20.png", "index": 19}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=1ba7e6 type=86a754 id=8a91c6 sources=25fdbf name_key=ab0d3b desc_key=aa753c kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=a7242f effect_kind=da4b92 effects=46ffaf damage_or_effect=e21297 visual=25293f icon=a71171 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Dark Knight Skull Transformation](../assets/skills/20001.png) |
| **Skill id** | `20001` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Items_20.png` cell 19 |

### Tooltip

> [Active] Dark knight Skull transformation. 
> Consumes EXP when transforming.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20001\|Buff 20001]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds\|Immortal Body : Recovering for 300 seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20001|Buff 20001]] (100%); applies [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds|Immortal Body : Recovering for 300 seconds]] (100%).
<!-- generated:end -->

## Notes

- Hero transformation (key X). Heroes are unlocked from gacha hero pieces and usable only at the max level 30 ([[gameplay/classes-and-legions]] §1, guides). *guide*
- Patch history: transformation cooldown 10 → **120 s** ([WM 0621](https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204)); hero durability 24 → 240 ([WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018)); a hero gets a share of the gear stats, 35 % at T1+0, 45 % at T1+15, 65 % at T2+10, 100 % at T3+15 ([WM 0628](https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838)); Innocence Crystal durability 1,500, −5 per second while transformed, no level limit ([WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)) ([[gameplay/classes-and-legions]] §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes). *notes*
- Dark Knight Skull hero balance: passive cooldown fixed at 300 s ([WM 0615](https://steamcommunity.com/games/718790/announcements/detail/2842216343262999426)), see [[wiki/skills/20000-dark-knight-skull-passive|20000]] ([[gameplay/classes-and-legions]] §5 Heroes). *notes*
- Seen in play in [[gameplay/video-fort-war]] §1 Hero form ([P2 0:07](https://www.youtube.com/watch?v=6_z6CUpZj30&t=7s)): max HP / MP went from 7,282 / 1,660 to 16,214 / 3,645 (×2.2); HP was set to exactly 50 % of the new max and MP to 25 %; the form lasted at least 8.5 min of heavy fighting; the X slot then counted down from about 10 s. *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §1, §5 Heroes, [[gameplay/events-and-schedules]] §9, [[gameplay/patch-history]] Heroes, [[gameplay/video-fort-war]] §1.

## Open questions

- Cooldown: the June 2018 video (uploaded 24 Jun, three days after WM 0621) shows the X slot counting down from about 10 s after transforming, while WM 0621 and this client row say 120 s. The video may predate the patch. Client kept.
- Hero stats: observed max HP 16,214 is not base 7,282 + `HeroData` hp 10,890, so the stat formula is unknown ([[gameplay/video-fort-war]] §5).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
