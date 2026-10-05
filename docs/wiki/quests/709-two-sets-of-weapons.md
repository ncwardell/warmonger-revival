---
title: "Two sets of weapons"
type: "quest"
id: 709
status: "complete"
missing: []
sources: ["client: Quest.cdb id 709", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "video: [[gameplay/video-tutorial-walkthrough]] steps 3-5 (lesson exp shown = table value)"]
name_key: "Quest_Title_672"
kind: 2
kind_name: "Guide"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 79
automatic: true
prev: []
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 10008, "what": "client_swap_weapon", "text_key": "Quest_QuickText_672_1"}
rewards:
  - {"type": 2, "what": "exp", "amount": 1000, "shown": 1000}
---
<!-- generated:start -->
<!-- generated-keys: title=0e3967 type=eb5b2b id=29da9b sources=f8df0d name_key=5302b1 kind=da4b92 kind_name=875cc6 giver=847ad4 turn_in=847ad4 bit=b74f5e automatic=5ffe53 prev=97d170 next=97d170 stages=30caa7 objectives=f7ded1 rewards=ce0ddb -->
|  |  |
|---|---|
| **Quest id** | `709` |
| **Kind** | Guide (kind 2) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 79 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Shares completion bit 79 with:** [[wiki/quests/1510-item-change-weapon|Item - Change weapon]] (completing one closes the others)

### Objectives

1. client event: weapon swap — tracker: “Press [Space] to switch between your weapons”

### Rewards

- **Basic reward:** 1,000 exp

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 26
<!-- generated:end -->

## Notes

Swap between the two weapon sets; appeared at [92:55](https://www.youtube.com/watch?v=s04CSN16w1s&t=5575s) ([[gameplay/video-early-quests]] step 26). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/video-early-quests]]
- [[gameplay/video-tutorial-walkthrough]]

## Open questions

The first-session notes give Space as the swap key, while the walkthrough's hotbar shows X as weapon swap ([[gameplay/video-early-quests]] step 26, [[gameplay/video-tutorial-walkthrough]] §3). *video*

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
