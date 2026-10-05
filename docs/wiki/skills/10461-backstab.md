---
title: "Backstab"
type: "skill"
id: 10461
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10461", "client: StringAll_Eng SkillComment_10461 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420 (Q cooldown 15 → 19 s)"]
name_key: "Skill_10461"
desc_key: "SkillComment_10461"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 30421, "rate": 100}
  - {"slot": 2, "type": 301, "value": 30422, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 30421, "rate": 100}, {"buff": 30422, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 105}
visual: 466
icon: {"file": "Skill_Miriam_01.png", "index": 29}
used_by:
  - {"weapon_base": 130, "slot": 1, "items": [16008]}
---
<!-- generated:start -->
<!-- generated-keys: title=982e1b type=86a754 id=f2c5e8 sources=fd4e39 name_key=96bca3 desc_key=52cac2 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=628d31 effect_kind=356a19 effects=19956e damage_or_effect=c27a5d tooltip_formula=4d8780 visual=cf2f32 icon=c0fb59 used_by=aa0fb9 -->
|  |  |
|---|---|
|  | ![Backstab](../assets/skills/10461.png) |
| **Skill id** | `10461` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 466 `마력의 은신 대거_은신술_시전` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 29 |

### Tooltip

> [Active] Your Movement Speed is increased. Inflicts `{EF_STATIC 10}``{EF_R_DAM 105}` Damage during a basic attack. Reduces Movement Speed of all hit targets.

Tooltip formula: **10 + 105% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30421-backstab-increase-movement-speed\|Backstab : Increase movement speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/30422-backstab-your-basic-attacks-deal-additional-damage\|Backstab : Your basic Attacks deal additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/30421-backstab-increase-movement-speed|Backstab : Increase movement speed]] (100%); applies [[wiki/buffs/30422-backstab-your-basic-attacks-deal-additional-damage|Backstab : Your basic Attacks deal additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 130: [[wiki/items/16008-magical-hiding-dagger|Magical hiding Dagger]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 97): 0420 · Magical Hiding Dagger (15008) · Q cooldown 15 → 19 s, W 20 → 25 s (client: Backstab 20 s, Deception 25 s)
<!-- generated:end -->

## Notes

- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) raised Magical Hiding Dagger (15008)'s Q cooldown 15 → 19 s. The client has Backstab at 20 s. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- Cooldown: WM 0420 gives 19 s; the client has 20 s. Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
