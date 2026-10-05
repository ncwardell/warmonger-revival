---
title: "The 1st Challenge: Chepas ahead"
type: "quest"
id: 6
status: "complete"
missing: []
sources: ["client: Quest.cdb id 6", "video: [[gameplay/video-tutorial-walkthrough]] (lessons and giver-less chain quests start on their own)", "client: QuestTalk.cdb id 899", "design: requires_bit 5 and offer_maps 88/92/96 enable the prototype Frei follow-up; see [[testing]]"]
name_key: "Quest_Title_634"
kind: 0
kind_name: "Main"
giver: {"auto": true}
turn_in: {"auto": true}
bit: 6
automatic: true
manual: ["requires_bit", "offer_maps"]
requires_bit: 5
offer_maps: [88, 92, 96]
server_policy_source: "design: enable the client quest-6 variant after quest 5 in Training Camp; see docs/testing.md, Chepa continuation"
prev: [5]
next: [7]
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 4, "what": "talk", "npc": 198, "talk": 899, "maps": [89, 93, 97], "text_key": "Quest_QuickText_CB_FREI"}
rewards: []
---
<!-- generated:start -->
<!-- generated-keys: title=2ab84f type=eb5b2b id=c1dfd9 sources=764b65 name_key=6b6dd8 kind=b6589f kind_name=b3f808 giver=847ad4 turn_in=847ad4 bit=c1dfd9 automatic=5ffe53 prev=10ae24 next=bd703d stages=30caa7 objectives=70463b rewards=97d170 -->
|  |  |
|---|---|
| **Quest id** | `6` |
| **Kind** | Main (kind 0) |
| **Giver** | automatic |
| **Turn in** | automatic |
| **Completion bit** | 6 |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/5-united-problem-solvers|United Problem Solvers]]
- **Next:** [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- **Shares completion bit 6 with:** [[wiki/quests/45-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]] (completing one closes the others)

### Objectives

1. Talk to [[wiki/npcs/198-frei|Frei]] (dialogue 899) — tracker: “Report back to Frei” — on Arslan: [[wiki/fields/89-training-ground|Training Ground]] (89) · Erion: [[wiki/fields/93-training-ground|Training Ground]] (93) · Armia: [[wiki/fields/97-training-ground|Training Ground]] (97)

### Rewards

None in the client.

### Dialogue

#### Objective 1 (QuestTalk 899)

Speaker: [[wiki/npcs/198-frei|Frei]]

> **You:** Oooook... About those tests?  
> **Frei:** Your first challenge will be to hunt down the Chepa Leaders. <br>This is Innocence Fragment. Take it to Shaia.  
> **You:** Chepa Leaders? As good as done! I should go to Shaia and ask about them.  
> *(accept / continue)*

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]]: step 15 at [12:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=755s)
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]]: step 7 at [16:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=997s)
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]]: step 16 at [20:20](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1220s)
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

The Python prototype automatically assigns this supported variant after completion
bit 5, in Training Camp. A server-validated conversation with Frei is required
before setting bit 6 and unlocking quest 7 at Shaia. Assignment is restored on
reconnect and deferred if the quest log is full. This is an explicit prototype
policy using the chain edge in [[wiki/quests/5-united-problem-solvers]], not a
recovered original-server rule.

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

Client inspection at `0x599395..0x5993ab` shows the type-4 marker map check uses
objective parameter b (zero for this row), not the three tracker map IDs.
`FUN_00597b0e` sends the matching talk report without a map check. This supports
testing Frei's conversation in Camp, but tracker navigation and live UI still
need verification. See `contract/quests.yaml` for loader offsets.

The client row names Frei but puts the objective in Training Ground; Frei is
placed in Training Camp. The videos also show the alternate quest 45, which
shares completion bit 6, starts with an Innocence Fragment prerequisite, and
asks for Shaia. The prototype follows quest 6's actual NPC target at Frei's
location. Its marker/dialogue behavior needs a real-client check; quest 45 and
the fragment chain are not implemented. No claim of an exact historical flow
is made by these server policy fields.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
