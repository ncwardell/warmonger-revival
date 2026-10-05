---
title: "Poisonous Swamp"
type: "skill"
id: 10028
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10028", "client: StringAll_Eng SkillComment_10028 (tooltip value tags)"]
name_key: "Skill_10028"
desc_key: "SkillComment_10028"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 101, "value": 25, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30027, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 60, "attack_pct": 25, "buffs": [{"buff": 30027, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_DAM", "value": 25}
visual: 83
icon: {"file": "Skill_Miriam_01.png", "index": 18}
used_by:
  - {"weapon_base": 129, "slot": 3, "items": [16007]}
---
<!-- generated:start -->
<!-- generated-keys: title=3e271c type=86a754 id=4b48d1 sources=1672e9 name_key=ed838c desc_key=0c0378 kind=356a19 kind_name=9bc378 target=e84f24 range=ac3478 area=e8b0ea cost=911ade cooldown=628d31 delivery=8af2f4 effect_kind=da4b92 effects=89deef damage_or_effect=c4cdbf tooltip_formula=4df6d2 visual=7d7116 icon=90d3d6 used_by=4c72fa -->
|  |  |
|---|---|
|  | ![Poisonous Swamp](wiki/assets/skills/10028.png) |
| **Skill id** | `10028` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 83 `PCM_Knife_01_E_맹독의 늪` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 18 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 60}``{EF_R_DAM 25}` Damage to all enemies standing in it. Reduces Armor and Magic Resistance by 20% for 5 seconds.

Tooltip formula: **60 + 25% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 25 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30027-deadly-poisonous-swamp-reduced-armor-and-magic-resistance\|Deadly Poisonous Swamp : Reduced Armor and Magic Resistance]] | 100 |

**Reading:** amount **60 + 25% Attack**; damage (magic?); applies [[wiki/buffs/30027-deadly-poisonous-swamp-reduced-armor-and-magic-resistance|Deadly Poisonous Swamp : Reduced Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 129: [[wiki/items/16007-magical-judge-dagger|Magical judge Dagger]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
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
