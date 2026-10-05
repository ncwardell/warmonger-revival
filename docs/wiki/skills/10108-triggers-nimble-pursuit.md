---
title: "Triggers Nimble Pursuit."
type: "skill"
id: 10108
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 10108"]
name_key: "Skill_10108"
desc_key: "SkillComment_10108"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 105, "rate": 0}
  - {"slot": 3, "type": 132, "value": 3, "rate": 1}
  - {"slot": 4, "type": 302, "value": 30098, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 105, "stats": [{"code": 132, "value": 3}], "buffs": [{"buff": 30098, "rate": 100}]}
weapon_type: 10
visual: 248
icon: {"file": "Skill_Dolorece_01.png", "index": 16}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=2e9cde type=86a754 id=577486 sources=3252d4 name_key=0d9137 desc_key=92eb22 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=a08bda damage_or_effect=810c04 weapon_type=b1d578 visual=ca3799 icon=197b6c used_by=97d170 -->
|  |  |
|---|---|
|  | ![Triggers Nimble Pursuit.](wiki/assets/skills/10108.png) |
| **Skill id** | `10108` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 10 |
| **Visual** | skillVisual 248 `PCD_Cannon_01_Q_피격` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 16 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 105 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 3 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/30098-nimble-pursuit-your-next-basic-attack-deals-additional-damag\|Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.]] | 100 |

**Reading:** amount **10 + 105% Attack**; damage (physical?); applies [[wiki/buffs/30098-nimble-pursuit-your-next-basic-attack-deals-additional-damag|Nimble Pursuit : Your next basic attack deals additional damage based on your targets current HP.]] (100%).
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
