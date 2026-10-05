---
title: "Might of Thunder God"
type: "skill"
id: 5007
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5007", "client: StringAll_Eng SkillComment_5007 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0412 (cooldown 70 → 60 s, note says E)"]
name_key: "Skill_5007"
desc_key: "SkillComment_5007"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 4, "field_tick": 0.9}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 130, "rate": 100}
  - {"slot": 2, "type": 102, "value": 120, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10007, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 130, "ability_pct": 120, "buffs": [{"buff": 10007, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 130}
  - {"tag": "EF_R_MDAM", "value": 120}
visual: 106
icon: {"file": "Skill_Einsel_01.png", "index": 7}
used_by:
  - {"weapon_base": 2, "slot": 4, "items": [10001]}
---
<!-- generated:start -->
<!-- generated-keys: title=bf802b type=86a754 id=e30861 sources=0b7ae9 name_key=4692f4 desc_key=b0a71e kind=356a19 kind_name=9bc378 target=138a60 range=902ba3 area=6d01a6 cost=ff5a60 cooldown=7d0c8c delivery=4fe5f3 effect_kind=da4b92 effects=3cbe0e damage_or_effect=73d944 tooltip_formula=9f723b visual=7224f9 icon=62f758 used_by=6786d7 -->
|  |  |
|---|---|
|  | ![Might of Thunder God](../assets/skills/5007.png) |
| **Skill id** | `5007` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 12 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 390 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX (4), tick 0.9 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 106 `PCE_Staff_02_R_뇌전 작렬` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 7 |

### Tooltip

> [Active] Thunderbolts fall down at the targeted area, inflicting `{EF_STATIC 130}``{EF_R_MDAM 120}` damage. All targets that are hit are stunned for 2 seconds.

Tooltip formula: **130 + 120% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 130 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 120 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10007-might-of-the-thunder-god-stunned-for-2-seconds\|Might of the Thunder God : Stunned for 2 seconds]] | 100 |

**Reading:** amount **130 + 120% Ability Power**; damage (magic?); applies [[wiki/buffs/10007-might-of-the-thunder-god-stunned-for-2-seconds|Might of the Thunder God : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 2: [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 93): 0412 · Magical Thunder Wand (10001) · Q AP base 70 → 80; W 90 → 100; "E" cooldown 70 → 60 s (in the client the 60 s skill is the R, Might of Thunder God, ski...
<!-- generated:end -->

## Notes

- Skill R of Magical Thunder Wand (item 10001), one of the Saint's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Patch history: [WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359) cut a Magical Thunder Wand cooldown 70 → 60 s. The note calls it the "E", but in the client the 60 s skill is this R. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1, [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
