---
title: "Rapid Dash"
type: "skill"
id: 5149
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5149"]
name_key: "Skill_5149"
desc_key: "SkillComment_5149"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 132, "value": 3, "rate": 1}
  - {"slot": 4, "type": 302, "value": 10174, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 80, "stats": [{"code": 132, "value": 3}], "buffs": [{"buff": 10174, "rate": 100}]}
weapon_type: 9
visual: 292
icon: {"file": "Skill_Einsel_01.png", "index": 30}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=1679a3 type=86a754 id=3b92a2 sources=b9781d name_key=0e22fc desc_key=6bc7a8 kind=ac3478 kind_name=65782b target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=dae3d8 damage_or_effect=dfe0c3 weapon_type=0ade7c visual=85f100 icon=4bb647 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Rapid Dash](../assets/skills/5149.png) |
| **Skill id** | `5149` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 9 |
| **Visual** | skillVisual 292 `PCE_Gun_05_E_빠른 대쉬 추가 피해` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 30 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 3 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10174-rapid-dash-increased-attack-speed\|Rapid Dash : Increased Attack Speed]] | 100 |

**Reading:** amount **10 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10174-rapid-dash-increased-attack-speed|Rapid Dash : Increased Attack Speed]] (100%).

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 96): Client check: Skill_Base cooldowns are Soul Infestation 19 s (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail o...
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
