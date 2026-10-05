---
title: "Mark of Death"
type: "skill"
id: 5046
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5046"]
name_key: "Skill_5046"
desc_key: "SkillComment_5046"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 11
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 314, "value": 10042, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10042, "rate": 100}]}
visual: 195
icon: {"file": "Skill_Miriam_01.png", "index": 6}
used_by:
  - {"weapon_base": 23, "slot": 3, "items": [15001]}
---
<!-- generated:start -->
<!-- generated-keys: title=832dcc type=86a754 id=7840f8 sources=c14572 name_key=5c9396 desc_key=5dfcb5 kind=356a19 kind_name=9bc378 target=069ef3 range=17ba07 cost=da6e22 cooldown=4aa5a5 effect_kind=356a19 effects=f177bb damage_or_effect=b6ffee visual=752ae7 icon=c3bc1a used_by=2099a3 -->
|  |  |
|---|---|
|  | ![Mark of Death](../assets/skills/5046.png) |
| **Skill id** | `5046` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 11 (world units) |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 195 `PCM_Bow_02_E 목표설정` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 6 |

### Tooltip

> [Active] Marks an enemy and decreases their Armor by 20%.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10042-mark-of-death-reduced-armor\|Mark of Death : Reduced Armor]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10042-mark-of-death-reduced-armor|Mark of Death : Reduced Armor]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 23: [[wiki/items/15001-magical-sniping-bow|Magical Sniping Bow]]
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
