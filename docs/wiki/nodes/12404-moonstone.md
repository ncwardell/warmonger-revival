---
title: "Moonstone"
type: "node"
id: 12404
status: "partial"
missing: ["respawn_s"]
sources: ["client: Trigger.cdb id 12404", "video: [[gameplay/video-dungeon-run]] §5 (Crush 2016 minimap icon matches this row within ≈5 units; gathered, ≈3 s cast)"]
kind: "gather"
field: 124
x: 1881.23
z: 1924.38
shape: 5
name_key: "UnitName_1001"
model: 1086
scale: 1.0
item: 808
respawn_s: null
---
<!-- generated:start -->
<!-- generated-keys: title=19b90e type=09842e id=da35a9 sources=94b289 kind=3d390e field=f38cfe x=a640c5 z=379c4b shape=ac3478 name_key=26fc8d model=8d4f80 scale=e8dc05 item=38afd2 respawn_s=2be88c -->
|  |  |
|---|---|
| **Trigger id** | `12404` |
| **Kind** | gathering node |
| **Field** | [[wiki/fields/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress]] at (1881.23, 1924.38) |
| **Gives** | [[wiki/items/808-moonstone\|Moonstone]] |
| **Model** | ObjectList `1086`, scale 1.0 |

Gathering nodes are client data only for their place and material. How long a node takes to come back (`respawn_s`), how many items it gives and how long gathering takes were server rules; add them with a source when known.

### Seen in

- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]]
<!-- generated:end -->

## Notes

- Its minimap icon in a 2016 Crush Online video of Ghost Fortress sits at (1880, 1925); gathered in the video at (1880, 1923), within about 5 units of this row, so the 2016 node layout equals the final client's `Trigger` table ([[gameplay/video-dungeon-run|dungeon-run video notes]] §5). *video + client*

## Behaviour

- Gathering Moonstone took about **3 s** (cast bar, then "You acquired Moonstone"), and a hit from a Black Ghost did not interrupt it. After leaving and re-entering the dungeon (a fresh instance) node 12401 could be gathered again ([[gameplay/video-dungeon-run|dungeon-run video notes]] §5). *video*

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

- How long a node takes to come back inside one instance (`respawn_s`) and how many items it gives are not shown in any source; the video only shows that a fresh instance has the node again ([[gameplay/video-dungeon-run|dungeon-run video notes]] §5).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
