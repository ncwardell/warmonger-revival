---
title: "Innocence report"
type: "quest"
id: 44
status: "stub"
missing: ["next"]
sources: ["client: Quest.cdb id 44", "client: QuestTalk.cdb id 854", "client: QuestTalk.cdb id 855"]
name_key: "Quest_Title_31"
kind: 0
kind_name: "Main"
giver: {"npc": 200}
turn_in: {"npc": 325}
offer_maps: [120, 120, 120]
bit: 89
requires_bit: 32
prev: [36]
next: []
prerequisites:
  - {"type": 6, "what": "item", "item": 2548, "count": 1}
  - {"type": 6, "what": "item", "item": 911, "count": 1}
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 13, "what": "use_item", "item": 911, "count": 1, "text_key": "Quest_QuickText_31_1"}
  - {"n": 2, "type": 4, "what": "talk", "npc": 327, "maps": [90, 94, 98], "text_key": "Quest_QuickText_31_3"}
  - {"n": 3, "type": 0, "what": "report", "text_key": "Quest_QuickText_24_1"}
rewards:
  - {"type": 1, "what": "item", "item": 8501, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 8500, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 8506, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 8507, "count": 1, "pick": "choose", "e": 1}
  - {"type": 1, "what": "item", "item": 7162, "count": 1, "pick": "fixed"}
offer_talk: 854
complete_talk: 855
---
<!-- generated:start -->
<!-- generated-keys: title=64b9bc type=eb5b2b id=98fbc4 sources=2ea1ca name_key=6179d6 kind=b6589f kind_name=b3f808 giver=1caac0 turn_in=ad0cc6 offer_maps=15f2a7 bit=16b06b requires_bit=cb4e52 prev=f7a9ff next=97d170 prerequisites=ae2852 stages=30caa7 objectives=7f3f02 rewards=bf883d offer_talk=cbc34d complete_talk=ebcab2 -->
|  |  |
|---|---|
|  | ![Innocence report](../assets/npcs/200.png) |
| **Quest id** | `44` |
| **Kind** | Main (kind 0) |
| **Giver** | [[wiki/npcs/200-freya\|Freya]] |
| **Turn in** | [[wiki/npcs/325-joel\|Joel]] |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | 89 |
| **Requires bit** | 32 |

### Chain

- **After:** [[wiki/quests/36-thorn-s-hell|Thorn's Hell]]
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 6 | item | carries [[wiki/items/2548-broken-innocence\|Broken Innocence]] |
| 6 | item | carries [[wiki/items/911-scroll-castle\|Scroll : Castle]] |

### Objectives

1. Use [[wiki/items/911-scroll-castle|Scroll : Castle]] — tracker: “Use the Castle Scroll”
2. Talk to [[wiki/npcs/327-aenes|Aenes]] — tracker: “Moving to the Temple through Oracle of the Protection” — on Arslan: [[wiki/fields/90-castle|Castle]] (90) · Erion: [[wiki/fields/94-castle|Castle]] (94) · Armia: [[wiki/fields/98-castle|Castle]] (98)
3. Report (tracker line; done by turning the quest in) — tracker: “Go to Joel: (Moving the Temple through the Oracle of the Protection)”

### Rewards

- **Basic reward:** [[wiki/items/7162-movement-rune|Movement(%) Rune]]
- **Choose one:** [[wiki/items/8501-crystal-guardian|Crystal : Guardian]] (e = 1) *or* [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]] (e = 1) *or* [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]] (e = 1) *or* [[wiki/items/8507-crystal-tempest-fisher|Crystal : Tempest Fisher]] (e = 1)

### Dialogue

#### Offer (QuestTalk 854)

Speaker: [[wiki/npcs/200-freya|Freya]]

> **Freya:** If you go to the priest, you will know more about Innocence ~  
> **Freya:** Here is the Castle scroll.  
> *(accept / continue)*

#### Completion (QuestTalk 855)

Speaker: [[wiki/npcs/325-joel|Joel]]

> **Joel:** I heard it from the Oracle. You collected all the Pieces of Innocence? <br> I would like to give you a gift to show my gratitude.  
> **Joel:** I do not think it's enough to use the Innocence yet.<br> But you will use it some day.  
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
