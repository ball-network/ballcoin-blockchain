from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ball.consensus.block_rewards import MOJO_PER_BALL, STAKE_LOCK_FIXED_HEIGHT
from ball.util.ints import uint16, uint64
from ball.util.streamable import Streamable, streamable

STAKE_PER_COEFFICIENT = 10 ** 17

STAKE_FARM_COUNT = 10000
STAKE_FARM_MIN = 10000 * MOJO_PER_BALL
STAKE_FARM_PREFIX = "dpos:ball:"

STAKE_LOCK_MIN = 10000 * MOJO_PER_BALL


@streamable
@dataclass(frozen=True)
class StakeValue(Streamable):
    time_lock: uint64
    coefficient: str
    reward_coefficient: Optional[str]

    def stake_amount(self, amount: uint64) -> int:
        return int(int(amount) * float(self.coefficient) * MOJO_PER_BALL)

    def least_reward_amount(self, amount: uint64) -> float:
        if self.reward_coefficient is None:
            return 0
        return int(amount) * MOJO_PER_BALL * float(self.coefficient) * float(self.reward_coefficient)

    def least_reward_amount2(self, amount: uint64) -> float:
        if self.reward_coefficient is None:
            return 0
        return int(amount) * MOJO_PER_BALL * float(self.reward_coefficient)

STAKE_FARM_LIST: List[StakeValue] = [
    StakeValue(86400 * 3, "1.0", None),
    StakeValue(86400 * 10, "1.05", None),
    StakeValue(86400 * 30, "1.1", None),
    StakeValue(86400 * 90, "1.2", None),
    StakeValue(86400 * 180, "1.4", None),
    StakeValue(86400 * 365, "1.6", None),
    StakeValue(86400 * 730, "1.8", None),
    StakeValue(86400 * 1095, "2", None),
    StakeValue(86400 * 1825, "2.25", None),
    StakeValue(86400 * 3650, "2.5", None),
]


STAKE_LOCK_LIST: List[StakeValue] = [
    StakeValue(86400 * 3, "1.0", "0.0002"),
    StakeValue(86400 * 10, "1.05", "0.00021"),
    StakeValue(86400 * 30, "1.1", "0.00022"),
    StakeValue(86400 * 90, "1.2", "0.00024"),
    StakeValue(86400 * 180, "1.4", "0.00028"),
    StakeValue(86400 * 365, "1.6", "0.00032"),
    StakeValue(86400 * 730, "1.8", "0.00036"),
    StakeValue(86400 * 1095, "2", "0.0004"),
    StakeValue(86400 * 1825, "2.25", "0.00045"),
    StakeValue(86400 * 3650, "2.5", "0.0005"),
    StakeValue(86400 * 5475, "3.15", "0.00052"),
    StakeValue(86400 * 7300, "3.3", "0.00054"),
    StakeValue(86400 * 10950, "3.5", "0.0006"),
]


STAKE_LOCK_LIST2: List[StakeValue] = [
    StakeValue(86400 * 3, "1.0", "0.0002"),
    StakeValue(86400 * 10, "1.05", "0.00021"),
    StakeValue(86400 * 30, "1.1", "0.00022"),
    StakeValue(86400 * 90, "1.2", "0.00024"),
    StakeValue(86400 * 180, "1.4", "0.00028"),
    StakeValue(86400 * 365, "1.6", "0.00032"),
    StakeValue(86400 * 730, "1.8", "0.00036"),
    StakeValue(86400 * 1095, "2", "0.0004"),
    StakeValue(86400 * 1825, "2.25", "0.00045"),
    StakeValue(86400 * 3650, "2.5", "0.0005"),
    StakeValue(86400 * 5475, "2.6", "0.00052"),
    StakeValue(86400 * 7300, "2.7", "0.00054"),
    StakeValue(86400 * 10950, "3", "0.0006"),
]


def get_stake_value_time_lock(stake_type: uint16, is_stake_farm: bool) -> uint64:
    value = STAKE_FARM_LIST if is_stake_farm else STAKE_LOCK_LIST2
    if 0 <= stake_type < len(value):
        return value[stake_type].time_lock
    return uint64(0)


def get_stake_value(height: uint32, stake_type: uint16, is_stake_farm: bool) -> StakeValue:
    value = STAKE_FARM_LIST if is_stake_farm else (
        STAKE_LOCK_LIST if height < STAKE_LOCK_FIXED_HEIGHT else STAKE_LOCK_LIST2
    )
    if 0 <= stake_type < len(value):
        return value[stake_type]
    return StakeValue(0, "0", None)


def get_stake_lock_coefficient(stake_type: uint16) -> str:
    if 0 <= stake_type < len(STAKE_LOCK_LIST2):
        return STAKE_LOCK_LIST2[stake_type].coefficient
    return "0"
