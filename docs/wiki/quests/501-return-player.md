---
title: "Return Player"
type: "quest"
id: 501
status: "stub"
missing: ["rewards", "next"]
sources: ["client: Quest.cdb id 501", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "client: QuestTalk.cdb id 897"]
name_key: "Quest_Title_501_"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"npc": 208}
turn_in_maps: [120, 120, 120]
bit: 0
prev: []
next: []
stages: [0, 0, 0, 0, 0]
objectives:
  - {"n": 1, "type": 0, "what": "report", "text_key": "Quest_QuickText_674_3"}
rewards: null
rewards_client:
  - {"type": 10, "what": null, "a": 5000}
  - {"type": 9, "what": null}
complete_talk: 897
---
<!-- generated:start -->
<!-- generated-keys: title=e89337 type=eb5b2b id=2c9a62 sources=98bda4 name_key=02ce77 kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=58f603 turn_in_maps=15f2a7 bit=b6589f prev=97d170 next=97d170 stages=46f29e objectives=b2eb7d rewards=2be88c rewards_client=46e162 complete_talk=0bab1d -->
|  |  |
|---|---|
| **Quest id** | `501` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | [[wiki/npcs/208-bell-thain\|Bell Thain]] |
| **Turned in on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Objectives

1. Report (tracker line; done by turning the quest in) — tracker: “Meeting Balten”

Stages are all 0: the client never reports progress for this quest (contract/quests.yaml).

### Rewards

> [!warning] Not all reward types are decoded
> The rows below are the client's (`rewards_client`). Write the server-ready list into `rewards:` once the unclear ones are understood.

- Type 10 — unknown 10; values a=5000
- Type 9 — unknown 9; values none

### Dialogue

#### Completion (QuestTalk 897)

Speaker: [[wiki/npcs/208-bell-thain|Bell Thain]]

> **Bell Thain:** It's been a long time! Would you like to fight again?<br>keeper!! Take this and try it once.  
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
