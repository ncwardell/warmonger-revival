---
title: "Overcharge"
type: "skill"
id: 20004
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20004", "client: StringAll_Eng SkillComment_5181 (tooltip value tags)"]
name_key: "Skill_5181"
desc_key: "SkillComment_5181"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 90}
cooldown: {"ms": 10000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 318
icon: {"file": "Policy.png", "index": 35}
used_by:
  - {"weapon_base": 69, "slot": 1, "items": [8000, 8500]}
---
<!-- generated:start -->
<!-- generated-keys: title=e607a4 type=86a754 id=988020 sources=247651 name_key=0fa0c8 desc_key=d7bd4e kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=da6e22 cooldown=4aa5a5 movement=5f1488 effect_kind=356a19 effects=14fb0f damage_or_effect=f8f6f9 tooltip_formula=74c011 visual=154a31 icon=64fa61 used_by=0d74e4 -->
|  |  |
|---|---|
|  | ![Overcharge](wiki/assets/skills/20004.png) |
| **Skill id** | `20004` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 90 MP |
| **Cooldown** | 10 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 318 `Skeleton_King_변신스킬_01_차징` |
| **Icon** | `ui/icons/Policy.png` cell 35 |

### Tooltip

> [Active] Dash to the targeted location and deal `{EF_STATIC 75}``{EF_R_DAM 80}` damage.

Tooltip formula: **75 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |

**Reading:** amount **75 + 80% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 69: [[wiki/items/8000-dark-knight-skull|Dark knight Skull]], [[wiki/items/8500-crystal-dark-knight-skull|Crystal : Dark knight Skull]]

### Mentioned in

- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Hero form (Dark Knight Skull) (line 53): Hero · Dark Knight Skull: the new R skill is Heaven and Earth 20006, which is weapon 69 (item 8000 "Dark knight Skull"; HeroData 1). Hero skills on that weap...
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
