---
title: "No4. Lords of the Land"
type: "quest"
id: 765
status: "stub"
missing: ["objectives", "next"]
sources: ["client: Quest.cdb id 765", "video: [[gameplay/video-early-quests]] §4 (kind 0 quest exp shown = table ÷ 1.1)", "client: QuestTalk.cdb id 769", "client: QuestTalk.cdb id 912"]
name_key: "Quest_Title_765"
kind: 0
kind_name: "Main"
giver: {"npc": 210}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 113
requires_bit: 112
automatic: true
prev: [764]
next: []
stages: [1, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "c": 5, "text_key": "Quest_QuickText_765_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 210, "talk": 912, "text_key": "Quest_QuickText_693_1_"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1500000, "shown": 1363636}
  - {"type": 1, "what": "item", "item": 1027, "count": 1, "pick": "fixed"}
offer_talk: 769
---
<!-- generated:start -->
<!-- generated-keys: title=3be468 type=eb5b2b id=e1f463 sources=66953d name_key=08312f kind=b6589f kind_name=b3f808 giver=7abdb8 turn_in=847ad4 offer_maps=15f2a7 bit=e99321 requires_bit=601ca9 automatic=5ffe53 prev=7b294d next=97d170 stages=a80fa1 objectives=2be88c objectives_client=bd4ad9 rewards=36d7e5 offer_talk=98079d -->
|  |  |
|---|---|
|  | ![No4. Lords of the Land](wiki/assets/npcs/210.png) |
| **Quest id** | `765` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/210-kesley\|Kesley]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 113 |
| **Requires bit** | 112 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/764-no3-lords-of-the-land|No3. Lords of the Land]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values c=5 — tracker: “Conquer Neutral monster territory”
2. Talk to [[wiki/npcs/210-kesley|Kesley]] (dialogue 912) — tracker: “Return to Kesley”

Stages (`flag1..5` = [1, 5, 5, 5, 5]): objectives unlock in steps; with the first unfinished objective *i*, objectives 1..flag*i* are active (contract/quests.yaml).

### Rewards

- **Basic reward:** 1,500,000 exp (shown in game as 1,363,636); [[wiki/items/1027-phase-of-gaia-box|Phase of Gaia Box]]

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
