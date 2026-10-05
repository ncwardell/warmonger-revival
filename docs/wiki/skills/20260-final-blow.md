---
title: "Final blow"
type: "skill"
id: 20260
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20260", "client: StringAll_Eng SkillComment_20260 (tooltip value tags)"]
name_key: "Skill_20260"
desc_key: "SkillComment_20260"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 4, "type_name": "HP %", "amount": 10}
cooldown: {"ms": 110000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 131, "value": 6, "rate": 1}
  - {"slot": 4, "type": 43, "value": 55, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 100, "stats": [{"code": 131, "value": 6}, {"code": 43, "value": 55}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 458
icon: {"file": "Skill_Boss_01.dds", "index": 55}
used_by:
  - {"weapon_base": 75, "slot": 8, "items": [8006, 8506]}
---
<!-- generated:start -->
<!-- generated-keys: title=df8af1 type=86a754 id=ca15ea sources=c56700 name_key=8ec0e6 desc_key=9292ca kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=12e604 cooldown=e0e4dd effect_kind=356a19 effects=5d01a0 damage_or_effect=fc30e9 tooltip_formula=719b28 visual=06be19 icon=9c415d used_by=9fc538 -->
|  |  |
|---|---|
|  | ![Final blow](wiki/assets/skills/20260.png) |
| **Skill id** | `20260` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 10 HP % |
| **Cooldown** | 110 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 458 `데스헤드_결정타` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 55 |

### Tooltip

> [Active] Attacks the designated target and deals `{EF_STATIC 120}``{EF_R_DAM 100}`damage. The damage is increased by 6% of your target's maximum health. Heal yourself for 55% of the damage dealt.

Tooltip formula: **120 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 131 | stat? Health(%) | 6 | 1 |
| 4 | 43 | stat? Spell Vamp(%) | 55 | 0 |

**Reading:** amount **120 + 100% Attack**; damage (physical?).

### Used by

- Weapon skill **hero set 4** of WeaponBase 75: [[wiki/items/8006-king-deathhead|King Deathhead]], [[wiki/items/8506-crystal-king-deathhead|Crystal : King Deathhead]]
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
