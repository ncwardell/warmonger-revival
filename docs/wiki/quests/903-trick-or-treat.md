---
title: "Trick or Treat!!"
type: "quest"
id: 903
status: "complete"
missing: []
sources: ["client: Quest.cdb id 903", "client: QuestTalk.cdb id 783", "client: QuestTalk.cdb id 784"]
name_key: "Quest_Title_901"
kind: 3
kind_name: "Free"
giver: {"npc": 2001}
turn_in: {"npc": 2001}
offer_maps: [98, 98, 98]
turn_in_maps: [98, 98, 98]
bit: 0
prev: []
next: []
prerequisites:
  - {"type": 3, "what": null, "a": 3}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 1, "what": "collect", "unit": 2000, "count": 20, "item": 2549, "rate": 100, "text_key": "Quest_QuickText_901_1"}
  - {"n": 2, "type": 0, "what": "report", "text_key": "Quest_QuickText_901_2"}
rewards:
  - {"type": 1, "what": "item", "item": 1056, "count": 1, "pick": "fixed"}
offer_talk: 783
complete_talk: 784
---
<!-- generated:start -->
<!-- generated-keys: title=11d9fb type=eb5b2b id=437aa7 sources=492044 name_key=009e6b kind=77de68 kind_name=01e781 giver=a31e9a turn_in=a31e9a offer_maps=3173d2 turn_in_maps=3173d2 bit=b6589f prev=97d170 next=97d170 prerequisites=c9dbbd stages=30caa7 objectives=26193f rewards=3e6aea offer_talk=43095d complete_talk=aa5076 -->
|  |  |
|---|---|
| **Quest id** | `903` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/2001-corpse-bride\|Corpse Bride]] |
| **Turn in** | [[wiki/npcs/2001-corpse-bride\|Corpse Bride]] |
| **Offered on** | [[wiki/fields/98-castle\|Castle]] (98) |
| **Completion bit** | none (no bit is set: can be taken again) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 3 | unknown | a=3 |

### Objectives

1. Collect [[wiki/items/2549-jack-s-pumpkin|Jack's Pumpkin]] × 20 from [[wiki/monsters/2000-jack-o-lantern|Jack O' Lantern]] (drop 100%) — tracker: “Gather (0/20) Jack's pumpkin”
2. Report (tracker line; done by turning the quest in) — tracker: “Go to Corpse bride”

### Rewards

- **Basic reward:** [[wiki/items/1056-halloween-rewar-box|Halloween Rewar Box]]

### Dialogue

#### Offer (QuestTalk 783)

Speaker: [[wiki/npcs/2001-corpse-bride|Corpse Bride]]

> **Corpse Bride:** Trick or Treat!! HaHa !!  
> **Corpse Bride:** Do you know? When you camouflage like ghost in halloween day, Haunters can't detect you.<br>If you don't camouflage as ghost, you will be in danger!<br>Go to Gaia and bring Jack's pumpkin to me. then i will help you.  
> *(accept / continue)*

#### Completion (QuestTalk 784)

Speaker: [[wiki/npcs/2001-corpse-bride|Corpse Bride]]

> **Corpse Bride:** Oh ! Here you are. As I promised, I will give a magical Jack's mask to you.<br>Take care yourself !!  
> *(accept / continue)*

### Mentioned in

- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
<!-- generated:end -->

## Notes

Crush Online's Halloween quest (27 Oct 2016): the NPC Corpse Bride in the nation's castle sends players to hunt Jack O'Lantern in PvE, for a reward box with the skill stone "Creep Jack"; players said the stone had only 120 spell charges ([[gameplay/crush-patch-notes]], *staff / player*). The client still has the unit (2000), the box (1056) and Jack's Pumpkin (2549). *client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/crush-patch-notes]]

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
