---
title: "Demon Hell"
type: "quest"
id: 743
status: "complete"
missing: []
sources: ["client: Quest.cdb id 743", "video: [[gameplay/video-early-quests]] §4 (kind 3 quest exp shown = table value)", "client: QuestTalk.cdb id 763"]
name_key: "Quest_Title_760"
kind: 3
kind_name: "Free"
giver: {"npc": 213}
turn_in: {"auto": true}
offer_maps: [120, 120, 120]
bit: 0
requires_bit: 30
excludes_bit: 31
owned_field: 125
automatic: true
prev: [34]
next: []
stages: [5, 5, 5, 5, 5]
objectives:
  - {"n": 1, "type": 12, "what": "reach_map", "map": 126, "maps": [126, 126, 126], "text_key": "Quest_QuickText_760_1"}
  - {"n": 2, "type": 1, "what": "collect", "unit_group": 10031, "units": [662], "count": 10, "item": 2574, "rate": 70, "maps": [126, 126, 126], "text_key": "Quest_QuickText_760_2"}
rewards:
  - {"type": 2, "what": "exp", "amount": 45000, "shown": 45000}
offer_talk: 763
---
<!-- generated:start -->
<!-- generated-keys: title=be0e6f type=eb5b2b id=f032e5 sources=580456 name_key=0a25b6 kind=77de68 kind_name=01e781 giver=91ad7d turn_in=847ad4 offer_maps=15f2a7 bit=b6589f requires_bit=22d200 excludes_bit=632667 owned_field=0ca927 automatic=5ffe53 prev=91a33c next=97d170 stages=30caa7 objectives=e246a6 rewards=4b5c7d offer_talk=e1de5f -->
|  |  |
|---|---|
|  | ![Demon Hell](wiki/assets/npcs/213.png) |
| **Quest id** | `743` |
| **Kind** | Free (kind 3) |
| **Giver** | [[wiki/npcs/213-odin\|Odin]] |
| **Turn in** | automatic |
| **Offered on** | [[wiki/fields/120-fortress\|Fortress]] (120) |
| **Completion bit** | none (no bit is set: can be taken again) |
| **Requires bit** | 30 |
| **Not after bit** | 31 |
| **Field c7@10** | [[wiki/dungeons/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon]] (125) (contract: fort the nation must own) |
| **Automatic flag** | set (c14@11) |

### Chain

- **After:** [[wiki/quests/34-tow-canyon|Tow Canyon]]
- **Next:** nothing: no quest requires this quest's bit (chain end)
- **Not offered after:** [[wiki/quests/35-demon-hell|Demon Hell]]

### Objectives

1. Go to [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126) — tracker: “Move to the Demonic Hell Boundary Area” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)
2. Collect [[wiki/items/2574-unknown-crystal|Unknown Crystal]] × 10 from any unit of kill group 10031 ([[wiki/monsters/662-demon-hunter|Demon Hunter]]) (drop 70%) — tracker: “Kill a demon and collect decisions (0/10)” — on [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] (126)

### Rewards

- **Basic reward:** 45,000 exp

### Dialogue

#### Offer (QuestTalk 763)

Speaker: [[wiki/npcs/213-odin|Odin]]

> **Odin:** The Demon living in the Devildom are coming to our world. Please go to the Demon Hell and kill them. If you kill the Demons, please bring some drop items aswell.  
> *(accept / continue)*

### Mentioned in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]]
- [[gameplay/maps-and-dungeons|Maps and dungeons]]
- [[gameplay/patch-history|Patch notes and other sources]]
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]]
- [[gameplay/server-rules|Server rules checklist]]
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
