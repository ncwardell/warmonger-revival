---
title: "HP Potion [S]: Supreme HP Regeneration"
type: "buff"
id: 2063
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 2063", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "client: [[gameplay/potion-regen]] client data (item → buff, regen values)", "guide: [[gameplay/consumables]] §1, §3 (17 s vs 16 s; no family; tooltip totals)", "player: [[gameplay/potion-regen]] tick measurements (Crush Online, March 2017; history)"]
name_key: "SkillBuff_2063"
duration: {"ticks": 85, "seconds": 17.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 32, "stat": "Health Regeneration", "value": 75}
icon: {"file": "Items_01.png", "index": 4}
applied_by:
  - {"item": 888}
---
<!-- generated:start -->
<!-- generated-keys: title=1ab57e type=6143a1 id=c7131f sources=7eec7e name_key=43b3c1 duration=6c2ae7 is_buff=b6589f stack_type=356a19 group=b6589f effects=da9772 icon=96b2eb applied_by=9863f0 -->
|  |  |
|---|---|
|  | ![HP Potion (S): Supreme HP Regeneration](../assets/buffs/2063.png) |
| **Buff id** | `2063` |
| **Duration** | 17 s (85 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Items_01.png` cell 4 |

### Tooltip

> HP Potion [S]: Supreme HP Regeneration

### Effects

Effect codes read as `ItemOption` stat codes (*assumed*: a few rows disagree with their own tooltip, e.g. buff 1 "EXP +15%" uses code 41).

| code | effect | value |
|---|---|---|
| 32 | Health Regeneration | 75 |

### Applied by

- Using [[wiki/items/888-potion-of-health-s|Potion of Health (S)]] (Item_Base option 301)

### Mentioned in

- [[gameplay/potion-regen|Potion regeneration ticks]] § Client data: potion items and their buffs (line 24): 888 · Potion of Health [S] · 182 · 50 · 2063 · 75 · –
<!-- generated:end -->

## Notes

- Buff of Potion of Health [S] (item 888): HP regen 75; the item tooltip promises 1,200 HP in total over 16 s ([[gameplay/potion-regen]] client data; [[gameplay/consumables]] §3). *client*
- Duration: 85 ticks = 17 s, while the tooltip says 16 s (probably 16 regen ticks after the first) ([[gameplay/consumables]] §1). Potions are in no exclusive family, so HP and MP potions run together ([[gameplay/consumables]] §1, buffs guide §3). *client + guide*

## Behaviour

- The tooltip totals are the buff value × 16, so the intended rule reads as "regen value per second for 16 s" (*guess*, [[gameplay/potion-regen]]). In Crush Online (March 2017) the live server paid about value × 3.2 per ~6 s regen tick, so only 3–4 ticks landed inside the window ([[gameplay/potion-regen]], player measurements).
- S-grade measurement (Crush Online, March 2017): health 240 × 4 ticks = 960 of the 1,200 shown ([[gameplay/potion-regen]]; [[gameplay/crush-mechanics]] §4). *player/image*

## Sources

- Gameplay pages this page draws on: [[gameplay/potion-regen]], [[gameplay/consumables]] §1, §3.

## Open questions

- Payout rule: "faithful" (value × 3.2 per regen tick inside 16 s, as Crush Online did) or "as advertised" (value × 16 in total). [[gameplay/server-rules]] leaves the choice open.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
