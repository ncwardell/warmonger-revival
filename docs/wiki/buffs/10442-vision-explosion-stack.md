---
title: "Vision explosion : Stack"
type: "buff"
id: 10442
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 10442", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "notes: [[gameplay/classes-and-legions]] §5 Skeleton King's Vision Bow, WM 0110 (max 10 stacks, 7 s; matches client)"]
name_key: "SkillBuff_10442"
duration: {"ticks": 35, "seconds": 7.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 405, "stat": "code 405 (unknown)", "value": 10}
icon: {"file": "Skill_Miriam_01.png", "index": 35}
applied_by:
  - {"skill": 5494, "slot": 4, "type": 301, "rate": 100}
  - {"skill": 5495, "slot": 3, "type": 301, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=b29f55 type=6143a1 id=e659b3 sources=68c1cd name_key=39179c duration=bdf5bf is_buff=b6589f stack_type=356a19 group=b6589f effects=027940 icon=8527d3 applied_by=d56317 -->
|  |  |
|---|---|
|  | ![Vision explosion : Stack](../assets/buffs/10442.png) |
| **Buff id** | `10442` |
| **Duration** | 7 s (35 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 35 |

### Tooltip

> Vision explosion : Stack

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 405 | code 405 (unknown) | 10 |

### Applied by

- Skill [[wiki/skills/5494-essence-wave|Essence Wave]], effect slot 4 (type 301, rate 100%)
- Skill [[wiki/skills/5495|Skill 5495]], effect slot 3 (type 301, rate 100%)
<!-- generated:end -->

## Notes

- Vision stack of Skeleton King's Vision Bow (item 15005). [WM 0110](https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842): stacks come from basic attacks, up to 10, and last 7 s; Vision Explosion (W) spends them and Essence Wave (R) adds one per enemy hit ([[gameplay/classes-and-legions]] §5). The client buff (7 s, value 10) matches. *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
