---
title: "Potential Power"
type: "skill"
id: 10113
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10113"]
name_key: "Skill_10113"
desc_key: "SkillComment_10113"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 314, "value": 30113, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 30113, "rate": 100}]}
visual: 254
icon: {"file": "Skill_Miriam_01.png", "index": 13}
used_by:
  - {"weapon_base": 126, "slot": 2, "items": [16004]}
---
<!-- generated:start -->
<!-- generated-keys: title=e308ef type=86a754 id=410f98 sources=ea7aec name_key=17697a desc_key=2a4f20 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=4e8ae0 cooldown=d1c73e effect_kind=356a19 effects=f37ad9 damage_or_effect=1f1f2b visual=c9f13c icon=c4dc58 used_by=c0a5e1 -->
|  |  |
|---|---|
|  | ![Potential Power](../assets/skills/10113.png) |
| **Skill id** | `10113` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 254 `PCM_Bow_04_W 혼신의힘` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 13 |

### Tooltip

> [Active] Grants Attack and Movement Speed equal to 30% of your current Armor for 3 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/30113-disturbance-of-the-force-increased-attack-and-movement-speed\|Disturbance of the Force : Increased Attack and Movement Speed]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/30113-disturbance-of-the-force-increased-attack-and-movement-speed|Disturbance of the Force : Increased Attack and Movement Speed]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 126: [[wiki/items/16004-magical-frost-bow|Magical Frost Bow]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
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
