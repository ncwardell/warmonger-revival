"""Where the server finds game data extracted from your own copy of the client.

Set WARMONGER_DATA to override; the default is ./data at the repository root
(gitignored). Populate it with tools/jpk.py, e.g.
  python3 tools/jpk.py extract "<game>/Data/setting.jpk" data/setting
"""
import os
import pathlib

DATA = pathlib.Path(os.environ.get("WARMONGER_DATA", pathlib.Path(__file__).resolve().parent.parent / "data"))
SETTING = DATA / "setting"
