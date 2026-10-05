---
title: "Kesley's Disgrace"
type: "quest"
id: 105
status: "stub"
missing: ["objectives"]
sources: ["client: Quest.cdb id 105", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 675"]
name_key: "Quest_Title_652"
kind: 0
kind_name: "Main"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 44
requires_bit: 22
automatic: true
prev: [22]
next: [29]
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 14, "what": null, "a": 3, "b": 1, "maps": [120, 120, 120], "text_key": "Quest_QuickText_652_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 10000, "shown": 9091}
offer_talk: 675
---
<!-- generated:start -->
<!-- generated-keys: title=64c742 type=eb5b2b id=e114c4 sources=f68554 name_key=c2d13e kind=b6589f kind_name=b3f808 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=98fbc4 requires_bit=12c6fc automatic=5ffe53 prev=5c6c1d next=f7cf3c stages=30caa7 objectives=2be88c objectives_client=6a1975 rewards=e15e5b offer_talk=fcd72f -->
|  |  |
|---|---|
|  | ![Kesley's Disgrace](../assets/npcs/210.png) |
| **Quest id** | `105` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 44 |
| **Requires bit** | 22 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]]
- **Next:** [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]]

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 14 — move to battlefield / monster area?; values a=3, b=1 — tracker: “Move to Monster area”

### Rewards

- **Basic reward:** 10,000 exp (shown in game as 9,091)

The reward panel shows quest exp lower than the table: kind 0 quests show the table value ÷ 1.1, kind 1 ÷ 1.2 ([[gameplay/video-early-quests|video notes]] §4). Which of the two the original server granted is not known.

### Dialogue

#### Offer (QuestTalk 675)

Speaker: [[wiki/npcs/210-kesley|Kesley]]

> **Kesley:** I see, the famous protector of our nation. I have a new task for you.  
> **Kesley:** Go crush those monsters occupying our territories.  
> **Kesley:** When you get to the monster occupation, you have to win the war against the NPC that occupies the area!<br>Kill a monster and use the acquired tp to kill an Officer monster and acquire his territory<br>And if you eliminate the boss that appears, you can destroy the Monster's Territory  
> **Kesley:** Oh!It would be more interesting and easy to have a party with other users or members of the legion.<br> Good Luck~  
> *(accept / continue)*
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
