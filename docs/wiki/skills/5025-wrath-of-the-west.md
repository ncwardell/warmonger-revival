---
title: "Wrath of the West"
type: "skill"
id: 5025
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5025", "client: StringAll_Eng SkillComment_5025 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420/0426 (R multipliers)"]
name_key: "Skill_5025"
desc_key: "SkillComment_5025"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 4.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 129, "value": 30, "rate": 1}
damage_or_effect: {"kind": "damage (magic?)", "base": 120}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 130}
visual: 180
icon: {"file": "Skill_Einsel_01.png", "index": 27}
used_by:
  - {"weapon_base": 18, "slot": 4, "items": [10017]}
---
<!-- generated:start -->
<!-- generated-keys: title=9ac475 type=86a754 id=ac6075 sources=a43406 name_key=7d2e07 desc_key=cbba92 kind=356a19 kind_name=9bc378 target=e84f24 range=1b6453 area=3e9947 cost=ff5a60 cooldown=ad2ac8 delivery=93a212 effect_kind=da4b92 effects=69769b damage_or_effect=f69851 tooltip_formula=79cd88 visual=ec7f1f icon=251b00 used_by=865c34 -->
|  |  |
|---|---|
|  | ![Wrath of the West](../assets/skills/5025.png) |
| **Skill id** | `5025` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | line / rectangle?, radius 4, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 180 `PCE_Knife_02__R_서풍의 진노` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 27 |

### Tooltip

> [Active]The sword of the western wind gets the power of the wind and deals magic damage to the target on the straight line with `{EF_STATIC 130}`.The additional magical damage that is equal to 30% of the enemy's lost stamina.

Tooltip formula: **130** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 129 | % of the target's missing HP? (5025 tooltip: 30 = '30% of the enemy's lost stamina') | 30 | 1 |

**Reading:** amount **120**; damage (magic?).

> [!warning] The tooltip (130) and the effect slots (120) disagree; one of them was out of date in the shipped client.

### Used by

- Weapon skill **R** of WeaponBase 18: [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
<!-- generated:end -->

## Notes

- Skill R of Magical Wrath Blade (item 10017), one of the Saint's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) cut Magical Wrath Blade's R AP multiplier 120 → 100 and its HP multiplier 30 → 20; [WM 0426](https://steamcommunity.com/games/718790/announcements/detail/2394103650887775295) made the R base damage no longer scale with AP. The client tooltip is a flat 130 plus 30 % of the enemy's lost HP, so it has the 0426 change but still says 30 %. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1, [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- Lost-HP part: WM 0420 says 30 → 20; the client tooltip still says 30 %. The page keeps the client value until play shows otherwise.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
