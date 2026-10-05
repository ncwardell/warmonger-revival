---
title: "Howl of Victory"
type: "skill"
id: 5069
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5069", "client: StringAll_Eng SkillComment_5069 (tooltip value tags)"]
name_key: "Skill_5069"
desc_key: "SkillComment_5069"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 0
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 50, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10060, "rate": 100}
  - {"slot": 4, "type": 131, "value": 1, "rate": 0}
damage_or_effect: {"kind": "heal HP", "base": 80, "ability_pct": 50, "buffs": [{"buff": 10060, "rate": 100}], "stats": [{"code": 131, "value": 1}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 50}
visual: 74
icon: {"file": "Skill_Dolorece_01.png", "index": 14}
used_by:
  - {"weapon_base": 45, "slot": 3, "items": [20003]}
---
<!-- generated:start -->
<!-- generated-keys: title=68d82e type=86a754 id=9639c6 sources=ba9b09 name_key=9560b7 desc_key=29e423 kind=356a19 kind_name=9bc378 target=55b685 range=b6589f area=e9876d cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=febcbd damage_or_effect=55dc3a tooltip_formula=8e1eb8 visual=1f1362 icon=384e30 used_by=f3d059 -->
|  |  |
|---|---|
|  | ![Howl of Victory](wiki/assets/skills/5069.png) |
| **Skill id** | `5069` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 0 (world units) |
| **Area** | circle, radius 6, width/angle 0 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 74 `PCD_Hammer_04_E_승리의 포효` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 14 |

### Tooltip

> [Active] Heals all nearby party for `{EF_STATIC 80}``{EF_R_MDAM 50}`. The damage is increased by 1% of your target's maximum health. Increases your Health Regeneration by 20% for 8 seconds

Tooltip formula: **80 + 50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 50 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10060-howl-of-victory-increased-hp-regeneration\|Howl of Victory: Increased HP Regeneration]] | 100 |
| 4 | 131 | stat? Health(%) | 1 | 0 |

**Reading:** amount **80 + 50% Ability Power**; heal HP; applies [[wiki/buffs/10060-howl-of-victory-increased-hp-regeneration|Howl of Victory: Increased HP Regeneration]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 45: [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/20003-magical-crush-hammer|Magical Crush Hammer]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 36): Guardian · 20001 Magical Demolition Hammer (Mace) · 20021 Magical Protect Cannon (Cannon) · 20003 Magical Crush Hammer (no label string) · 43: Soul Infestati...
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
