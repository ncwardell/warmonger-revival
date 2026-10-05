---
title: "Rune of Flames"
type: "skill"
id: 801
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 801"]
name_key: "Skill_801"
desc_key: "SkillComment_801"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 0}
  - {"slot": 2, "type": 131, "value": 25, "rate": 1}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "stats": [{"code": 131, "value": 25}]}
visual: 228
icon: {"file": "Skill_Hunter_BlazeArrow.png", "index": 0}
used_by:
  - {"item_use": 801}
  - {"item_use": 2904}
---
<!-- generated:start -->
<!-- generated-keys: title=06c021 type=86a754 id=549843 sources=2d6352 name_key=74c554 desc_key=902b0d kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=f78559 damage_or_effect=1e7ff4 visual=cad06f icon=3a349a used_by=4e16f9 -->
|  |  |
|---|---|
| **Skill id** | `801` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 228 `화염룬` |
| **Icon** | `ui/icons/Skill_Hunter_BlazeArrow.png` cell 0 |

### Tooltip

> Amplification

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 0 |
| 2 | 131 | stat? Health(%) | 25 | 1 |

**Reading:** amount **100**; damage (magic?).

### Used by

- Cast when [[wiki/items/801-rune-of-flame|Rune of Flame]] is used (Item_Base option 210)
- Cast when [[wiki/items/2904-amplification|Amplification]] is used (Item_Base option 210)
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
