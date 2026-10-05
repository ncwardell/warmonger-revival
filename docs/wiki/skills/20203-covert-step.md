---
title: "Covert Step"
type: "skill"
id: 20203
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 20203"]
name_key: "Skill_20203"
desc_key: "SkillComment_20203"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: null
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 132, "value": 5, "rate": 1}
  - {"slot": 4, "type": 302, "value": 20203, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 100, "stats": [{"code": 132, "value": 5}], "buffs": [{"buff": 20203, "rate": 100}]}
visual: 437
icon: {"file": "Skill_Boss_01.dds", "index": 31}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4164ff type=86a754 id=87f06e sources=ba85e3 name_key=8bed23 desc_key=788f33 kind=ac3478 kind_name=65782b target=069ef3 range=fe5dbb cost=2be88c cooldown=367d78 effect_kind=356a19 effects=5aa38c damage_or_effect=8eebda visual=bf9e99 icon=10f839 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Covert Step](../assets/skills/20203.png) |
| **Skill id** | `20203` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 437 `아르타모스_은밀한 발걸음 추가 피해` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 31 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 5 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/20203-covert-steps-your-basic-attacks-deal-additional-damage\|Covert Steps: Your basic Attacks deal additional damage]] | 100 |

**Reading:** amount **80 + 100% Attack**; damage (physical?); applies [[wiki/buffs/20203-covert-steps-your-basic-attacks-deal-additional-damage|Covert Steps: Your basic Attacks deal additional damage]] (100%).
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
