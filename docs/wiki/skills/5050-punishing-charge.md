---
title: "Punishing Charge"
type: "skill"
id: 5050
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5050", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0329/0402 (AD to AP)"]
name_key: "Skill_5050"
desc_key: "SkillComment_5050"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 8.0, "width_or_angle": 1.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
movement: "dash"
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 10045, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10045, "rate": 100}]}
requirements:
  - {"type": 10045, "a": 5, "b": 5051}
visual: 171
icon: {"file": "Skill_Einsel_01.png", "index": 21}
used_by:
  - {"weapon_base": 16, "slot": 2, "items": [10015]}
---
<!-- generated:start -->
<!-- generated-keys: title=92808c type=86a754 id=9b248b sources=031cae name_key=ee2b6e desc_key=852a6d kind=356a19 kind_name=9bc378 target=6bbbc3 range=902ba3 area=fbbe31 cost=deac18 cooldown=a93f07 movement=5f1488 effect_kind=b6589f effects=653d1b damage_or_effect=81fcc5 requirements=79f67e visual=94940e icon=83e0e4 used_by=54ee05 -->
|  |  |
|---|---|
|  | ![Punishing Charge](wiki/assets/skills/5050.png) |
| **Skill id** | `5050` |
| **Kind** | active (1) |
| **Target** | ground; self, ally; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 8, width/angle 1 (indicator `stick256x512.png`) |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Movement** | dash |
| **Visual** | skillVisual 171 `PCE_Knife_01_W 돌진 (형벌의 인장: 돌진)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 21 |

### Tooltip

> [Active] Charge to the designated area, enabling you to use Punishing Stomp.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10045-punishing-charge-you-are-able-to-use-punishing-stomp-now\|Punishing Charge : You are able to use Punishing Stomp now]] | 100 |

**Reading:** applies [[wiki/buffs/10045-punishing-charge-you-are-able-to-use-punishing-stomp-now|Punishing Charge : You are able to use Punishing Stomp now]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10045 | 5 | 5051 |

### Used by

- Weapon skill **W** of WeaponBase 16: [[wiki/items/10015-magical-dash-blade|Magical Dash Blade]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0329](https://steamcommunity.com/games/718790/announcements/detail/2383968106570216224) / [WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018) moved Magical Dash Blade's Q and W scaling from AD to AP; the client tooltips use AP (`EF_R_MDAM`) where they have one. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
