from __future__ import annotations

from ball.types.blockchain_format.sized_bytes import bytes32
from ball.util.ints import uint32, uint64

# 1 Ball coin = 1,000,000,000,000 = 1 trillion mojo.
MOJO_PER_BALL = 1000000000000
STAKE_FORK_HEIGHT = 2000000
STAKE_LOCK_HEIGHT = 2002500
STAKE_LOCK_FIXED_HEIGHT = 2005000
OLD_STAKE_FORK_HEIGHT = 2020000
_reward_per = [
    (100000, 200),
    (200000, 190),
    (300000, 180),
    (400000, 170),
    (500000, 160),
    (700000, 150),
    (900000, 140),
    (1100000, 130),
    (1300000, 120),
    (1600000, 110),
    (1900000, 100),
    (1900000, 100),
]


def calculate_reward(height: uint32, index: int = -1) -> int:
    _height, _reward = _reward_per[index]
    if height >= _height if index == -1 else height < _height:
        return _reward
    else:
        index += 1
        return calculate_reward(height, index)


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height < STAKE_FORK_HEIGHT:
        return uint64(int((7 / 8) * calculate_reward(height) * MOJO_PER_BALL))
    return uint64(int((7 / 8) * 20 * MOJO_PER_BALL))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height < STAKE_FORK_HEIGHT:
        return uint64(int((1 / 8) * calculate_reward(height) * MOJO_PER_BALL))
    return uint64(int((1 / 8) * 20 * MOJO_PER_BALL))


def calculate_community_reward(height: uint32) -> uint64:
    if height < STAKE_FORK_HEIGHT:
        return uint64(int((6 / 100) * calculate_reward(height) * MOJO_PER_BALL))
    return uint64(int(60 * calculate_reward(height) * MOJO_PER_BALL))


def calculate_stake_farm_reward(height: uint32) -> uint64:
    return uint64(80 * MOJO_PER_BALL)


def calculate_stake_lock_reward(scale: float) -> float:
    return 4608*200 * MOJO_PER_BALL * scale


def calculate_timelord_fee(height: uint32) -> uint64:
    """
    Community Rewards: 2% every block
    """
    if height < STAKE_FORK_HEIGHT:
        return uint64(int((2 / 100) * calculate_reward(height) * MOJO_PER_BALL))
    else:
        return uint64(0)
