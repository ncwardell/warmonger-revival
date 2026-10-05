---
title: "Poisonous Swamp"
type: "skill"
id: 5028
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5028", "client: StringAll_Eng SkillComment_5028 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0426 (E debuff 10% → 20%; matches client tooltip)"]
name_key: "Skill_5028"
desc_key: "SkillComment_5028"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
delivery: {"type": 4, "field_tick": 0.1}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 101, "value": 20, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10027, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 60, "attack_pct": 20, "buffs": [{"buff": 10027, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_DAM", "value": 20}
visual: 83
icon: {"file": "Skill_Miriam_01.png", "index": 18}
used_by:
  - {"weapon_base": 29, "slot": 3, "items": [15007]}
---
<!-- generated:start -->
<!-- generated-keys: title=3e271c type=86a754 id=b68969 sources=a118e5 name_key=7d0edd desc_key=da9fcf kind=356a19 kind_name=9bc378 target=e84f24 range=ac3478 area=e8b0ea cost=911ade cooldown=628d31 delivery=8af2f4 effect_kind=da4b92 effects=546ce8 damage_or_effect=faed5f tooltip_formula=c9bdad visual=7d7116 icon=90d3d6 used_by=3cf339 -->
|  |  |
|---|---|
|  | ![Poisonous Swamp](wiki/assets/skills/5028.png) |
| **Skill id** | `5028` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Delivery** | projectile / SFX (4), tick 0.1 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 83 `PCM_Knife_01_E_맹독의 늪` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 18 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 60}``{EF_R_DAM 20}` Damage to all enemies standing in it. Reduces Armor and Magic Resistance by 20% for 5 seconds.

Tooltip formula: **60 + 20% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 20 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10027-deadly-poisonous-swamp-reduced-armor-and-magic-resistance\|Deadly Poisonous Swamp : Reduced Armor and Magic Resistance]] | 100 |

**Reading:** amount **60 + 20% Attack**; damage (magic?); applies [[wiki/buffs/10027-deadly-poisonous-swamp-reduced-armor-and-magic-resistance|Deadly Poisonous Swamp : Reduced Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 29: [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill E of Magical judge Dagger (item 15007), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Patch history: [WM 0426](https://steamcommunity.com/games/718790/announcements/detail/2394103650887775295) raised Magical Judge Dagger's E armor/MR debuff 10 % → 20 %; the client tooltip says 20 %. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
