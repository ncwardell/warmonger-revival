---
title: "Secret Movement"
type: "skill"
id: 10044
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 10044"]
name_key: "Skill_10044"
desc_key: "SkillComment_10044"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: null
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 105, "rate": 0}
  - {"slot": 3, "type": 132, "value": 3, "rate": 1}
  - {"slot": 4, "type": 302, "value": 30040, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 105, "stats": [{"code": 132, "value": 3}], "buffs": [{"buff": 30040, "rate": 100}]}
weapon_type: 11
visual: 258
icon: {"file": "Skill_Miriam_01.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=12d4a7 type=86a754 id=56fb44 sources=0c9834 name_key=8ea47a desc_key=d17d1c kind=ac3478 kind_name=65782b target=069ef3 range=fe5dbb cost=2be88c cooldown=367d78 effect_kind=356a19 effects=d87539 damage_or_effect=4d6578 weapon_type=17ba07 visual=982fd8 icon=bfcc89 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Secret Movement](wiki/assets/skills/10044.png) |
| **Skill id** | `10044` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 11 |
| **Visual** | skillVisual 258 `PCM_Bow_02_Q 은밀한 움직임 사격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 0 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 105 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 3 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/30040-secret-movement-your-next-basic-attack-will-deal-additional\|Secret Movement : Your next basic attack will deal additional damage]] | 100 |

**Reading:** amount **10 + 105% Attack**; damage (physical?); applies [[wiki/buffs/30040-secret-movement-your-next-basic-attack-will-deal-additional|Secret Movement : Your next basic attack will deal additional damage]] (100%).
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
