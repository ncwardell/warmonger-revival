---
title: "Shadow Walk"
type: "skill"
id: 5027
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5027", "client: StringAll_Eng SkillComment_5027 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)"]
name_key: "Skill_5027"
desc_key: "SkillComment_5027"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 317, "value": 10023, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10028, "rate": 100}
  - {"slot": 4, "type": 301, "value": 10142, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10023, "rate": 100}, {"buff": 10028, "rate": 100}, {"buff": 10142, "rate": 100}], "attack_pct": 100}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 45}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 82
icon: {"file": "Skill_Miriam_01.png", "index": 17}
used_by:
  - {"weapon_base": 29, "slot": 2, "items": [15007]}
---
<!-- generated:start -->
<!-- generated-keys: title=112228 type=86a754 id=67b1a8 sources=a10a88 name_key=aa9b7a desc_key=13d7d3 kind=356a19 kind_name=9bc378 target=53cfaf range=902ba3 cost=060055 cooldown=5b7687 movement=953fcf effect_kind=356a19 effects=d2eb9d damage_or_effect=6004cd tooltip_formula=bcf431 visual=76546f icon=67ccf4 used_by=edd796 -->
|  |  |
|---|---|
|  | ![Shadow Walk](../assets/skills/5027.png) |
| **Skill id** | `5027` |
| **Kind** | active (1) |
| **Target** | unit; ally, enemy; units: monster, player; up to 2 |
| **Range** | 7 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 82 `PCM_Knife_01_W_그림자 밟기` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 17 |

### Tooltip

> [Active] You jump your target out of the shadows, silencing it for 2 seconds. You gain a 350 Absorbtion Shield. Your next Attack on your victim deals `{EF_STATIC 45}``{EF_R_DAM 70}`. The Damage is increased by 2%.

Tooltip formula: **45 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/10023-shadow-walk-creates-a-shield-that-absorbs-damage-for-10-seco\|Shadow Walk: Creates a shield that absorbs Damage for 10 seconds.]] | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10028-shadow-walk-silenced-for-2-seconds\|Shadow Walk : Silenced for 2 seconds]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10142-shadow-walk-your-next-attack-deals-bonus-damage\|Shadow Walk : Your next Attack deals bonus damage]] | 100 |

**Reading:** amount **100% Attack**; damage (physical?); applies [[wiki/buffs/10023-shadow-walk-creates-a-shield-that-absorbs-damage-for-10-seco|Shadow Walk: Creates a shield that absorbs Damage for 10 seconds.]] (100%); applies [[wiki/buffs/10028-shadow-walk-silenced-for-2-seconds|Shadow Walk : Silenced for 2 seconds]] (100%); applies [[wiki/buffs/10142-shadow-walk-your-next-attack-deals-bonus-damage|Shadow Walk : Your next Attack deals bonus damage]] (100%).

> [!warning] The tooltip (45 + 70% Attack) and the effect slots (100% Attack) disagree; one of them was out of date in the shipped client.

### Used by

- Weapon skill **W** of WeaponBase 29: [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/15007-magical-judge-dagger|Magical judge Dagger]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill W of Magical judge Dagger (item 15007), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*

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
