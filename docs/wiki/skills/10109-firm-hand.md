---
title: "Firm Hand"
type: "skill"
id: 10109
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10109"]
name_key: "Skill_10109"
desc_key: "SkillComment_10109"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 30099, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30099, "rate": 100}]}
visual: 244
icon: {"file": "Skill_Dolorece_01.png", "index": 17}
used_by:
  - {"weapon_base": 163, "slot": 2, "items": [21021]}
---
<!-- generated:start -->
<!-- generated-keys: title=c3c11a type=86a754 id=d216cf sources=fd1ef7 name_key=4b7764 desc_key=6570b3 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=060055 cooldown=5b7687 effect_kind=b6589f effects=dc9485 damage_or_effect=ab3891 visual=01592d icon=159906 used_by=118580 -->
|  |  |
|---|---|
|  | ![Firm Hand](../assets/skills/10109.png) |
| **Skill id** | `10109` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Visual** | skillVisual 244 `PCD_Cannon_01_W 강인한 정신` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 17 |

### Tooltip

> [Active] Increases your Damage by 30% of your current Armor for 5 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/30099-firm-hand-you-deal-additional-damage-based-on-your-current-a\|Firm Hand : You deal additional damage based on your current Armor]] | 100 |

**Reading:** applies [[wiki/buffs/30099-firm-hand-you-deal-additional-damage-based-on-your-current-a|Firm Hand : You deal additional damage based on your current Armor]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 163: [[wiki/items/21021-magical-protect-cannon|Magical Protect Cannon]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
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
