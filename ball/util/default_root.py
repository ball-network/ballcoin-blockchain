from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("BALL_ROOT", "~/.ball/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("BALL_KEYS_ROOT", "~/.ball_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("BALL_SIMULATOR_ROOT", "~/.ball/simulator"))).resolve()
