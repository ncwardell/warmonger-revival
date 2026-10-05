---
title: "Sharp Edges"
type: "skill"
id: 5112
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5112", "client: StringAll_Eng SkillComment_5112 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5112"
desc_key: "SkillComment_5112"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10111, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 10111, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 253
icon: {"file": "Skill_Miriam_01.png", "index": 12}
used_by:
  - {"weapon_base": 26, "slot": 1, "items": [15004]}
---
<!-- generated:start -->
<!-- generated-keys: title=fc9661 type=86a754 id=b3138e sources=58e653 name_key=dab589 desc_key=b237f7 kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=8b4fa7 cooldown=0156ad delivery=93a212 effect_kind=356a19 effects=a09cf2 damage_or_effect=f9638b tooltip_formula=4709a0 visual=4c15dc icon=5a5175 used_by=ee5578 -->
|  |  |
|---|---|
|  | ![Sharp Edges](wiki/assets/skills/5112.png) |
| **Skill id** | `5112` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 253 `PCM_Bow_04_Q 날카로운상처` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 12 |

### Tooltip

> [Active] Inflicts a bleeding wound that deals `{EF_STATIC 80}``{EF_R_DAM 80}` Damage. Lasts  for 3 seconds.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10111-sharp-edges-bleeds-for-3-seconds\|Sharp Edges : Bleeds for 3 seconds]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10111-sharp-edges-bleeds-for-3-seconds|Sharp Edges : Bleeds for 3 seconds]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 26: [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill Q of Magical Frost Bow (item 15004), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

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
