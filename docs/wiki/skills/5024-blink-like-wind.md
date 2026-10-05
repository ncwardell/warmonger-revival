---
title: "Blink like wind"
type: "skill"
id: 5024
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5024", "client: StringAll_Eng SkillComment_5024 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0329/0402/0420/0719 (E scaling history)"]
name_key: "Skill_5024"
desc_key: "SkillComment_5024"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 9
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
movement: "blink / teleport"
effect_kind: 2
effects:
  - {"slot": 3, "type": 330, "value": 100, "rate": 100}
  - {"slot": 4, "type": 102, "value": 50, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "ability_pct": 50}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 50}
visual: 179
icon: {"file": "Skill_Einsel_01.png", "index": 26}
used_by:
  - {"weapon_base": 18, "slot": 3, "items": [10017]}
---
<!-- generated:start -->
<!-- generated-keys: title=8a878f type=86a754 id=9c245d sources=35731f name_key=ceffb4 desc_key=c8471b kind=356a19 kind_name=9bc378 target=53cfaf range=0ade7c cost=4e8ae0 cooldown=d1c73e movement=953fcf effect_kind=da4b92 effects=6d22f3 damage_or_effect=22cc6a tooltip_formula=5cbf35 visual=9e44d2 icon=6c8b2c used_by=8a7b3f -->
|  |  |
|---|---|
|  | ![Blink like wind](../assets/skills/5024.png) |
| **Skill id** | `5024` |
| **Kind** | active (1) |
| **Target** | unit; ally, enemy; units: monster, player; up to 2 |
| **Range** | 9 (world units) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 179 `PCE_Knife_02__E_바람의 흔적` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 26 |

### Tooltip

> [Active] Appear next to an enemy and deal `{EF_STATIC 100}``{EF_R_MDAM 50}` Damage.

Tooltip formula: **100 + 50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 3 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 4 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 50 | 0 |

**Reading:** amount **100 + 50% Ability Power**; damage (magic?).

### Used by

- Weapon skill **E** of WeaponBase 18: [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
- `contract/combat.yaml` line 221: `evidence: "Handler and sender read; world.hit_push() live-tested (skill 5024 dash, 10 packets in the 04 Oct log)."`

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 96): Client check: Skill_Base cooldowns are Soul Infestation 19 s (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail o...
<!-- generated:end -->

## Notes

- Skill E of Magical Wrath Blade (item 10017), one of the Saint's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Patch history: [WM 0329](https://steamcommunity.com/games/718790/announcements/detail/2383968106570216224) / [WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018) moved Magical Wrath Blade's E from AD to AP; [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) cut its AP multiplier 120 → 100; [WM 0719](https://steamcommunity.com/games/718790/announcements/detail/2412125660633804214) cut the maximum multiplier at T3 from 1.2 to 0.8 AP. The client tooltip reads 100 + 50 % AP (10024: 55 %). The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
