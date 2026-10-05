---
title: "PvP, land wars and matches"
---

# PvP, land wars and matches

From the player guides listed in [[gameplay/README|Gameplay]] and their screenshots, checked against `Skill_TP.tsv`, `UnitDB.tsv` and [[spec/match]]. Tags: **client**, **guide(s)**, **image**, **guess**.

## 1. Land war (field war)

The core PvP. Walking into an enemy-owned land (or a grey land) starts a **war** for it.

- **Length: 40 minutes.** *guides* [definitive guide][g-def] §PvP, [strategy guide][g-strat] §How to War.
- **Defenders start owning all towers.** If no nexus falls before time runs out, **the defence wins**. *guide* [strategy guide][g-strat].
- Attack wins by **destroying the enemy Nexus**, or (Crush Online era) by reaching **10,000 TP**. The HUD shows "TP: x / 10000", Kill and Assist counters and a countdown clock. *guide* [Crush basics][g-crush-basics] §Wars, *image* [strategy guide][g-strat]. Client: TP gauge out of 10,000 ([[spec/match]] §3).
- Grey (NPC) land: kill its boss **or** reach 10,000 TP. *guide* [Crush basics][g-crush-basics].
- **Nexus lock**: the nexus can only be damaged when **at most one** of its towers is still standing. *guide* [definitive guide][g-def].
- **Towers**: a destroyed tower slot can be rebuilt after **~20 seconds** for **500 TP**. The minimap marks unbuilt tower slots with a green circle and jungle camps with yellow circles. *guide + image* [definitive guide][g-def].
- **TP** (territory points) is a **team pool**: spending it on a skill removes it for the whole team, so attackers racing to 10,000 should not spend it. *guide* [Crush basics][g-crush-basics] §SP, EP, TP.
- **TP from kills**: normal monster **30**, elite **100**, Troll **1,500**, Ogre **2,500**, Bear **3,000** (the definitive guide rounds all three to "1,500+"). *guides* [strategy guide][g-strat], [definitive guide][g-def].
- The ordinary monsters in a war are those of the invaded nation's **dungeon** for that land. *guide* [strategy guide][g-strat].
- **Jungle bosses** (Troll, Ogre, Bear): when killed they **join the killer's team** and push the nearest enemy towers, then the nexus once the towers are gone. Spawn timers on the 40:00 clock: **Troll and Ogre at 36:00, then 4 minutes after each death; Bear at 35:00, then 5 minutes after each death**. *guides* [definitive guide][g-def], [strategy guide][g-strat]. Client: Troll 562/563/583/584, Ogre 548–555/564/565/575–582, Bear 571/572, Giant Bear 573/574/601/602 (*client*).
- **Golems** (and one other rare monster) appear on some lands for **1,500 / 2,500 TP**; they only give a **buff** and do not attack towers. *guide* [strategy guide][g-strat]. Client: Jungle/Valley/Mushroom/Wasteland/Sulphur Golem 610–618.

### TP skills

Right-click your **Nexus** or a **Tower** to open its TP skill grid. Values seen in-game (*image* [strategy guide][g-strat]) and in client `Skill_TP.tsv` (*client*):

| Skill (skill id) | Used from | TP | Cooldown (image) | Client `Skill_TP` TP / cd | Effect (in-game text, paraphrased) |
|---|---|---|---|---|---|
| Shield recovery (4500/4501) | Nexus, Tower | 1,500 | 120 s | 1500 / 120 | Gives the nexus a shield (restores shield, not HP) |
| Remote Bomb (4502/4527) | Nexus | 1,500 | 120 s | 1500 / 120 | PvP: hits enemy towers, then the nexus once the attacking towers are gone. PvE: hits every boss after the middle one |
| Nexus Remote Bomb (4504) | Tower | 2,000 | 180 s | 2000 / 180 | Attacks the nexus |
| Siege Minion (4506) | Nexus | 1,000 | 100 s | 1000 / 60 | Summons a weak tanking minion; **field war only** |
| Fortified (4507) | Tower | 2,000 | 180 s | 2000 / 120 | Raises attack and defence of all your towers on the map |

Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Freeze (4518), Highly Concentrated Bomb (4519, **10,000 TP**), Powerful Remote Bomb (4521/4525, 2,500), Powerful Nexus Remote Bomb (4523, 3,000), and four free ones (4701–4707). More TP skills unlock when the **legion equips Cores**; Shield, Bomb and Siege Minion are always available on attack/defence fields (not neutral). *guide* [definitive guide][g-def]; *client*.

### Rewards

- Winning a war against the NPC side, or **successfully defending** a land, gives a stacking **"Lords of the Land"** buff. Attacking an enemy land successfully does **not**. Clicking the buff lets you spend the stacks on a chest; more stacks → better chest. *guide* [Crush basics][g-crush-basics] §Wars. Client: `WinAffect` (war-winner buff/item). The strategy guide warns players to postpone the "Lord of the Lands" quest line.
- Medals (bronze/silver/gold) are earned in PvP **by performance**; bronze also from monster invasions. Mithril only from Gold/Mithril reward boxes. *guide* [Turkish guide][g-tr] §Para Birimleri. Client: match type 0xd has "no medals in the result" ([[spec/match]] §2).
- Daily quests include **Kill Player** (10 enemy players in Gaia), **War of Warmonger**, **Win in Battle**; weekly and monthly versions exist (monthly Kill Player 240). *image* [noob guide][g-noob], [strategy guide][g-strat].
- Game option "War of warmonger Support" (used "for medal farming") and "Alarm War". *image* [noob guide][g-noob] §Getting started. Probably auto-joins/notifies wars (*guess*).

## 2. Fort war

See [[gameplay/classes-and-legions#4-forts-castles|Forts]]: weekly **Civil War** (Sunday 20:00, same-nation legions, bid on Saturday) played as a normal nexus battlefield inside the fort, and **fort sieges** by the other nation (6 cores and the Heart of Magic on floor 1; a hero-only boss on floor 2; Crusader Cherubim guardian; up to 3 shields). Client match types 8 and 9 are fort war (FortWarGauge) ([[spec/match]] §2).

## 3. Queued battles and arenas

- The guides barely mention queued matches. A daily quest **"Win in Battle"** and an achievement category **Battle** (935 points) separate from **War** (2,530 points) show that queued "battles" existed alongside land wars. *image* [noob guide][g-noob].
- Client field 140 is *Battle Arena*; match types 2/3/4 are normal queued matches with nation teams, 6/0xa are custom rooms ([[spec/match]] §2). *client*.

## 4. Field PvP outside wars

- Enemy players can be killed in Gaia fields (quests count "destroy the enemy player from the Gaia field"). *image*.
- Crush Online had **SP** (gained by killing monsters in a zone, starting at 0 on entry; spent to "activate" equipment steps) and **EP** (equipment points, max by level, each item has an EP cost). *guide* [Crush basics][g-crush-basics]. Not seen in Warmonger guides — likely removed.

[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-crush-basics]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080
