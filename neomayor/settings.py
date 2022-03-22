from pathlib import Path
import os

try:
    import pwd
    USER = pwd.getpwuid(os.getuid())[0]
except ModuleNotFoundError as e:
    USER = os.getlogin()

PROJECT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
WWW_STORAGE = PROJECT_DIR / "www"
CACHE_STORAGE = PROJECT_DIR / "data"

PROJECT_STRUCTURE = {
    "dirs_to_make": [
        PROJECT_DIR,
        WWW_STORAGE,
        CACHE_STORAGE
    ],
    "info.json": CACHE_STORAGE / "info.json",
    "list.json": CACHE_STORAGE / "list.json",
}