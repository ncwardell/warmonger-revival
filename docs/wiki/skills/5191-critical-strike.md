---
title: "Critical Strike"
type: "skill"
id: 5191
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5191", "client: StringAll_Eng SkillComment_5191 (tooltip value tags)"]
name_key: "Skill_5191"
desc_key: "SkillComment_5191"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 4
cost: {"type": 4, "type_name": "HP %", "amount": 11}
cooldown: {"ms": 100000, "group": 0}
effect_kind: 15
effects:
  - {"slot": 1, "type": 330, "value": 400, "rate": 100}
  - {"slot": 2, "type": 132, "value": 10, "rate": 1}
damage_or_effect: {"kind": "effect kind 15", "base": 400, "stats": [{"code": 132, "value": 10}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 400}
visual: 328
icon: {"file": "Skill_Boss_01.dds", "index": 3}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=291e77 type=86a754 id=8be703 sources=075994 name_key=812bb3 desc_key=5a6a65 kind=356a19 kind_name=9bc378 target=069ef3 range=1b6453 cost=cf76b6 cooldown=4ae204 effect_kind=f1abd6 effects=b649f2 damage_or_effect=67c861 tooltip_formula=664d4b visual=5547f6 icon=596634 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Critical Strike](wiki/assets/skills/5191.png) |
| **Skill id** | `5191` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 4 (world units) |
| **Cost** | 11 HP % |
| **Cooldown** | 100 s |
| **Effect kind** | ? (15) |
| **Visual** | skillVisual 328 `수호신장_변신스킬_04_혼신의 일격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 3 |

### Tooltip

> [Active] Deal `{EF_STATIC 400}` damage. The damage gets increased by 10% of the enemy's maximum health.

Tooltip formula: **400** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 400 | 100 |
| 2 | 132 | stat? Health Regeneration(%) | 10 | 1 |

**Reading:** amount **400**; effect kind 15.

### Mentioned in

- [[gameplay/gear-stats|Gear stats (Crush Online artifacts)]] § 5. Crafting costs of the special artifacts (forum) (line 211): Gloves of Ghost · 6,100 · B-grade Ultimate Gloves + 53 Black Crystals + 10 Amplifying spell stones (200 gold medals). Ultimate Gloves = Last Gloves + Thorns...
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 1. Rune upgrade materials (final, from 20 Sep 2018) (line 18): - Tier 2: Armor Penetration, Magic Resist Penetration, Life Steal, Spell Vamp, Movement (%), Cooldown Reduction, Critical Strike (%).
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 1. Rune upgrade materials (final, from 20 Sep 2018) (line 19): - Tier 3: Armor Penetration (%), Magic Resist Penetration (%), PvP Attack, PvP Armor, Critical Strike Damage.
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]] § Set bonuses (line 60): 8 · Attack +20, Life Steal +8 %, Critical Strike +5 % · 1, 41, 109 · Armor +50, Magic Resist +50
- [[gameplay/skull-artifact-set|Skull artifact set tooltips (Crush Online, Feb 2017)]] § Set bonuses (line 62): - Crush Online numbers image img A, img B. Option codes client: the tooltip's own wording ("AttackSpeed(%)", "Life Steal(%)", "Critical Strike +(%)") matches...
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Player stats (Arslan Guardian, Magical Demolition Hammer) (line 103, at 5:40): Character sheet at level 2 (5:40): Nation Arslan, Legion –, Class Guardian, Rank Novice, Fame 0, Arena 0 P; HP 530 (regen 44), MP 725 (regen 7), Attack 89, A...
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
