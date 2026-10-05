---
title: "Aura of Demise"
type: "skill"
id: 10039
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 10039"]
name_key: "Skill_10039"
desc_key: "SkillComment_10039"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 3
area: {"shape": 1, "shape_name": "circle", "radius": 3.0, "width_or_angle": 3.0}
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 45, "rate": 100}
  - {"slot": 2, "type": 131, "value": 1, "rate": 1}
  - {"slot": 3, "type": 102, "value": 55, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 45, "stats": [{"code": 131, "value": 1}], "ability_pct": 55}
visual: 219
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=c55ca4 type=86a754 id=c2bdbf sources=a0c561 name_key=eaf175 desc_key=79b679 kind=356a19 kind_name=9bc378 target=d1cc1b range=77de68 area=344636 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=c1e885 damage_or_effect=f5a15f visual=c0ba17 icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `10039` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 3 (world units) |
| **Area** | circle, radius 3, width/angle 3 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 219 `PCD_Hammer_02_W_ 귀화 피격` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 45 | 100 |
| 2 | 131 | stat? Health(%) | 1 | 1 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 55 | 0 |

**Reading:** amount **45 + 55% Ability Power**; damage (magic?).

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 45): Aura of Demise · 28 s · 180 · 45 (+0) damage to nearby enemies over 10 s, plus 1 % of own max HP per second
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
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
