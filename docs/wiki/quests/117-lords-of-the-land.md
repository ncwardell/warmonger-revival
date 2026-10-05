---
title: "Lords of the Land"
type: "quest"
id: 117
status: "complete"
missing: []
sources: ["client: Quest.cdb id 117", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 714", "client: QuestTalk.cdb id 912", "guide: [[gameplay/lords-of-the-land]] §4 (objective type 15 = conquer 2 NPC lands, then talk to Kelsey 210); image shows \"Conquer NPC territory (2/2)\""]
manual: ["objectives"]
name_key: "Quest_Title_693"
kind: 0
kind_name: "Main"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 51
requires_bit: 52
automatic: true
prev: [29]
next: [763]
stages: [1, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 15, "what": "conquer_npc_land", "count": 2, "a": 3, "c": 2, "text_key": "Quest_QuickText_693_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 210, "talk": 912, "text_key": "Quest_QuickText_693_1_"}
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 3, "c": 2, "text_key": "Quest_QuickText_693_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 210, "talk": 912, "text_key": "Quest_QuickText_693_1_"}
rewards:
  - {"type": 2, "what": "exp", "amount": 100000, "shown": 90909}
  - {"type": 1, "what": "item", "item": 1024, "count": 1, "pick": "fixed"}
offer_talk: 714
---
<!-- generated:start -->
<!-- generated-keys: title=bb813a type=eb5b2b id=d0e2db sources=411b14 name_key=951d1f kind=b6589f kind_name=b3f808 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=b7eb6c requires_bit=a93349 automatic=5ffe53 prev=f7cf3c next=6c698d stages=a80fa1 objectives=2be88c objectives_client=a25197 rewards=fd89ae offer_talk=3acc03 -->
|  |  |
|---|---|
|  | ![Lords of the Land](../assets/npcs/210.png) |
| **Quest id** | `117` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 51 |
| **Requires bit** | 52 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]]
- **Next:** [[wiki/quests/763-no2-lords-of-the-land|No2. Lords of the Land]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=3, c=2 — tracker: “Occupy neutral monster zone”
2. Talk to [[wiki/npcs/210-kesley|Kesley]] (dialogue 912) — tracker: “Return to Kesley”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 100,000 exp (shown in game as 90,909); [[wiki/items/1024-help-of-gaia-box|Help of Gaia Box]]

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 714)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** I'll give you important information…  
> **Kesley:** You get the Lords of the Land Buff when you help occupy or defend territories in Gaia.  
> **Kesley:** Occupy a new territory for our nation and come back to me.  
> *(accept / continue)*

#### Objective 2 (QuestTalk 912)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** You came back winning the war~ He suffered. <br>This is Gaia Box. If you open the box, you can get good rewards ~  
> *(accept / continue)*

### Seen in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]]
- [[gameplay/server-rules|Server rules checklist]]

### Mentioned in

- [[gameplay/README|Gameplay]]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/pvp-and-matches|PvP, land wars and matches]]
- [[gameplay/sources|Sources and gaps]]
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]]
<!-- generated:end -->

## Notes

Kelsey (210, Legion Manager, Fortress) asks the player to conquer 2 NPC lands and then talk to her; reward 100,000 exp + Help of Gaia Box (1024) ([[gameplay/lords-of-the-land]] §4). A Crush Online screenshot of the quest log shows "Conquer NPC territory (2/2)" and "Gain a random box as a reward", with the 2nd box as the reward. *client + guide*

## Behaviour

The quest is completed by claiming the Lords of the Land box whose stack count equals the number of conquests, starting from zero stacks (here the 2nd box). Gaining more stacks than the quest needs overwrites the progress and the player must start again ([[gameplay/lords-of-the-land]] §1, §4). Stacks: +1 for winning a war against the NPC side or defending a land, none for taking an enemy land, −1 for losing or leaving a war ([[gameplay/server-rules]], [[gameplay/pvp-and-matches]]). The strategy guide advises putting this quest line off ([[gameplay/pvp-and-matches]]). *guide*

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
