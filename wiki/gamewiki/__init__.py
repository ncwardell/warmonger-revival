"""Game-wiki generator: builds docs/wiki/ (one page per game entity) from the
client's data. See common.py for the design and the module contract.

  python3 -m wiki.gamewiki build [types...] [--dry-run]   pages + indexes
  python3 -m wiki.gamewiki assets [types...] [--force]    images (needs Pillow)
  python3 -m wiki.gamewiki index                          indexes only
"""
import importlib
import pkgutil

NOT_ENTITY = {"common", "index", "assets", "__main__"}


def entity_modules():
    """{type: module} for every module in this package with a build()."""
    out = {}
    for info in pkgutil.iter_modules(__path__):
        if info.name in NOT_ENTITY or info.name.startswith("_"):
            continue
        mod = importlib.import_module(__name__ + "." + info.name)
        if hasattr(mod, "build"):
            out[getattr(mod, "TYPE", info.name)] = mod
    return out
