---
title: "Backstab"
type: "skill"
id: 10462
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 10462", "client: StringAll_Eng SkillComment_10462 (tooltip value tags)"]
name_key: "Skill_10462"
desc_key: "SkillComment_10462"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 2
cost: null
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 10, "rate": 100}
  - {"slot": 2, "type": 101, "value": 105, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30426, "rate": 100}
  - {"slot": 4, "type": 302, "value": 30422, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 10, "attack_pct": 105, "buffs": [{"buff": 30426, "rate": 100}, {"buff": 30422, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 105}
weapon_type: 1
visual: 467
icon: {"file": "Skill_Miriam_01.png", "index": 29}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=982e1b type=86a754 id=add40f sources=64b333 name_key=ef4301 desc_key=cb76e1 kind=ac3478 kind_name=65782b target=069ef3 range=da4b92 cost=2be88c cooldown=367d78 effect_kind=356a19 effects=63ac25 damage_or_effect=1a5f44 tooltip_formula=4d8780 weapon_type=356a19 visual=ec2b67 icon=c0fb59 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Backstab](wiki/assets/skills/10462.png) |
| **Skill id** | `10462` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 2 (world units) |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Needs weapon type** | 1 |
| **Visual** | skillVisual 467 `마력의 은신 대거_은신술_피격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 29 |

### Tooltip

> [Active] Your Movement Speed is increased. Inflicts `{EF_STATIC 10}``{EF_R_DAM 105}` Damage during a basic attack. Reduces Movement Speed of all hit targets.

Tooltip formula: **10 + 105% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 10 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 105 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30426-backstab-reduced-movement-speed\|Backstab : Reduced movement speed]] | 100 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/30422-backstab-your-basic-attacks-deal-additional-damage\|Backstab : Your basic Attacks deal additional damage]] | 100 |

**Reading:** amount **10 + 105% Attack**; damage (physical?); applies [[wiki/buffs/30426-backstab-reduced-movement-speed|Backstab : Reduced movement speed]] (100%); applies [[wiki/buffs/30422-backstab-your-basic-attacks-deal-additional-damage|Backstab : Your basic Attacks deal additional damage]] (100%).

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 97): 0420 · Magical Hiding Dagger (15008) · Q cooldown 15 → 19 s, W 20 → 25 s (client: Backstab 20 s, Deception 25 s)
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
