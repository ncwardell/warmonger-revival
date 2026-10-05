---
title: "The Dark Art"
type: "skill"
id: 5030
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5030", "client: StringAll_Eng SkillComment_5030 (tooltip value tags)"]
name_key: "Skill_5030"
desc_key: "SkillComment_5030"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 90, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 302, "value": 10022, "rate": 100}
  - {"slot": 4, "type": 301, "value": 10025, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 90, "attack_pct": 80, "buffs": [{"buff": 10022, "rate": 100}, {"buff": 10025, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 90}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 124
icon: {"file": "Skill_Miriam_01.png", "index": 19}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=9a9dcc type=86a754 id=b791c2 sources=d1c885 name_key=18a872 desc_key=6fffba kind=356a19 kind_name=9bc378 target=f3d46d range=902ba3 cost=9e049c cooldown=7d0c8c movement=953fcf effect_kind=356a19 effects=231a68 damage_or_effect=0dfc97 tooltip_formula=827f56 visual=f38cfe icon=fdf9b8 used_by=97d170 -->
|  |  |
|---|---|
|  | ![The Dark Art](wiki/assets/skills/5030.png) |
| **Skill id** | `5030` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 2 |
| **Range** | 7 (world units) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 124 `PCM_Knife_01_R_어둠의 습격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 19 |

### Tooltip

> [Active] You deal `{EF_STATIC 90}``{EF_R_DAM 80}` Damage. You gain 40% additional Life Steal for 10 seconds.

Tooltip formula: **90 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 90 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 302 | applies buff (variant 302) | [[wiki/buffs/10022-you-prepare-your-next-attack\|You prepare your next Attack]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10025-the-dark-art-increased-life-steal\|The Dark Art : Increased Life Steal]] | 100 |

**Reading:** amount **90 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10022-you-prepare-your-next-attack|You prepare your next Attack]] (100%); applies [[wiki/buffs/10025-the-dark-art-increased-life-steal|The Dark Art : Increased Life Steal]] (100%).

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
