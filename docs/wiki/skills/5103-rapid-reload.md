---
title: "Rapid Reload"
type: "skill"
id: 5103
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5103", "client: StringAll_Eng SkillComment_5103 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5103"
desc_key: "SkillComment_5103"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 10085, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10140, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10085, "rate": 100}, {"buff": 10140, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 120}
visual: 241
icon: {"file": "Skill_Einsel_01.png", "index": 17}
used_by:
  - {"weapon_base": 12, "slot": 2, "items": [10011]}
---
<!-- generated:start -->
<!-- generated-keys: title=590afc type=86a754 id=44a1b6 sources=59f22f name_key=4431ac desc_key=a3be8d kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=e3989d effect_kind=b6589f effects=be3ddc damage_or_effect=78c1a4 tooltip_formula=2b234c visual=9ffd1a icon=7c2320 used_by=1a5571 -->
|  |  |
|---|---|
|  | ![Rapid Reload](../assets/skills/5103.png) |
| **Skill id** | `5103` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Visual** | skillVisual 241 `PCE_Gun_01_W` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 17 |

### Tooltip

> [Active] Gain 40% Attack and Movement Speed. Your basic Attacks deal an additional `{EF_STATIC 10}``{EF_R_DAM 120}` Damage for 4 seconds.

Tooltip formula: **10 + 120% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/10085-rapid-reload-gain-improved-attack-and-movement-speed\|Rapid Reload : Gain improved Attack and Movement Speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10140-quick-reload-your-next-basic-attacks-deal-area-damage\|Quick Reload : Your next basic Attacks deal area damage]] | 100 |

**Reading:** applies [[wiki/buffs/10085-rapid-reload-gain-improved-attack-and-movement-speed|Rapid Reload : Gain improved Attack and Movement Speed]] (100%); applies [[wiki/buffs/10140-quick-reload-your-next-basic-attacks-deal-area-damage|Quick Reload : Your next basic Attacks deal area damage]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 12: [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
<!-- generated:end -->

## Notes

- Skill W of Magical adapted Dual Gun (item 10011), one of the Saint's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

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
