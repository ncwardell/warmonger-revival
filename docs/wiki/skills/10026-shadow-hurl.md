---
title: "Shadow Hurl"
type: "skill"
id: 10026
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10026", "client: StringAll_Eng SkillComment_10026 (tooltip value tags)"]
name_key: "Skill_10026"
desc_key: "SkillComment_10026"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 9
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 8.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 85}
cooldown: {"ms": 9000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 81
icon: {"file": "Skill_Miriam_01.png", "index": 16}
used_by:
  - {"weapon_base": 129, "slot": 1, "items": [16007]}
---
<!-- generated:start -->
<!-- generated-keys: title=a241ca type=86a754 id=dd5415 sources=86f22a name_key=3398e8 desc_key=70778f kind=356a19 kind_name=9bc378 target=aa5d92 range=0ade7c area=38ed23 cost=4921ef cooldown=db479b delivery=93a212 effect_kind=356a19 effects=73cf54 damage_or_effect=bbbb47 tooltip_formula=d94767 visual=1d513c icon=fa0505 used_by=4d41e3 -->
|  |  |
|---|---|
|  | ![Shadow Hurl](../assets/skills/10026.png) |
| **Skill id** | `10026` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 9 (world units) |
| **Area** | line / rectangle?, radius 8, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 85 MP |
| **Cooldown** | 9 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 81 `PCM_Knife_01_Q_그림자 궤적` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 16 |

### Tooltip

> [Active] Hurls a blade out of the shadows towards an enemy, inflicting `{EF_STATIC 70}``{EF_R_DAM 85}` Damage.

Tooltip formula: **70 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |

**Reading:** amount **70 + 85% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 129: [[wiki/items/16007-magical-judge-dagger|Magical judge Dagger]]

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
