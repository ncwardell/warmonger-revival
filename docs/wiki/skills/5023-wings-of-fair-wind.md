---
title: "Wings of fair wind"
type: "skill"
id: 5023
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5023"]
name_key: "Skill_5023"
desc_key: "SkillComment_5023"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10021, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10021, "rate": 100}]}
visual: 178
icon: {"file": "Skill_Einsel_01.png", "index": 25}
used_by:
  - {"weapon_base": 18, "slot": 2, "items": [10017]}
---
<!-- generated:start -->
<!-- generated-keys: title=17b215 type=86a754 id=07e9ca sources=d154c3 name_key=1f8aaa desc_key=f4f6cc kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=911ade cooldown=628d31 effect_kind=da4b92 effects=ecaab3 damage_or_effect=fb1efb visual=25293f icon=8f0410 used_by=6c763e -->
|  |  |
|---|---|
|  | ![Wings of fair wind](../assets/skills/5023.png) |
| **Skill id** | `5023` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 25 |

### Tooltip

> [Active] Increases your Ability Power by 20%. You gain 5% Armor and Magic Resistance.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10021-wings-of-westerly-increased-ability-power-armor-and-magic-re\|Wings of Westerly : Increased Ability Power, Armor and Magic Resistance]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10021-wings-of-westerly-increased-ability-power-armor-and-magic-re|Wings of Westerly : Increased Ability Power, Armor and Magic Resistance]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 18: [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
- `contract/combat.yaml` line 597: `- "C->S 0x411 for a buff skill (e.g. 5023, self target slot 0 = caster)"`
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
