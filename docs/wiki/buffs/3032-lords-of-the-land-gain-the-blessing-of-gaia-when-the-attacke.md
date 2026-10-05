---
title: "Lords of the Land : Gain the blessing of Gaia when the attacker gets the medal. 1st Buff : Attack damage and Ability Power + 10 2nd Buff : the resurrection waiting time - 5% 3rd Buff : Armor, Magic Resistance +4% 4th Buff : Attack damage , Ability Power + 4% 5th Buff : doubles benefits of the whole buff. When you runaway of defeat from battle field, this buff will be reset."
type: "buff"
id: 3032
status: "complete"
missing: []
sources: ["client: Skill_Buff.cdb id 3032", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)", "guide: [[gameplay/lords-of-the-land]] §1–§3 (stack rules, tiers, WinAffect mapping)", "guide: [[gameplay/pvp-and-matches]] Rewards", "notes: [[gameplay/events-and-schedules]] §2, WM 0426 / WM 0920 (medal rule, leave penalty, box price)", "notes: [[gameplay/crush-patch-notes]] 2016-11-23 and [[gameplay/events-and-schedules]] §11 (CO tiers; history)", "image: [[gameplay/lords-of-the-land]] §2 and video: [[gameplay/video-fort-war]] §1 (120 = minutes; 42/88/86 min seen)", "client: [[gameplay/lords-of-the-land]] §2 (effects from the client buff text, tiers 1–3; read as cumulative, *inferred*)"]
manual: ["effects", "duration"]
name_key: "SkillBuff_3032"
duration: {"ticks": 120, "seconds": 7200.0, "permanent": false, "unit": "minutes (WinAffect)"}
is_buff: 0
stack_type: 1
group: 0
effects:
  - {"code": 1, "stat": "Attack", "value": 10, "tier": 1}
  - {"code": 2, "stat": "Ability Power", "value": 10, "tier": 1}
  - {"code": null, "stat": "Resurrection waiting time (%)", "value": -5, "tier": 2}
  - {"code": null, "stat": "Armor (%)", "value": 4, "tier": 3}
  - {"code": null, "stat": "Magic Resist (%)", "value": 4, "tier": 3}
icon: {"file": "Skill_Boss_01.dds", "index": 3}
applied_by:
  - {"war_reward": 3}
---
<!-- generated:start -->
<!-- generated-keys: title=a9fe57 type=6143a1 id=36f2cb sources=85e421 name_key=aaed43 duration=acd3ed is_buff=b6589f stack_type=356a19 group=b6589f effects=97d170 icon=596634 applied_by=c62c48 -->
|  |  |
|---|---|
|  | ![Lords of the Land : Gain the blessing of Gaia when the attacker gets the medal. 1st Buff : Attack damage and Ability Power + 10 2nd Buff : the resurrection waiting time - 5% 3rd Buff : Armor, Magic Resistance +4% 4th Buff : Attack damage , Ability Power + 4% 5th Buff : doubles benefits of the whole buff. When you runaway of defeat from battle field, this buff will be reset.](../assets/buffs/3032.png) |
| **Buff id** | `3032` |
| **Duration** | 24 s (120 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 3 |

### Tooltip

> Lords of the Land :
>
> Gain the blessing of Gaia when the attacker gets the medal.
>
> 1st Buff : Attack damage and Ability Power + 10
> 2nd Buff : the resurrection waiting time - 5%
> 3rd Buff : Armor, Magic Resistance +4%
> 4th Buff : Attack damage , Ability Power + 4%
> 5th Buff :  doubles benefits of the whole buff.
>
> When you runaway of defeat from battle field, this buff will be reset.

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.

### Applied by

- War-winner reward, WinAffect row 3 (120 minutes?)

### Mentioned in

- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] § 3. Stack level → buff → box (`WinAffect`) (line 55): 3 · 3032 · 1025 · Impact of Gaia Box
<!-- generated:end -->

## Notes

- Lords of the Land war buff, stack level 3 (`WinAffect`: stacks → buff 3032, box 1025 Impact of Gaia) ([[gameplay/lords-of-the-land]] §3). *client*
- Earning: +1 stack for winning a grey (NPC) land war or defending a land, nothing for conquering an enemy nation's land, −1 for losing or leaving; claiming a box resets the buff ([[gameplay/lords-of-the-land]] §1; [[gameplay/pvp-and-matches]] Rewards). In WM the buff needs at least one medal in the fight; leaving a war early resets it, lowers its reward level by 1 and costs fame ([WM 0426](https://steamcommunity.com/games/718790/announcements/detail/2394103650887775295), [[gameplay/events-and-schedules]] §2). Opening the reward box costs 300,000 → 200,000 gold ([WM 0920](https://steamcommunity.com/games/718790/announcements/detail/2450411965551395652)). *guide + image + notes*
- Tiers, as the WM client text gives them: 1 Attack and AP +10; 2 resurrection wait −5 %; 3 Armor and MR +4 %; 4 Attack and AP +4 %; 5 the whole buff doubles ([[gameplay/lords-of-the-land]] §2). The Crush Online launch tiers (Oct 2016) were different: +4 % AD/AP; cooldown and respawn −5 %; SP gain +6; 5 % damage taken dealt back; +20 heal/mana regen and doubling ([[gameplay/lords-of-the-land]] §2; [[gameplay/crush-patch-notes]] 2016-11-23; [[gameplay/events-and-schedules]] §11). *client + image*
- Duration: `WinAffect` gives each stack level **120** and the screenshots show 42 and 88 min left, the June 2018 fort-war video 86 min ([[gameplay/lords-of-the-land]] §2; [[gameplay/video-fort-war]] §1). So this row's 120 counts **minutes**, not 200 ms ticks; the duration is set to 7,200 s here. *client + image + video*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/lords-of-the-land]], [[gameplay/pvp-and-matches]] Rewards, [[gameplay/events-and-schedules]] §2, §11, [[gameplay/crush-patch-notes]] 2016-11-23, [[gameplay/video-fort-war]] §1.

## Open questions

- Tiers: the Crush Online (Oct 2016) and WM client texts differ (see Notes); the client text is used.
- Effects are entered as cumulative (tier n includes tiers 1…n), as the "doubles the whole buff" wording implies; no source states it outright. Codes are left empty where the stat (resurrection wait, Armor %, MR %) has no unambiguous `ItemOption` code.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
