---
title: "Bloody Revenge"
type: "skill"
id: 10055
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10055", "client: StringAll_Eng SkillComment_10055 (tooltip value tags)"]
name_key: "Skill_10055"
desc_key: "SkillComment_10055"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 80}
cooldown: {"ms": 8000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
  - {"slot": 3, "type": 43, "value": 25, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90, "stats": [{"code": 43, "value": 25}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 107
icon: {"file": "Skill_Miriam_01.png", "index": 20}
used_by:
  - {"weapon_base": 128, "slot": 1, "items": [16006]}
---
<!-- generated:start -->
<!-- generated-keys: title=e2f921 type=86a754 id=461344 sources=986dbb name_key=a35187 desc_key=3d885e kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=e01d1d cooldown=9ded33 effect_kind=356a19 effects=c2d7d4 damage_or_effect=9f7358 tooltip_formula=0fc93d visual=524e05 icon=590769 used_by=13eada -->
|  |  |
|---|---|
|  | ![Bloody Revenge](wiki/assets/skills/10055.png) |
| **Skill id** | `10055` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 80 MP |
| **Cooldown** | 8 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 107 `PCM_Knife_02_Q_피의 보복` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 20 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 90}` Damage. Heal yourself with 25% of the Damage dealt.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |
| 3 | 43 | stat? Spell Vamp(%) | 25 | 0 |

**Reading:** amount **80 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 128: [[wiki/items/16006-magical-blood-dagger|Magical Blood Dagger]]
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
