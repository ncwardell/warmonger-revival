---
title: "Delivering Punishment"
type: "quest"
id: 104
status: "complete"
missing: []
sources: ["client: Quest.cdb id 104", "video: [[gameplay/video-early-quests]] §4 (kind 1 quest exp shown = table ÷ 1.2)", "client: QuestTalk.cdb id 673", "client: QuestTalk.cdb id 674"]
name_key: "Quest_Title_651"
kind: 1
kind_name: "Sub"
giver: {"npc": 217}
turn_in: {"npc": 217}
offer_maps: [120, 120, 120]
turn_in_maps: [120, 120, 120]
bit: 43
requires_bit: 13
prev: [14]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "kill", "unit_group": 10005, "units": [650, 651], "count": 10, "maps": [103, 105, 107], "text_key": "Quest_QuickText_651_1"}
  - {"n": 2, "type": 1, "what": "kill", "unit": 10006, "count": 10, "maps": [103, 105, 107], "text_key": "Quest_QuickText_651_2"}
  - {"n": 5, "type": 0, "what": "report", "maps": [120, 120, 120], "text_key": "Quest_QuickText_651_5"}
rewards:
  - {"type": 2, "what": "exp", "amount": 204000, "shown": 170000}
  - {"type": 4, "what": "gold", "amount": 20000}
  - {"type": 1, "what": "item", "item": 601, "count": 40, "pick": "fixed"}
  - {"type": 1, "what": "item", "item": 611, "count": 40, "pick": "fixed"}
offer_talk: 673
complete_talk: 674
---
<!-- generated:start -->
<!-- generated-keys: title=1e472e type=eb5b2b id=78a8ef sources=0663cf name_key=96a609 kind=356a19 kind_name=0bac50 giver=05a31e turn_in=05a31e offer_maps=15f2a7 turn_in_maps=15f2a7 bit=0286dd requires_bit=bd307a prev=76cdc5 next=97d170 stages=30caa7 objectives=3eeab1 rewards=6ddc71 offer_talk=dca7d0 complete_talk=ee4988 -->
|  |  |
|---|---|
|  | ![Delivering Punishment](wiki/assets/npcs/217.png) |
| **Quest id** | `104` |
| **Kind** | Sub (kind 1) |
| **Giver** | [[wiki/npcs/217-haley\|Haley]] |
| **Turn in** | [[wiki/npcs/217-haley\|Haley]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 43 |
| **Requires bit** | 13 |

### Chain

- **After:** [[wiki/quests/14-battle-preparations|Battle preparations]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Kill any unit of kill group 10005 ([[wiki/monsters/650-fragile-lizard-swordsman|Fragile Lizard Swordsman]], [[wiki/monsters/651-fragile-lizard-swordsman|Fragile Lizard Swordsman]]) × 10 — tracker: “Fragile Kill Lizard (0/10)” — on Arslan: [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]] (103) · Erion: [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]] (105) · Armia: [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]] (107)
2. Kill [[wiki/npcs/10006|NPC 10006]] × 10 — tracker: “Fragile Kill Elite Lizard (0/10)” — on Arslan: [[wiki/fields/103-place-for-scattered-troops|Place for Scattered troops]] (103) · Erion: [[wiki/fields/105-place-for-scattered-troops|Place for Scattered troops]] (105) · Armia: [[wiki/fields/107-place-for-scattered-troops|Place for Scattered troops]] (107)
5. Report (tracker line; done by turning the quest in) — tracker: “Talk to Haley”

### Rewards

- **Basic reward:** 204,000 exp (shown in game as 170,000); 20,000 gold; [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]] × 40; [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]] × 40

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 673)

Speaker: [[wiki/npcs/217-haley|Haley]]

> **Haley:** Because of the Lizards we lack important supplies.<br>Please get rid of them.  
> **Haley:** I think you are the only Protector strong enough to get the job done.  
> *(accept / continue)*

#### Completion (QuestTalk 674)

Speaker: [[wiki/npcs/217-haley|Haley]]

> **You:** I did what you asked me to.  
> **Haley:** Thank you for your service, the battle in the Abyss is still worrisome…  
> *(accept / continue)*

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 18 at [42:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2532s)

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]
<!-- generated:end -->

## Notes

Haley (217, Teleporter): the Lizards are cutting off supplies; kill 10 Lizard (group 10005) and 10 Elite Lizard (10006) in Place for Scattered troops (fields 103/105/107) ([42:10](https://www.youtube.com/watch?v=s04CSN16w1s&t=2530s)). Turned in at [56:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=3395s). Panel: 170,000 exp, 20,000 gold, 40/40 Passion Fragments ([[gameplay/video-early-quests]] step 18). A Fragile Lizard Swordsman had 600 HP ([53:40](https://www.youtube.com/watch?v=s04CSN16w1s&t=3220s)). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
