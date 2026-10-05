---
title: "Heaven and Earth"
type: "skill"
id: 20006
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20006", "client: StringAll_Eng SkillComment_5183 (tooltip value tags)"]
name_key: "Skill_5183"
desc_key: "SkillComment_5183"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 440}
cooldown: {"ms": 80000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 110, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20005, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 110, "attack_pct": 100, "buffs": [{"buff": 20005, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 110}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 320
icon: {"file": "Policy.png", "index": 38}
used_by:
  - {"weapon_base": 69, "slot": 4, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=e89435 type=86a754 id=5fffae sources=6e645f name_key=f9a437 desc_key=996df5 kind=356a19 kind_name=9bc378 target=7056fd range=902ba3 area=bade13 cost=15d513 cooldown=dceb3e delivery=93a212 effect_kind=356a19 effects=816e68 damage_or_effect=8e646d tooltip_formula=1ae4cb visual=7fdec8 icon=a887cd used_by=eacb37 -->
|  |  |
|---|---|
|  | ![Heaven and Earth](wiki/assets/skills/20006.png) |
| **Skill id** | `20006` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 440 MP |
| **Cooldown** | 80 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 320 `Skeleton_King_변신스킬_03_천지개벽` |
| **Icon** | `ui/icons/Policy.png` cell 38 |

### Tooltip

> [Active] Deals `{EF_STATIC 110}``{EF_R_DAM 100}` Damage to all enemies, stunning them for 3 seconds.

Tooltip formula: **110 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 110 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20005-heaven-and-earth-stunned\|Heaven and Earth : Stunned]] | 100 |

**Reading:** amount **110 + 100% Attack**; damage (physical?); applies [[wiki/buffs/20005-heaven-and-earth-stunned|Heaven and Earth : Stunned]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]

### Mentioned in

- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) (line 53): Hero · Dark Knight Skull: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; HeroData 1). Hero skills on that weap...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) (line 59, at 0:02): Heaven and Earth (R) · cooldown 80 s, mana 440; "deals 110 (+3,499) damage to all enemies, stunning them for 3 seconds" · P3 0:02; Skill_Base 20006 (80,000 m...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 142, at 0:02, 31:06): P3 0:02 · 31:06 · Heaven and Earth tooltip
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
