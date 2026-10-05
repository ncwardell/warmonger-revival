---
title: "Shadow Hurl"
type: "skill"
id: 5026
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5026", "client: StringAll_Eng SkillComment_5026 (tooltip value tags)"]
name_key: "Skill_5026"
desc_key: "SkillComment_5026"
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
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 81
icon: {"file": "Skill_Miriam_01.png", "index": 16}
used_by:
  - {"weapon_base": 29, "slot": 1, "items": [15007]}
---
<!-- generated:start -->
<!-- generated-keys: title=a241ca type=86a754 id=124e0f sources=00951a name_key=ed588d desc_key=7b494c kind=356a19 kind_name=9bc378 target=aa5d92 range=0ade7c area=38ed23 cost=4921ef cooldown=db479b delivery=93a212 effect_kind=356a19 effects=9d1073 damage_or_effect=fdf7ab tooltip_formula=4d3643 visual=1d513c icon=fa0505 used_by=309d81 -->
|  |  |
|---|---|
|  | ![Shadow Hurl](../assets/skills/5026.png) |
| **Skill id** | `5026` |
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

> [Active] Hurls a blade out of the shadows towards an enemy, inflicting `{EF_STATIC 70}``{EF_R_DAM 80}` Damage.

Tooltip formula: **70 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |

**Reading:** amount **70 + 80% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 29: [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

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
