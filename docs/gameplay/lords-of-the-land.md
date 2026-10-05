---
title: "Lords of the Land buff and quest"
---

# Lords of the Land buff and quest

What one forum post (Kawe, Crush Online forum, October 2016) and its three screenshots show about the **Lords of the Land** war buff, its six reward boxes and the quest chain that asks for them, checked against the client tables. For the war itself see [[gameplay/pvp-and-matches|PvP, land wars and matches]].

Sources:

- [thread] the forum post and replies: [archived thread][thread]
- [img-buff] buff window with the compensation row, Oct 2016 Crush client: [NqmceA1][img-buff]
- [img-quest] quest log + buff window side by side: [AEjbbtw][img-quest]
- [img-map] world map with land names and the buff rules: [gqWSZJQ][img-map]

Confidence tags: *client* (decoded table in `data/tables/`), *image* (read off a screenshot), *guide* (the post text), *guess*.

## 1. How a stack is earned and lost

| Rule | Source |
|---|---|
| +1 stack for winning a war on an **NPC (grey) land** | *guide + image* [thread], [img-map] |
| +1 stack for **successfully defending** a fort/land ("Fort Defend Victory") | *guide + image* [thread], [img-map] |
| **0** stacks for conquering an **enemy nation's** land | *guide + image* [thread] (reply), [img-map] |
| −1 stack for **losing** a war or **leaving** one | *guide* [thread] |
| Claiming a box resets the buff and the compensation row to zero ("when compensation is received, the buff and compensation reset") | *image* [img-buff] |
| Gaining more stacks than the quest needs overwrites the progress; the player must restart | *guide* [thread] |
| Later client text: the buff is granted when the attacker earns a **medal**; running away or losing resets it | *client* `Skill_Buff` 3029–3034 description |

## 2. Buff tiers

Two versions exist. The October 2016 screenshot shows the Crush-era numbers; the decoded client (later Warmonger build) carries different text for the same buff ids.

| Tier | Oct 2016 (*image* [img-buff], [img-quest]) | Later client text (*client* `Skill_Buff` 3029–3034) |
|---|---|---|
| 1 | Attack damage and Ability Power **+4%** | Attack damage and Ability Power **+10** (flat) |
| 2 | Cooldown and resurrection wait **−5%** | Resurrection wait **−5%** |
| 3 | SP gain **+6** | Armor and Magic Resistance **+4%** |
| 4 | Take **5%** less damage and deal the same amount back as bonus damage | Attack damage, Ability Power **+4%** |
| 5 | Heal and Mana Regeneration **+20**; **doubles** the whole buff | **Doubles** the whole buff |

Buff timing:

- The buff shows a remaining time: **42 min** in one screenshot, **88 min** in the other. *image* [img-buff], [img-quest]
- `WinAffect` gives each stack level a duration of **120** (minutes, matching the screenshots) *client*; `Skill_Buff` 3030–3034 also hold `120` in the duration column, while 3029 (the 0-stack placeholder) holds 2,100,000,000 (never expires). *client*
- Tier icon: `Skill_Boss_01.dds` index 3 for all six rows; tier 5 uses effect 1060, tiers 1–4 effect 1058. *client*

## 3. Stack level → buff → box (`WinAffect`)

| Stacks | Buff id | Box item id | Box name (*client* `Item_Base`) |
|---|---|---|---|
| 0 | 3029 | — | — |
| 1 | 3030 | 1023 | Spirit of Gaia Box |
| 2 | 3031 | 1024 | Help of Gaia Box |
| 3 | 3032 | 1025 | Impact of Gaia Box |
| 4 | 3033 | 1026 | Ruler of Gaia Box |
| 5 | 3034 | 1027 | Phase of Gaia Box |
| 6 | 3034 | 1028 | Lords of the Land Box |

*client* `WinAffect.tsv`, `Item_Base.tsv`. The screenshot's compensation row has exactly **six** boxes, each "×1", in the same left-to-right order (gold, green, red, purple, blue, gold-white); the post calls the 4th one the **purple** box. *image* [img-buff], [thread]

All six boxes: item kind 43, bound, any class, icon `Items_07.png` 39–44, buy/sell value 1,000 (currency 2, *guess* gold), `opt1_value` 20 → 25 rising with the tier (*guess*: box level). *client*. Their contents are not in `RandomBox.tsv` (no row lists 1023–1028), so the drop table is still unknown. A later patch made opening the box cost 200,000 gold (was 300,000) — see [[gameplay/server-rules|server rules]].

## 4. The quest chain (NPC Kelsey)

The quest giver is **Kelsey, the Legion Manager** (*image* [img-quest]); in the client that is unit **210** (`UnitDB`, guild NPC portrait `NPC_Guild.dds`, talk set `Quest_Talk_Default_Guild`). Quest map field 120 (`FieldNames` "Fortress"). *client*

| Quest id | Name | Objective (type 15, conquer NPC land) | Then | Reward | Source |
|---|---|---|---|---|---|
| 117 | Lords of the Land | conquer **2** NPC lands | talk to Kelsey (210) | 100,000 exp + **Help of Gaia Box** (1024) | *client* `Quest`; *image* [img-quest] shows "Conquer NPC territory (2/2)", "Gain a random box as a reward", reward box = 2nd box |
| 763 | No2. Lords of the Land | conquer **3** | talk to Kelsey | 1,500,000 exp + Impact of Gaia Box (1025) | *client* |
| 764 | No3. Lords of the Land | conquer **4** | talk to Kelsey | 1,500,000 exp + Ruler of Gaia Box (1026) | *client*; post: "No.3 quest = purple box (4th)" [thread] |
| 765 | No4. Lords of the Land | conquer **5** | talk to Kelsey | 1,500,000 exp + Phase of Gaia Box (1027) | *client* |

- The quest is completed by **claiming the box whose stack count equals the quest's number of conquests**, starting from zero stacks (e.g. 4 conquests → 4th box). *guide* [thread]
- Quest 117 follows quest 714 (*Buy time energy*); 763–765 follow quest 769 (*Group – Border Area Hard Mode*). *client* (`prev_quest?` column, guessed meaning).
- The `Achievement_Base` row 36 "Lords of the Land" has thresholds 1, 5, 10, 20, 30, 40, 60, 80, 100, 150 and points 10–100. *client*

## 5. Other numbers on the screenshots

| Value | What | Source |
|---|---|---|
| 10,000 | TP target on a grey-land war HUD (0/10000) | *image* [img-buff] |
| 40:00 | War length: panel reads "Remaining Time 39:24" right after a tower fell | *image* [img-map] |
| Windmist Valley (80) | War on the map screenshot: defender **Armia**, attacker **Erion** | *image* [img-map] |
| [Lv 8] Thorns Hell (129) | Dungeon shown on the minimap during the grey-land war | *image* [img-buff] |
| Freya | Gives "Defensive aggression" (kill Tempest Fisher 0/1 / Slayer Komodo 0/1) | *image* [img-buff], [img-quest] |
| Kelsey | Also gives "Battle with Legion members No. 2" (battle with 10 legion members) | *image* [img-buff] |
| Odin | Repeat quest "Destroy the hell of demon": kill 10 Demon Hunters + 10 Elite Demon Hunters | *image* [img-buff] |

## 6. World map land names

Every Gaia land label on [img-map] matches a `FieldNames` id 1–86 (End of Earth = 1 … Moonlight Temple = 86); the training areas above the map are the nation home zones 87–98. *image + client*. Ownership in that snapshot (Erion's view): a brown NPC block on the west (End of Earth, Exit of Shadewood, Fall of Abyss, Long Canyon, Punish Canyon/Peak, Dark Shore, Eternal River regions, Fairy's Wood, Spirit's Hill), a red nation in the north-west centre, a green nation in the north-east, blue across the south. *image* [img-map]. The map marks the NPC block "+1 land buff", the green/red enemy block "no land buff", and the defended forts (yellow circles near Eternal River – Lower Region, Sunstone Hill, Angry River – Lower Region) "+1". *image* [img-map]

[thread]: https://web.archive.org/web/20161115172439/http://www.crush-game.com:80/forum/threads/psa-land-lord-quest.24/
[img-buff]: https://i.imgur.com/NqmceA1.jpg
[img-quest]: https://i.imgur.com/AEjbbtw.jpg
[img-map]: https://i.imgur.com/gqWSZJQ.jpg
