---
title: "Scroll of Reduced Area Damage [S] : Supreme protection from Area Damage."
type: "buff"
id: 2096
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2096", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_2096"
duration: {"ticks": 1500, "seconds": 300.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2085
effects:
  - {"code": 270, "stat": "Reduced Area Damage(%)", "value": 20}
icon: {"file": "Items_30.png", "index": 19}
applied_by:
  - {"item": 723}
---
<!-- generated:start -->
<!-- generated-keys: title=995804 type=6143a1 id=f426c6 sources=552efa name_key=25ab96 duration=995f11 is_buff=b6589f stack_type=356a19 group=d32f6a effects=71e67d icon=6af970 applied_by=4c2278 -->
|  |  |
|---|---|
|  | ![Scroll of Reduced Area Damage (S) : Supreme protection from Area Damage.](wiki/assets/buffs/2096.png) |
| **Buff id** | `2096` |
| **Duration** | 5 min (1,500 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2085 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Items_30.png` cell 19 |

### Tooltip

> Scroll of Reduced Area Damage [S] : Supreme protection from Area Damage.

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 270 | Reduced Area Damage(%) | 20 |

### Applied by

- Using [[wiki/items/723-tome-of-patience-s|Tome of Patience (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/consumables|Consumables and clickables]] § 2. Buff clickables: values per grade (line 57): Tome · Tome of Patience · 720–723 · 2093–2096 · Area damage taken −5 / 10 / 15 / 20% (opt 270)
- [[gameplay/stat-values|Stat values and caps]] § 5. Consumables (Sheet3 tab) vs the client (line 77): Tome S · Crit 20%, less AoE 20%, Cooldown 12%, Attack speed 40 · Critical Strikes +20% (2100), Reduced Area Damage 20% (2096), Cooldown Reduction 12% (2092),...
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
