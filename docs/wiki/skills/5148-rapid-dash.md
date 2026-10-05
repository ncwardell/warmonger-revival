---
title: "Rapid Dash"
type: "skill"
id: 5148
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5148", "client: StringAll_Eng SkillComment_5148 (tooltip value tags)"]
name_key: "Skill_5148"
desc_key: "SkillComment_5148"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
movement: "dash"
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10173, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10174, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10173, "rate": 100}, {"buff": 10174, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 291
icon: {"file": "Skill_Einsel_01.png", "index": 30}
used_by:
  - {"weapon_base": 15, "slot": 3, "items": [10014]}
---
<!-- generated:start -->
<!-- generated-keys: title=1679a3 type=86a754 id=1e5922 sources=77cf05 name_key=882cd6 desc_key=aa9af5 kind=356a19 kind_name=9bc378 target=cacd0a range=ac3478 cost=911ade cooldown=628d31 movement=5f1488 effect_kind=da4b92 effects=377868 damage_or_effect=467a00 tooltip_formula=47a1d3 visual=371786 icon=4bb647 used_by=bb82e8 -->
|  |  |
|---|---|
|  | ![Rapid Dash](../assets/skills/5148.png) |
| **Skill id** | `5148` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Movement** | dash |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 291 `PCE_Gun_05_E_빠른 대쉬` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 30 |

### Tooltip

> [Active] You can dash to forward. And after dash normal attack has `{EF_STATIC 10}``{EF_R_DAM 80}` damage. Deals 3% of the target's health as bonus damage. You gain increased Attack Speed and Damage for 8 seconds.

Tooltip formula: **10 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10173-rapid-dash-increased-damage\|Rapid Dash : Increased damage]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10174-rapid-dash-increased-attack-speed\|Rapid Dash : Increased Attack Speed]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10173-rapid-dash-increased-damage|Rapid Dash : Increased damage]] (100%); applies [[wiki/buffs/10174-rapid-dash-increased-attack-speed|Rapid Dash : Increased Attack Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 15: [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]]

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 96): Client check: Skill_Base cooldowns are Soul Infestation 19 s (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail o...
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
