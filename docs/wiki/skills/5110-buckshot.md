---
title: "Buckshot"
type: "skill"
id: 5110
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5110", "client: StringAll_Eng SkillComment_5110 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5110"
desc_key: "SkillComment_5110"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 10
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 247
icon: {"file": "Skill_Dolorece_01.png", "index": 18}
used_by:
  - {"weapon_base": 63, "slot": 3, "items": [20021]}
---
<!-- generated:start -->
<!-- generated-keys: title=79454d type=86a754 id=18e25c sources=d3171f name_key=87b96b desc_key=38a563 kind=356a19 kind_name=9bc378 target=138a60 range=b1d578 cost=e4e7cf cooldown=e3989d delivery=93a212 effect_kind=356a19 effects=36db75 damage_or_effect=0a50cc tooltip_formula=4709a0 visual=b4ef7d icon=54219d used_by=1d47d9 -->
|  |  |
|---|---|
|  | ![Buckshot](../assets/skills/5110.png) |
| **Skill id** | `5110` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 12 |
| **Range** | 10 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 247 `PCD_Cannon_01_E 산탄 발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 18 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 80}` Damage to all enemies hit.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |

**Reading:** amount **80 + 80% Attack**; damage (physical?).

### Used by

- Weapon skill **E** of WeaponBase 63: [[wiki/items/20021-magical-protect-cannon|Magical Protect Cannon]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/20021-magical-protect-cannon|Magical Protect Cannon]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
<!-- generated:end -->

## Notes

- Skill E of Magical Protect Cannon (item 20021), one of the Guardian's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

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
