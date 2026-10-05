---
title: "The Dark Art"
type: "skill"
id: 5029
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5029", "client: StringAll_Eng SkillComment_5029 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5029"
desc_key: "SkillComment_5029"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 308, "value": 10024, "rate": 100}
  - {"slot": 4, "type": 301, "value": 10022, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 70, "buffs": [{"buff": 10024, "rate": 100}, {"buff": 10022, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 70}
requirements:
  - {"type": 10022, "a": 5, "b": 5030}
visual: 84
icon: {"file": "Skill_Miriam_01.png", "index": 19}
used_by:
  - {"weapon_base": 29, "slot": 4, "items": [15007]}
---
<!-- generated:start -->
<!-- generated-keys: title=9a9dcc type=86a754 id=92ed4e sources=ac99cc name_key=ac9902 desc_key=1048e4 kind=356a19 kind_name=9bc378 target=f3d46d range=902ba3 cost=9e049c cooldown=7d0c8c movement=953fcf effect_kind=356a19 effects=634f97 damage_or_effect=d17fbd tooltip_formula=321def requirements=3ba419 visual=be461a icon=fdf9b8 used_by=d7a878 -->
|  |  |
|---|---|
|  | ![The Dark Art](wiki/assets/skills/5029.png) |
| **Skill id** | `5029` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 2 |
| **Range** | 7 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 84 `PCM_Knife_01_R_어둠의 습격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 19 |

### Tooltip

> [Active] You approach your target rapidly and strike it, dealing `{EF_STATIC 80}``{EF_R_DAM 70}` Damage and gain an 300 Absorbtion Shield. Another devastating blow follows the initial attack.

Tooltip formula: **80 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 308 | applies buff (variant 308) | [[wiki/buffs/10024-the-dark-art-creates-a-shield-that-absorbs-damage-for-10-sec\|The Dark Art: Creates a shield that absorbs Damage for 10 seconds.]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10022-you-prepare-your-next-attack\|You prepare your next Attack]] | 100 |

**Reading:** amount **80 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10024-the-dark-art-creates-a-shield-that-absorbs-damage-for-10-sec|The Dark Art: Creates a shield that absorbs Damage for 10 seconds.]] (100%); applies [[wiki/buffs/10022-you-prepare-your-next-attack|You prepare your next Attack]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10022 | 5 | 5030 |

### Used by

- Weapon skill **R** of WeaponBase 29: [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot R for [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill R of Magical judge Dagger (item 15007), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
