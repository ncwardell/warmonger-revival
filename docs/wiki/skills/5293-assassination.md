---
title: "Assassination"
type: "skill"
id: 5293
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5293"]
name_key: "Skill_5293"
desc_key: "SkillComment_5293"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 1
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 101, "value": 150, "rate": 0}
  - {"slot": 2, "type": 302, "value": 10343, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "attack_pct": 150, "buffs": [{"buff": 10343, "rate": 100}]}
weapon_type: 1
visual: 378
icon: {"file": "Skill_Miriam_01.png", "index": 25}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=073578 type=86a754 id=08ee36 sources=420284 name_key=f47e93 desc_key=7e79a4 kind=356a19 kind_name=9bc378 target=53cfaf range=356a19 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=491e53 damage_or_effect=1ad3c7 weapon_type=356a19 visual=0d990f icon=d212e9 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Assassination](wiki/assets/skills/5293.png) |
| **Skill id** | `5293` |
| **Kind** | active (1) |
| **Target** | unit; ally, enemy; units: monster, player; up to 2 |
| **Range** | 1 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 1 |
| **Visual** | skillVisual 378 `시즌1_PCM_Knife_05_W_암살_피격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 25 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 101 | % of Attack (tooltip `EF_R_DAM`) | 150 | 0 |
| 2 | 302 | applies buff (variant 302) | [[wiki/buffs/10343-assassination-active\|Assassination : Active]] | 100 |

**Reading:** amount **150% Attack**; damage (physical?); applies [[wiki/buffs/10343-assassination-active|Assassination : Active]] (100%).
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
