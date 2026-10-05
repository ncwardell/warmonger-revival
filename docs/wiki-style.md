---
title: "How to write wiki pages"
---

# How to write wiki pages

- **One topic per page**, named plainly (`death-valley.md`, `saint.md`). Link pages with `[[file-name]]` or `[[file-name|shown text]]`; links resolve by file name, as in Obsidian.
- **Cite every fact.** Put the source right after it: `Bosses respawn every 30 minutes ([src](https://…))`. Sources can be a guide, a video (with timestamp), a captured packet, a client table (`Item_Base.cdb`, column), or a client function address.
- **Say how sure you are** when it isn't obvious: *confirmed in client*, *from a guide*, *player memory*, *guess*.
- **Use the client's ids** where known (field/map id, unit id, item code), so the server can use the page directly.
- **Your own words only.** Don't paste text or images from guides; describe them and link the original.
- **The game wiki (`wiki/`) is the exception for the game's own content.** Its pages reproduce the client's names, stats, quest dialogue, icons and portraits, credited to the game on every page (*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*). That content comes from the generator (`python3 -m wiki.gamewiki build`); add your own findings in the front matter and the hand-written sections. See [[wiki/index|Game wiki]].
- Callouts work as in Obsidian:

> [!note]
> Callouts render on the website too.
