---
title: "Battle Arena"
type: "quest"
id: 839
status: "partial"
missing: ["giver", "objectives"]
sources: ["client: Quest.cdb id 839", "client: QuestTalk.cdb id 771"]
name_key: "Quest_Title_839"
kind: 7
kind_name: "Daily"
level: {"min": 28, "max": 30}
giver: null
turn_in: {"auto": true}
bit: 0
automatic: true
prev: []
next: []
prerequisites:
  - {"type": 4, "what": "level", "min": 28, "max": 30}
  - {"type": 5, "what": null}
stages: [5, 5, 5, 5, 5]
objectives: null
objectives_client:
  - {"n": 1, "type": 15, "what": null, "a": 10, "c": 1, "text_key": "Quest_QuickText_839_1"}
rewards:
  - {"type": 1, "what": "item", "item": 1000, "count": 5, "pick": "fixed"}
offer_talk: 771
---
<!-- generated:start -->
<!-- generated-keys: title=3ff156 type=eb5b2b id=706a95 sources=79e140 name_key=1c8ac8 kind=902ba3 kind_name=b6566f level=cf7982 giver=2be88c turn_in=847ad4 bit=b6589f automatic=5ffe53 prev=97d170 next=97d170 prerequisites=7f7bb1 stages=30caa7 objectives=2be88c objectives_client=093c35 rewards=8b0755 offer_talk=5d0fb6 -->
|  |  |
|---|---|
| **Quest id** | `839` |
| **Kind** | Daily (kind 7) |
| **Level** | 28–30 |
| **Giver** | **unknown** |
| **Turn in** | automatic |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** nothing (no prerequisite bit)
- **Next:** nothing: no quest requires this quest's bit (chain end)

### Requirements

| type | meaning | value |
|---|---|---|
| 4 | level | level 28–30 |
| 5 | unknown | no values |

### Objectives

> [!warning] Not all objective types are decoded
> The rows below are the client's (`objectives_client`). Write the server-ready list into `objectives:` once the unclear ones are understood.

1. Type 15 — monster-area war / occupation?; values a=10, c=1 — tracker: “Win Battle Arena”

### Rewards

- **Basic reward:** [[wiki/items/1000-medal-bronze|Medal : Bronze]] × 5

### Dialogue

#### Offer (QuestTalk 771)

Speaker: [[wiki/npcs/240-candice|Candice]]

> **Candice:** Have you heard about the Battle Arena? Anyone can get a huge reward in Arena if they win.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/arena-ranking-rewards|Battle Arena monthly ranking rewards]]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]]
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]]
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/pvp-and-matches|PvP, land wars and matches]]
- [[gameplay/server-rules|Server rules checklist]]
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]]
- [[gameplay/sources|Sources and gaps]]
- [[gameplay/videos|Videos]]
<!-- generated:end -->

## Notes

The Battle Arena is field 140; its NPC is unit 240 in the Fortress, which was disabled in October 2016 ([[gameplay/arena-ranking-rewards]]). *client + guide*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

Gameplay pages this page draws on:

- [[gameplay/arena-ranking-rewards]]
- [[gameplay/skull-artifact-set]]

## Open questions

A 2016 screenshot shows a "[Monthly] Battle Arena" quest (win 20 arena matches, 6/20) ([[gameplay/skull-artifact-set]]); the client has only these two daily-group rows for the arena.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
