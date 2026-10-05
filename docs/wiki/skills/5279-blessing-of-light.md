---
title: "Blessing of Light"
type: "skill"
id: 5279
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5279", "client: StringAll_Eng SkillComment_5279 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420 (W AP 80 → 60)"]
name_key: "Skill_5279"
desc_key: "SkillComment_5279"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 50, "rate": 0}
damage_or_effect: {"kind": "heal HP", "base": 80, "ability_pct": 50}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 50}
visual: 364
icon: {"file": "Skill_Einsel_01.png", "index": 9}
used_by:
  - {"weapon_base": 64, "slot": 2, "items": [10002]}
---
<!-- generated:start -->
<!-- generated-keys: title=2cbe2e type=86a754 id=c718f1 sources=572e44 name_key=cb8f1a desc_key=5a768c kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=e4e7cf cooldown=e3989d effect_kind=632667 effects=220f5e damage_or_effect=9570ea tooltip_formula=8e1eb8 visual=56e43a icon=aaa141 used_by=0f3585 -->
|  |  |
|---|---|
|  | ![Blessing of Light](wiki/assets/skills/5279.png) |
| **Skill id** | `5279` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 364 `시즌1_PCE_Staff_03_W_소생의 숨결` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 9 |

### Tooltip

> [Active] Heal the target with `{EF_STATIC 80}``{EF_R_MDAM 50}`

Tooltip formula: **80 + 50% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 50 | 0 |

**Reading:** amount **80 + 50% Ability Power**; heal HP.

### Used by

- Weapon skill **W** of WeaponBase 64: [[wiki/items/10002-magical-life-wand|Magical Life Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/10002-magical-life-wand|Magical Life Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
<!-- generated:end -->

## Notes

- Skill W of Magical Life Wand (item 10002), one of the Saint's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) cut Magical Life Wand's W AP multiplier 80 → 60. The client tooltip reads 50 % AP (10279: 55 %). ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1, [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- AP multiplier: WM 0420 gives 60 %; the client tooltip gives 50 % (55 % on 10279). Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
