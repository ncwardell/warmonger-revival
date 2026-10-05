---
title: "Poisonous Blade : Active"
type: "skill"
id: 5288
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5288"]
name_key: "Skill_5288"
desc_key: "SkillComment_5288"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 2
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10342, "rate": 100}
  - {"slot": 4, "type": 302, "value": 10341, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "ability_pct": 70, "buffs": [{"buff": 10342, "rate": 100}, {"buff": 10341, "rate": 100}]}
weapon_type: 1
visual: 373
icon: {"file": "Skill_Miriam_01.png", "index": 24}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=8f14e1 type=86a754 id=a7ae8d sources=265b1f name_key=aa2df1 desc_key=bc277b kind=356a19 kind_name=9bc378 target=069ef3 range=da4b92 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=32652d damage_or_effect=60f7bd weapon_type=356a19 visual=a51332 icon=78290d used_by=97d170 -->
|  |  |
|---|---|
|  | ![Poisonous Blade : Active](../assets/skills/5288.png) |
| **Skill id** | `5288` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 2 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 1 |
| **Visual** | skillVisual 373 `시즌1_PCM_Knife_05_Q_독 묻은 검_피격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 24 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10342-poisonous-blade-stunned-for-2-seconds\|Poisonous Blade : Stunned for 2 seconds]] | 100 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10341-poisonous-blade-next-attack-stunned\|Poisonous Blade : Next Attack Stunned]] | 100 |

**Reading:** amount **70 + 70% Ability Power**; damage (physical?); applies [[wiki/buffs/10342-poisonous-blade-stunned-for-2-seconds|Poisonous Blade : Stunned for 2 seconds]] (100%); applies [[wiki/buffs/10341-poisonous-blade-next-attack-stunned|Poisonous Blade : Next Attack Stunned]] (100%).
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
