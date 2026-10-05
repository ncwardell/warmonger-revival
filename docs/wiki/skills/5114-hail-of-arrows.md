---
title: "Hail of Arrows"
type: "skill"
id: 5114
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5114", "client: StringAll_Eng SkillComment_5114 (tooltip value tags)", "video: [[gameplay/video-character-creation-and-tutorial]] §1 starting weapons (weapon offered at creation)", "notes: [[gameplay/crush-patch-notes]] 2016-12-01 (CO: max 3 targets; history)", "guide: [[gameplay/crush-mechanics]] §5, §12 (WM client 5 targets)"]
name_key: "Skill_5114"
desc_key: "SkillComment_5114"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 10
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10114, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 80, "buffs": [{"buff": 10114, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 255
icon: {"file": "Skill_Miriam_01.png", "index": 14}
used_by:
  - {"weapon_base": 26, "slot": 3, "items": [15004]}
---
<!-- generated:start -->
<!-- generated-keys: title=7f0aab type=86a754 id=ff46fb sources=e5b9f5 name_key=fbbbea desc_key=3356c9 kind=356a19 kind_name=9bc378 target=e84f24 range=b1d578 cost=e4e7cf cooldown=e3989d delivery=93a212 effect_kind=356a19 effects=fa7d34 damage_or_effect=5d5dfd tooltip_formula=d00768 visual=3028f5 icon=21b456 used_by=4e73f6 -->
|  |  |
|---|---|
|  | ![Hail of Arrows](wiki/assets/skills/5114.png) |
| **Skill id** | `5114` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 10 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 255 `PCM_Bow_04_E 화살파도` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 14 |

### Tooltip

> [Active] Deals `{EF_STATIC 85}``{EF_R_DAM 80}` Damage to up to 3 enemies. Decreases their Movement Speed by 40% for 3 seconds.

Tooltip formula: **85 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10114-hail-of-arrows-reduced-movement-speed\|Hail of Arrows : Reduced Movement Speed]] | 100 |

**Reading:** amount **85 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10114-hail-of-arrows-reduced-movement-speed|Hail of Arrows : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 26: [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot E for [[wiki/items/15004-magical-frost-bow|Magical Frost Bow]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills (line 96): Client check: Skill_Base cooldowns are Soul Infestation 19 s (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail o...
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server (line 229): Hail of Arrows targets · 3 · 5 · WM
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2016-12-01 ((t747)) (line 277): Bow of Frost "Hail of Arrows" · tooltip fixed: hits at most 3 enemies staff
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2016-12-01 ((t747)) (line 282): WM: first-floor nexus 90,000 HP, armor 540 (WM 0809, gameplay/patch-history). Client Skill_Base 5114 Hail of Arrows has max_targets 5. client
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
<!-- generated:end -->

## Notes

- Skill E of Magical Frost Bow (item 15004), one of the Punisher's starting weapons offered at character creation in the June 2018 relaunch ([[gameplay/video-character-creation-and-tutorial]] §1, starting weapons table). *video + client*
- Crush Online fixed the tooltip on 1 Dec 2016 to say it hits at most **3** enemies ([[gameplay/crush-patch-notes]] §2016-12-01). The WM client allows **5** targets, and [[gameplay/crush-mechanics]] §12 says to use the WM value. *staff, history*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/video-character-creation-and-tutorial]] §1, [[gameplay/crush-patch-notes]] 2016-12-01, [[gameplay/crush-mechanics]] §5, §12.

## Open questions

- Targets: Crush Online 3 (Dec 2016 tooltip fix) vs WM client 5. Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
