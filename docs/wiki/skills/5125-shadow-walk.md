---
title: "Shadow Walk"
type: "skill"
id: 5125
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5125"]
name_key: "Skill_5125"
desc_key: "SkillComment_5125"
kind: 5
kind_name: "kind 5"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 45, "rate": 100}
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
  - {"slot": 3, "type": 132, "value": 2, "rate": 1}
  - {"slot": 4, "type": 302, "value": 10142, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 45, "attack_pct": 70, "stats": [{"code": 132, "value": 2}], "buffs": [{"buff": 10142, "rate": 100}]}
visual: 336
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=112228 type=86a754 id=9ec169 sources=8ef6c1 name_key=1bd340 desc_key=0f59b6 kind=ac3478 kind_name=65782b target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=595846 damage_or_effect=bd02cd visual=9c882d icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `5125` |
| **Kind** | kind 5 (5) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 336 `PCM_Knife_01_W_그림자 밟기 피격` |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 45 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |
| 3 | 132 | stat? Health Regeneration(%) | 2 | 1 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10142-shadow-walk-your-next-attack-deals-bonus-damage\|Shadow Walk : Your next Attack deals bonus damage]] | 100 |

**Reading:** amount **45 + 70% Attack**; damage (physical?); applies [[wiki/buffs/10142-shadow-walk-your-next-attack-deals-bonus-damage|Shadow Walk : Your next Attack deals bonus damage]] (100%).

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
