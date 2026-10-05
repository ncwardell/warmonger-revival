---
title: "Solo testing: saves, starter quests and weapons"
---

# Solo testing: saves, starter quests and weapons

## Start a test

From the repository root, run the server in one PowerShell window:

```powershell
.\scripts\start-test-server.ps1
```

Launch the client in another window with a consistent identity:

```powershell
.\scripts\play-windows.ps1 -Account alice
```

Each name has its own characters. The named `player` identity and an empty-token
legacy login are distinct in this branch. Existing `characters.json` and account
creation records are retained; progress is stored separately in ignored
`server/progress/<account hash>/<character id>.json`. `WARMONGER_STATE` relocates
both creation records and progress. Back up the whole state directory together.

## 1. Save and reconnect

1. Note the character name, equipped weapon and gold.
2. Kill slimes, collect their items and gold, swap a starting weapon and set an
   item quick slot. Note the new values.
3. Return to character selection and re-enter. Check bag quantities, both
   equipment slots, quick slots and gold.
4. Exit the client fully, restart the server, then launch with the same account.
   Check the same values again.
5. Try another character/account. It must have its own inventory and gold.

Progress is checkpointed after handled actions and automatic loot collection,
and before leaving. Quest slots, completion flags, experience and level are saved
too. Empty bags stay empty; starter items are seeded once. The last supported map
is saved as a checkpoint. Exact position, current HP/MP and uncollected drops are
transient. Reconnecting starts at that map's safe spawn with full HP/MP. Old saves
without a map checkpoint use the configured starting map. These remain prototype
server rules.

Saves use an atomic replacement; `.json.bak` holds the preceding checkpoint.
Invalid saves are rejected and preserved for inspection. Do not delete a save to
work around a load failure; record the error first. Creation records are never
rewritten by the progress saver (`server/persistence.py`).

## 2. Shaia and the first quests (experimental)

Exit the client and stop the previous server, then run:

```powershell
.\scripts\start-test-server.ps1 -QuestTest
.\scripts\play-windows.ps1 -Account alice
```

This explicitly enables `WARMONGER_QUEST_TEST=1`: the server uses Training Ground
(map 89) at a walkable spawn (419, 3661), near the video-derived Shaia position.
Terrain loads by coordinates (see [[spec/loading]]). Shaia (423.9, 3664.8) and
Floyd (370.5, 3660.6) use the estimates in [[gameplay/npc-locations]]; the monsters
use a small test layout on the same terrain. The spawn and every placed unit were
checked with `tools/navmesh.py`. Without this option, the server still uses map
117 at (1427, 429). Old quest-test saves retain their quests/XP and enter the
proper map on their next login.

The server loads rows 1 through 5 from your own `setting/Quest.cdb`. These are
protocol quest IDs; title suffixes 630/631/632/692 are different identifiers. The first
quest is a talk objective with Shaia; the next quests collect slime, snake and bee
items, with Floyd receiving those turn-ins. Quest 4 is a handoff from Floyd back
to Shaia: Floyd offers it, and accepting it marks it ready to turn in at Shaia.
It has no separate objective counters or rewards. Check:

1. Shaia has an offer and opens dialogue. Accept it; inspect the quest log.
2. Talk again as required. The opening talk quest completes automatically and grants experience; it has no separate turn-in NPC. Check that it leaves the log and the next quest appears.
3. Accept the slime objective, collect the required items, then visit Floyd.
4. Check that turn-in consumes required items and grants the listed reward once.
5. After the snake/bee quest, accept the next quest from Floyd, then speak to Shaia to finish the handoff. The offer marker on Floyd and the turn-in marker on Shaia are different steps.
6. Accept **United Problem Solvers** from Shaia (quest 5, title suffix 633).
   Walk to the southeast portal to Training Camp; its arrival anchor in Training
   Ground is (451.64, 3629.45). The portal trigger sends destination gate **1202**,
   not map id 88. Crossing loads map 88 at (325.8, 3438.9).
7. Walk northeast to Frei (unit 198) at (360.8, 3466.1). Turn in the letter and
   verify 2,750 XP, 500 gold and one item 402, awarded once. The video estimate
   (358.8, 3469.1) is off-mesh; this adjusted position has 2.06 units of clearance.
8. Reconnect in Camp, both before and after turning in the letter. The map and
   progress should survive. The southwest portal (destination gate 1203) returns
   to Training Ground. Abandoning the letter quest still permits the return trip.

This batch ends at the letter delivery. Quest 6's automatic assignment and quest
7's class-dependent rewards remain unsupported. Only this free two-way portal
route is enabled; other towns, teleporter menus, dungeons and wars are not enabled.
The quest-4 completion requirement and 25-unit portal proximity radius are test
server policies. Movement remains client-reported; this is not an anti-cheat
implementation. Try the quest tracker, but manually walk if auto-travel stalls:
the full client journey has not yet been tested against this server.

Packet layouts and table-field evidence: `contract/quests.yaml`, handlers
`FUN_00599ab2`, `FUN_0047529d` and `FUN_004752b3`; rewards/thresholds are read from
the local Quest and Level_Table tables. The initial zero-receiver quest completes automatically after a validated talk
report. The client skips ready markers when both receiver fields are zero
(`0x59925d`-`0x5992ab`); the automatic rule is an inference from the table and live
behavior, documented in `contract/quests.yaml`. Item consumption, a 15-unit
interaction radius, and the test monster layout are explicit server choices. Level/exp UI
updates are implemented. XP remains a cumulative total; at level L, the client
displays progress between Level_Table rows L-1 and L. A level increases upon
reaching row L, up to level 30. Older saves that are one level behind are repaired
on entry or during the live tick without changing earned XP.

Level-based combat-stat scaling is still separate work: max HP/MP remain the
test defaults (1,000/500), and player damage and defense do not grow with level.
Monster kills currently grant loot and quest progress, but no XP directly.
Quest 5 continues to NPC 198 on a different map (88 for nation 1); that travel,
later quests, dialogue services, selectable rewards and other objective types are
not implemented. The client may still offer later quests from its own tables;
their presence does not mean the server supports them. No client data or dialogue
text is copied into the repository.

## 3. Class and weapon checks

Test each weapon's model, four skill icons, basic attack, each skill's animation
and effect, swapping away/back, and reconnecting with it equipped. Record healing,
buff or movement skills separately from damaging skills: those effects are not
all implemented by the current combat prototype.

| Class | Starting weapon | Item ID |
|---|---|---|
| Saint | Blade | 10017 |
| Saint | Dual gun | 10011 |
| Saint | Thunder wand | 10001 |
| Saint | Life wand | 10002 |
| Punisher | Dagger | 15007 |
| Punisher | Bow | 15004 |
| Guardian | Demolition hammer | 20001 |
| Guardian | Cannon | 20021 |
| Guardian | Crush hammer | 20003 |

Evidence: `server/skills.py`, Create_Char / Item_Base / WeaponBase loaders and
[[spec/skills]]. All nine starting weapons have automated save/reconnect coverage;
that does not establish animation or effect correctness in the real client.

## Capture an observation

```powershell
python tools/test_session.py mark "Alice: equipped bow; fourth skill had no visible effect"
python tools/test_session.py report --log out/server.log
```

Notes include local time and UTC offset in ignored `out/test-observations.jsonl`.
The report counts incoming opcodes and lists server errors without packet bodies.
For each bug include character/class, weapon, exact steps, expected result, actual
result and time. Screenshots are useful for model/UI issues. Keep game files and
raw account/session data out of published issues.

## Original-game reference work

The [Definitive Guide for Warmonger by Zombids](https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573)
has a First Steps section and links a level-1-to-17 video. Use it as a lead for
checking quest order, markers and NPC placement. The linked footage has not been
visually verified in this implementation pass. For any finding record the source
URL, timestamp, visible NPC/quest name and relevant map landmarks; distinguish
observations from guesses. More source leads are in [[gameplay/README]].

## Automated verification

```powershell
cd server
python -B -m unittest discover -v -p 'test_*.py'
```

On 2026-10-05, 27 tests passed with local game data and in quest-test mode. Without
game data, 26 passed and the installed-table test was skipped. A captured quest-4
acceptance regression failed before enabling the handoff and passed afterward;
it also checks the prerequisite, receiver distance, duplicate completion and save.
The four standalone
world/AI/skills/loot self-tests also passed with and without game data. A fresh
Python process checks disk saves; a simulated interrupted replacement checks that
the previous save survives. Live client verification on 2026-10-05 confirmed entering the test map, opening
Shaia dialogue, accepting quest 1 and sending its valid talk report. That exposed
a missing automatic-completion rule: the server now clears the already-earned
quest and saves its 550 XP once. At 02:45, the live client then accepted quest 2,
turned it in and accepted quest 3. The persisted completion flags mark quests 1
and 2 complete, with quest 3 active and 1,870 total XP at level 2. This verifies
progression through the client protocol; the exact quest-log text was not
visually inspected. At 02:49 the client turned in quest 3; its save has completion
flags 14 and 5,720 XP at level 4. Repeated attempts to accept quest 4 then exposed
the old three-quest allowlist. Support for the Floyd-to-Shaia handoff was loaded
at 02:52 with the session preserved. At 02:53 the live client accepted quest 4
and turned it in; the save now has completion flags 30 (quests 1 through 4 done),
an empty quest log and the same 5,720 XP. The client then tried to accept quest 5,
which is outside the supported slice and was rejected. This confirms the handoff
through the client protocol; exact marker visuals, reconnect display and full
weapon checks still need confirmation.

The reported level-4 XP bar stuck at 1,920/1,920 exposed an off-by-one threshold
interpretation. Client disassembly at 0x57d223..0x57d28e confirms the display uses
rows L-1 and L. At 02:58 the running session and save were corrected to level 5,
keeping 5,720 XP and completion flags 30; expected display is 748/2,689. Boundary,
multi-level reward and live/save/reconnect regressions pass. Visual confirmation
of the corrected bar is still pending.

### Training Camp route (2026-10-05)

Evidence: `Quest.cdb` row 5 has giver maps 89/93/97 (fields 7–9), receiver maps
88/92/96 (fields 14–16), giver 201 and receiver 198. It has no objective counters;
acceptance makes it ready for the receiver, without granting its rewards.
`Teleport_List` rows 1202/1203 supply the arrival coordinates. The owned client's
`deviceTrigger` records in terrain segments ZP01_14 and ZP01_13 have action 1 and
destination 1202/1203 respectively, matching the sender `FUN_0048796a`.

The [Bravely Forward walkthrough at 11:41](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=701s)
shows United Problem Solvers active in Training Ground; at
[12:47](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=767s) it shows the letter
delivery dialogue and reward panel in Training Camp. These frames verify the
quest handoff, not the exact intervening travel inputs or packet timing.

Scene changes use `0x44e`, `FUN_00473548`, with distinct stable scene ids (89 and
88); old viewers receive removal and new viewers receive player spawns. NPC
queries, hits, displacement and AI/respawn broadcasts are scoped to map and
scene. `0x445` receives a neutral `0x446` with nation 1 to release the client's
post-travel wait (`FUN_00474eb1` -> `FUN_00598a5f`). This does not restore historical
world ownership. The avatar's team is now the prototype account's nation (1),
matching the route-state packet; NPC team 0 and monster team 4 remain unchanged.

Automated coverage includes portal rejection, old-save compatibility, map
checkpoints, cross-map combat/AI isolation, three-player visibility, return
travel, abandoned quests, duplicate rewards and an interrupted warp save.
The final run passed all 35 tests with local client data; without game data,
34 passed and the installed-table test was skipped. All four standalone
world/AI/skills/loot self-tests passed. Every placed unit and both map spawns
passed the local navmesh check; unit placements have at least 2 units of clearance.
Live loading, portal activation and quest-tracker navigation remain to be checked
in the real game. No original server combat stats or kill-XP formula were recovered
by this work.
