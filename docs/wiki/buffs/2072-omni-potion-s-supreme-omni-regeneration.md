---
title: "Omni Potion [S] : Supreme Omni Regeneration"
type: "buff"
id: 2072
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2072", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/potion-regen]] client data (item → buff, regen values)", "guide: [[gameplay/consumables]] §1, §3 (17 s vs 16 s; no family; tooltip totals)", "player: [[gameplay/potion-regen]] tick measurements (Crush Online, March 2017; history)"]
name_key: "SkillBuff_2072"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 38}
  - {"code": 34, "stat": "Mana Regeneration", "value": 8}
icon: {"file": "Items_01.png", "index": 14}
applied_by:
  - {"item": 897}
---
<!-- generated:start -->
<!-- generated-keys: title=05a17a type=6143a1 id=7e1fa8 sources=4a0878 name_key=8b08c8 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=1833b7 icon=7beea6 applied_by=50b30f -->
|  |  |
|---|---|
|  | ![Omni Potion (S) : Supreme Omni Regeneration](wiki/assets/buffs/2072.png) |
| **Buff id** | `2072` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 14 |

### Tooltip

> Omni Potion [S] : Supreme Omni Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 38 |
| 34 | Mana Regeneration | 8 |

### Applied by

- Using [[wiki/items/897-health-mana-potion-s|Health Mana Potion (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 34): 897 · Health Mana Potion [S] · 202 · 50 · 2072 · 38 · 8
<!-- generated:end -->

## Notes

- Buff of Health Mana Potion [S] (item 897): HP regen 38, MP regen 8; the item tooltip promises 600 HP + 120 MP in total over 16 s ([[gameplay/potion-regen]] client data; [[gameplay/consumables]] §3). *client*
- Duration: 85 ticks = 17 s, while the tooltip says 16 s (probably 16 regen ticks after the first) ([[gameplay/consumables]] §1). Potions are in no exclusive family, so HP and MP potions run together ([[gameplay/consumables]] §1, buffs guide §3). *client + guide*

## Behaviour

- The tooltip totals are the buff value × 16, so the intended rule reads as "regen value per second for 16 s" (*guess*, [[gameplay/potion-regen]]). In Crush Online (March 2017) the live server paid about value × 3.2 per ~6 s regen tick, so only 3–4 ticks landed inside the window ([[gameplay/potion-regen]], player measurements).
- S-grade measurement (Crush Online, March 2017): 120 HP + 24 MP × 4 ticks = 480 / 96 of 600 / 120 ([[gameplay/potion-regen]]; [[gameplay/crush-mechanics]] §4). *player/image*

## Sources

- Gameplay pages this page draws on: [[gameplay/potion-regen]], [[gameplay/consumables]] §1, §3.

## Open questions

- Payout rule: "faithful" (value × 3.2 per regen tick inside 16 s, as Crush Online did) or "as advertised" (value × 16 in total). [[gameplay/server-rules]] leaves the choice open.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
