---
title: "Return"
type: "skill"
id: 30
status: "partial"
missing: ["damage_or_effect", "cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 30", "video: [[gameplay/video-character-creation-and-tutorial]] §5, 15:15 (Return Scroll → Training Camp; inferred)"]
name_key: "Skill_30"
desc_key: "SkillComment_30"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: null
cooldown: null
cast_ms: 5000
effect_kind: 0
effects: []
damage_or_effect: {}
visual: 243
icon: {"file": "Skill_Miriam_01.png", "index": 8}
used_by:
  - {"item_use": 906}
---
<!-- generated:start -->
<!-- generated-keys: title=f9617f type=86a754 id=22d200 sources=d1a17e name_key=dd5ba4 desc_key=7b07f7 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=2be88c cooldown=2be88c cast_ms=f8237d effect_kind=b6589f effects=97d170 damage_or_effect=bf21a9 visual=4af7f9 icon=a11afc used_by=6b1e54 -->
|  |  |
|---|---|
|  | ![Return](../assets/skills/30.png) |
| **Skill id** | `30` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cast time** | 5 s |
| **Visual** | skillVisual 243 `귀환` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 8 |

### Tooltip

> [Active] Gain 30 Attack and 100 Movement Speed for 3 seconds.

### Used by

- Cast when [[wiki/items/906-scroll-return|Scroll : Return]] is used (Item_Base option 210)

### Mentioned in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 1. Map order (line 22, at 36:05): 36:05 · Training Camp · return
<!-- generated:end -->

## Notes

- Cast by Scroll : Return (item 906). In the June 2018 tutorial video the player used it in the Training Ground and reappeared in the Training Camp after a short load ([[gameplay/video-character-creation-and-tutorial]] §5, [15:15](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=915s); *inferred*). Wren sells the scroll for 79 gold ([[gameplay/video-character-creation-and-tutorial]] §3 step 12). *video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §3, §5.

## Open questions

- The client tooltip of this row ("Gain 30 Attack and 100 Movement Speed for 3 seconds") does not describe a return; the destination rule is not in any source.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
