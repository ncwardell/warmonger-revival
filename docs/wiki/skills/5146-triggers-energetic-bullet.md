---
title: "Triggers Energetic Bullet"
type: "skill"
id: 5146
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 5146"]
name_key: "Skill_5146"
desc_key: "SkillComment_5146"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 132, "value": 3, "rate": 1}
  - {"slot": 4, "type": 302, "value": 10170, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 80, "stats": [{"code": 132, "value": 3}], "buffs": [{"buff": 10170, "rate": 100}]}
weapon_type: 9
visual: 289
icon: {"file": "Skill_Einsel_01.png", "index": 28}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=25d5a7 type=86a754 id=0e1964 sources=c57298 name_key=2cae70 desc_key=c9ad31 kind=ac3478 kind_name=65782b target=069ef3 range=902ba3 cost=2be88c cooldown=367d78 effect_kind=356a19 effects=9aabee damage_or_effect=7877c2 weapon_type=0ade7c visual=6b0f4d icon=721c7c used_by=97d170 -->
|  |  |
|---|---|
|  | ![Triggers Energetic Bullet](wiki/assets/skills/5146.png) |
| **Skill id** | `5146` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 9 |
| **Visual** | skillVisual 289 `PCE_Gun_05_Q_암흑탄 추가 피해` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 28 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 3 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10170-energetic-bullet-your-next-basic-attack-deals-additional-dam\|Energetic Bullet : Your next basic attack deals additional damage]] | 100 |

**Reading:** amount **10 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10170-energetic-bullet-your-next-basic-attack-deals-additional-dam|Energetic Bullet : Your next basic attack deals additional damage]] (100%).
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
