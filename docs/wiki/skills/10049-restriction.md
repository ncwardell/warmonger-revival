---
title: "Restriction"
type: "skill"
id: 10049
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 10049"]
name_key: "Skill_10049"
desc_key: "SkillComment_10049"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["self", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 314, "value": 30044, "rate": 100}
  - {"slot": 3, "type": 302, "value": 30043, "rate": 100}
  - {"slot": 4, "type": 102, "value": 95, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "buffs": [{"buff": 30044, "rate": 100}, {"buff": 30043, "rate": 100}], "ability_pct": 95}
weapon_type: 2
visual: 170
icon: {"file": "Skill_Einsel_01.png", "index": 20}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=a3e44e type=86a754 id=6fa07a sources=85cd87 name_key=15b97b desc_key=ad44da kind=ac3478 kind_name=65782b target=18d7a2 range=77de68 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=23470c damage_or_effect=c7117a weapon_type=da4b92 visual=717b2f icon=b7a24b used_by=97d170 -->
|  |  |
|---|---|
|  | ![Restriction](wiki/assets/skills/10049.png) |
| **Skill id** | `10049` |
| **Kind** | kind 5 (5) |
| **Target** | unit; self, enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Effect kind** | damage (magic?) (2) |
| **Needs weapon type** | 2 |
| **Visual** | skillVisual 170 `PCE_Knife_01_Q 피격 (빛의 속박)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 20 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/30044-restriction-rooted-in-place-for-3-seconds\|Restriction : Rooted in place for 3 seconds]] | 100 |
| 3 | 302 | applies buff (variant 302) | [[wiki/buffs/30043-restriction-your-next-basic-attack-deals-additional-damage\|Restriction : Your next basic attack deals additional damage]] | 100 |
| 4 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 95 | 0 |

**Reading:** amount **70 + 95% Ability Power**; damage (magic?); applies [[wiki/buffs/30044-restriction-rooted-in-place-for-3-seconds|Restriction : Rooted in place for 3 seconds]] (100%); applies [[wiki/buffs/30043-restriction-your-next-basic-attack-deals-additional-damage|Restriction : Your next basic attack deals additional damage]] (100%).
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
