from pathlib import Path
import os
import pwd

USER = pwd.getpwuid(os.getuid())[0]

PACKAGE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = PACKAGE_DIR.parent
PROJECT_DIR = SRC_DIR.parent
WWW_STORAGE = PROJECT_DIR / "www"
CACHE_STORAGE = PROJECT_DIR / "data"

PROJECT_STRUCTURE = {
    "dirs_to_make": [
        PROJECT_DIR,
        SRC_DIR,
        PACKAGE_DIR,
        WWW_STORAGE,
        CACHE_STORAGE
    ],
    "info.json": CACHE_STORAGE / "info.json",
    "list.json": CACHE_STORAGE / "list.json",
}