---
title: "Feast of Blood"
type: "skill"
id: 5058
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5058", "client: StringAll_Eng SkillComment_5058 (tooltip value tags)"]
name_key: "Skill_5058"
desc_key: "SkillComment_5058"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 131, "value": 6, "rate": 1}
  - {"slot": 4, "type": 43, "value": 40, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 100, "stats": [{"code": 131, "value": 6}, {"code": 43, "value": 40}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 110
icon: {"file": "Skill_Miriam_01.png", "index": 23}
used_by:
  - {"weapon_base": 28, "slot": 4, "items": [15006]}
---
<!-- generated:start -->
<!-- generated-keys: title=2023a8 type=86a754 id=2bcfa8 sources=92fe78 name_key=8884a2 desc_key=200386 kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=9e049c cooldown=7d0c8c effect_kind=356a19 effects=e680ff damage_or_effect=4aa556 tooltip_formula=719b28 visual=5e796e icon=5572b0 used_by=c241f8 -->
|  |  |
|---|---|
|  | ![Feast of Blood](wiki/assets/skills/5058.png) |
| **Skill id** | `5058` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 110 `PCM_Knife_02_R_피의 향연` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 23 |

### Tooltip

> [Active] Attacks the designated target and deals `{EF_STATIC 120}``{EF_R_DAM 100}`damage. The damage is increased by 6% of your target's maximum health. Heal yourself for 40% of the damage dealt.

Tooltip formula: **120 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 131 | stat? Health(%) | 6 | 1 |
| 4 | 43 | stat? Spell Vamp(%) | 40 | 0 |

**Reading:** amount **120 + 100% Attack**; damage (physical?).

### Used by

- Weapon skill **R** of WeaponBase 28: [[wiki/items/15006-magical-blood-dagger|Magical Blood Dagger]]
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
