"""Command line: see __init__.py."""
import sys
import time

from . import common, entity_modules, index


def build(types, dry_run=False, verbose=False):
    t0 = time.time()
    ctx = common.Ctx(dry_run=dry_run, verbose=verbose)
    mods = entity_modules()
    unknown = [t for t in types if t not in mods]
    if unknown:
        sys.exit("unknown type(s): %s (have: %s)" % (", ".join(unknown), ", ".join(sorted(mods))))
    chosen = {t: mods[t] for t in (types or sorted(mods))}
    built = {}
    for t, mod in chosen.items():          # phase 1: data + merge with disk
        pages = list(mod.build(ctx))
        for p in pages:
            common.prepare(ctx, p, mod)
        built[t] = pages
        ctx._pages[t] = {p.id: p.fm for p in pages}
    report = []
    for t, pages in built.items():         # phase 2: bodies (may read other types)
        stats = {"new": 0, "changed": 0, "unchanged": 0, "renamed": 0}
        for p in pages:
            common.write(ctx, p, stats)
        ids = {p.id for p in pages}
        orphans = [f.name for f in (common.OUT / t).glob("*.md")
                   if f.name != "index.md" and f.name.split("-", 1)[0].split(".")[0].isdigit()
                   and int(f.name.split("-", 1)[0].split(".")[0]) not in ids]
        status = {}
        for p in pages:
            status[p.fm["status"]] = status.get(p.fm["status"], 0) + 1
        report.append("%-10s %5d pages  %s  %s%s" % (
            t, len(pages), " ".join("%s %d" % kv for kv in stats.items()),
            " ".join("%s %d" % kv for kv in sorted(status.items())),
            ("  orphans: %s" % ", ".join(orphans[:10])) if orphans else ""))
    if not dry_run:
        index.write_indexes(ctx)
    for n in ctx.notes:
        print("note:", n)
    print("\n".join(report))
    print("%s in %.1fs" % ("dry run" if dry_run else "built", time.time() - t0))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        sys.exit(__import__("wiki.gamewiki").gamewiki.__doc__)
    cmd, rest = argv[0], argv[1:]
    flags = {a for a in rest if a.startswith("--")}
    args = [a for a in rest if not a.startswith("--")]
    if cmd == "build":
        build(args, dry_run="--dry-run" in flags, verbose="--verbose" in flags)
    elif cmd == "assets":
        from . import assets
        assets.main(args, force="--force" in flags)
    elif cmd == "index":
        index.write_indexes(common.Ctx())
    else:
        sys.exit("unknown command %r" % cmd)


main(sys.argv[1:])
