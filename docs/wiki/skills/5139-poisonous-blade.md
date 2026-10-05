---
title: "Poisonous Blade"
type: "skill"
id: 5139
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5139"]
name_key: "Skill_5139"
desc_key: "SkillComment_5139"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10164, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 70, "buffs": [{"buff": 10164, "rate": 100}]}
visual: 280
icon: {"file": "Skill_Miriam_01.png", "index": 24}
used_by:
  - {"weapon_base": 31, "slot": 1, "items": [35009]}
---
<!-- generated:start -->
<!-- generated-keys: title=79cd7e type=86a754 id=0f5e08 sources=32bc20 name_key=2c9ad7 desc_key=57c4bb kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=e3989d effect_kind=356a19 effects=fea908 damage_or_effect=87f756 visual=ba613d icon=78290d used_by=7150e6 -->
|  |  |
|---|---|
|  | ![Poisonous Blade](wiki/assets/skills/5139.png) |
| **Skill id** | `5139` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 280 `PCM_Knife_05_Q_독 묻은 검` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 24 |

### Tooltip

> [Active] You gain additional 10% Attack Damage and Attack Speed for 6 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10164-poisonous-blade-increases-attack-damage\|Poisonous Blade: Increases Attack Damage]] | 100 |

**Reading:** amount **75 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10164-poisonous-blade-increases-attack-damage|Poisonous Blade: Increases Attack Damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 31: [[wiki/items/35009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
