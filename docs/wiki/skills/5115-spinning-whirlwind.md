---
title: "Spinning Whirlwind"
type: "skill"
id: 5115
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5115", "client: StringAll_Eng SkillComment_5115 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5115"
desc_key: "SkillComment_5115"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 100, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 256
icon: {"file": "Skill_Miriam_01.png", "index": 15}
used_by:
  - {"weapon_base": 26, "slot": 4, "items": [15004]}
---
<!-- generated:start -->
<!-- generated-keys: title=e25c22 type=86a754 id=d1c43a sources=65c1a5 name_key=868036 desc_key=c7ff15 kind=356a19 kind_name=9bc378 target=9dc90e range=1b6453 area=6d01a6 cost=9e049c cooldown=7d0c8c effect_kind=356a19 effects=7e5020 damage_or_effect=0d617f tooltip_formula=8572b2 visual=dd7c1a icon=1b8eb2 used_by=f86694 -->
|  |  |
|---|---|
|  | ![Spinning Whirlwind](../assets/skills/5115.png) |
| **Skill id** | `5115` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 256 `PCM_Bow_04_R 회전회오리` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 15 |

### Tooltip

> [Active] Deals `{EF_STATIC 100}``{EF_R_DAM 90}` Damage to all enemies around you.

Tooltip formula: **100 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **100 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **R** of WeaponBase 26: [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill R of Magical Frost Bow (item 15004), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
