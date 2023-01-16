import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("BALL_ROOT", "~/.ball/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("BALL_KEYS_ROOT", "~/.ball_keys"))).resolve()
