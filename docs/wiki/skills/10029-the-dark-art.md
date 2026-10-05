---
title: "The Dark Art"
type: "skill"
id: 10029
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10029", "client: StringAll_Eng SkillComment_10029 (tooltip value tags)"]
name_key: "Skill_10029"
desc_key: "SkillComment_10029"
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
  - {"slot": 2, "type": 101, "value": 75, "rate": 0}
  - {"slot": 3, "type": 308, "value": 30024, "rate": 100}
  - {"slot": 4, "type": 301, "value": 30022, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 75, "buffs": [{"buff": 30024, "rate": 100}, {"buff": 30022, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 75}
requirements:
  - {"type": 30022, "a": 5, "b": 10030}
visual: 84
icon: {"file": "Skill_Miriam_01.png", "index": 19}
used_by:
  - {"weapon_base": 129, "slot": 4, "items": [16007]}
---
<!-- generated:start -->
<!-- generated-keys: title=9a9dcc type=86a754 id=38d0a0 sources=7407cb name_key=39c416 desc_key=4fad68 kind=356a19 kind_name=9bc378 target=f3d46d range=902ba3 cost=9e049c cooldown=7d0c8c movement=953fcf effect_kind=356a19 effects=d3cbbe damage_or_effect=0806d2 tooltip_formula=d9a0c2 requirements=7863fc visual=be461a icon=fdf9b8 used_by=42d45b -->
|  |  |
|---|---|
|  | ![The Dark Art](wiki/assets/skills/10029.png) |
| **Skill id** | `10029` |
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

> [Active] You approach your target rapidly and strike it, dealing `{EF_STATIC 80}``{EF_R_DAM 75}` Damage and gain an 300 Absorbtion Shield. Another devastating blow follows the initial attack.

Tooltip formula: **80 + 75% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 75 | 0 |
| 3 | 308 | applies buff (variant 308) | [[wiki/buffs/30024-the-dark-art-creates-a-shield-that-absorbs-damage-for-10-sec\|The Dark Art: Creates a shield that absorbs Damage for 10 seconds.]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/30022-you-prepare-your-next-attack\|You prepare your next Attack]] | 100 |

**Reading:** amount **80 + 75% Attack**; damage (physical?); applies [[wiki/buffs/30024-the-dark-art-creates-a-shield-that-absorbs-damage-for-10-sec|The Dark Art: Creates a shield that absorbs Damage for 10 seconds.]] (100%); applies [[wiki/buffs/30022-you-prepare-your-next-attack|You prepare your next Attack]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 30022 | 5 | 10030 |

### Used by

- Weapon skill **R** of WeaponBase 129: [[wiki/items/16007-magical-judge-dagger|Magical judge Dagger]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
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
