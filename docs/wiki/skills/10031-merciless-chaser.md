---
title: "Merciless Chaser"
type: "skill"
id: 10031
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 10031"]
name_key: "Skill_10031"
desc_key: "SkillComment_10031"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 105, "rate": 0}
  - {"slot": 3, "type": 132, "value": 3, "rate": 1}
  - {"slot": 4, "type": 302, "value": 30029, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 105, "stats": [{"code": 132, "value": 3}], "buffs": [{"buff": 30029, "rate": 100}]}
weapon_type: 11
visual: 181
icon: {"file": "skill\\10902.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=cfa33d type=86a754 id=466b50 sources=503d12 name_key=b6885f desc_key=818838 kind=ac3478 kind_name=65782b target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=37b2d9 damage_or_effect=0ad357 weapon_type=17ba07 visual=aee544 icon=bd5d4e used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `10031` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 11 |
| **Visual** | skillVisual 181 `PCM_Bow_01_Q_피격` |
| **Icon** | `ui/icons/skill\10902.png` cell 0 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 105 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 3 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/30029-merciless-chase-your-next-basic-attack-deals-additional-dama\|Merciless Chase : Your next basic attack deals additional damage]] | 100 |

**Reading:** amount **10 + 105% Attack**; damage (physical?); applies [[wiki/buffs/30029-merciless-chase-your-next-basic-attack-deals-additional-dama|Merciless Chase : Your next basic attack deals additional damage]] (100%).
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
