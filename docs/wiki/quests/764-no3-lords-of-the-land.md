---
title: "No3. Lords of the Land"
type: "quest"
id: 764
status: "complete"
missing: []
sources: ["client: Quest.cdb id 764", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 769", "client: QuestTalk.cdb id 912", "guide: [[gameplay/lords-of-the-land]] §4 (objective type 15 = conquer 4 NPC lands, then talk to Kelsey 210)"]
manual: ["objectives"]
name_key: "Quest_Title_764"
kind: 0
kind_name: "Main"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 112
requires_bit: 111
automatic: true
prev: [763]
next: [765]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 15, "what": "conquer_npc_land", "count": 4, "c": 4, "text_key": "Quest_QuickText_764_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 210, "talk": 912, "text_key": "Quest_QuickText_693_1_"}
objectives_client:
  - {"n": 1, "type": 15, "what": null, "c": 4, "text_key": "Quest_QuickText_764_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 210, "talk": 912, "text_key": "Quest_QuickText_693_1_"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1500000, "shown": 1363636}
  - {"type": 1, "what": "item", "item": 1026, "count": 1, "pick": "fixed"}
offer_talk: 769
---
<!-- generated:start -->
<!-- generated-keys: title=e7dbc9 type=eb5b2b id=b55860 sources=53108f name_key=0d4884 kind=b6589f kind_name=b3f808 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=601ca9 requires_bit=6216f8 automatic=5ffe53 prev=6c698d next=796127 stages=a80fa1 objectives=2be88c objectives_client=382c86 rewards=38642b offer_talk=98079d -->
|  |  |
|---|---|
|  | ![No3. Lords of the Land](../assets/npcs/210.png) |
| **Quest id** | `764` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 112 |
| **Requires bit** | 111 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/763-no2-lords-of-the-land|No2. Lords of the Land]]
- **Next:** [[wiki/quests/765-no4-lords-of-the-land|No4. Lords of the Land]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values c=4 — tracker: “Conquer NPC territory”
2. Talk to [[wiki/npcs/210-kesley|Kesley]] (dialogue 912) — tracker: “Return to Kesley”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,500,000 exp (shown in game as 1,363,636); [[wiki/items/1026-ruler-of-gaia-box|Ruler of Gaia Box]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 769)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** Acquire a Lords of the Land Random Box through conquering territories controlled by NPCs or enemies.  
> *(accept / continue)*

#### Objective 2 (QuestTalk 912)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** You came back winning the war~ He suffered. <br>This is Gaia Box. If you open the box, you can get good rewards ~  
> *(accept / continue)*

### Seen in

- [[gameplay/server-rules|Server rules checklist]]

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
<!-- generated:end -->

## Notes

Kelsey (210, Legion Manager, Fortress) asks the player to conquer 4 NPC lands and then talk to her; reward 1,500,000 exp + Ruler of Gaia Box (1026) ([[gameplay/lords-of-the-land]] §4). The forum post calls this the purple (4th) box. *client + guide*

## Behaviour

The quest is completed by claiming the Lords of the Land box whose stack count equals the number of conquests, starting from zero stacks (here the 4th box). Gaining more stacks than the quest needs overwrites the progress and the player must start again ([[gameplay/lords-of-the-land]] §1, §4). Stacks: +1 for winning a war against the NPC side or defending a land, none for taking an enemy land, −1 for losing or leaving a war ([[gameplay/server-rules]], [[gameplay/pvp-and-matches]]). The strategy guide advises putting this quest line off ([[gameplay/pvp-and-matches]]). *guide*

## Sources

Gameplay pages this page draws on:

- [[gameplay/lords-of-the-land]]
- [[gameplay/server-rules]]
- [[gameplay/pvp-and-matches]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
