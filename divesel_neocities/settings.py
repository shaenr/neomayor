from pathlib import Path
import os
import pwd

USER = pwd.getpwuid(os.getuid())[0]
PROJECT_DIR = Path(f"/home/shaen/neocities-mayor")
LOCAL_STORAGE = PROJECT_DIR / "local"
