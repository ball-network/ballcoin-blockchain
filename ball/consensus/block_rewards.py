from __future__ import annotations

from ball.util.ints import uint32, uint64

# 1 Ball coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_ball = 1000000000000
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
    (2200000, 90),
    (2500000, 80),
    (3000000, 70),
    (3500000, 60),
    (4000000, 50),
    (4500000, 40),
    (5000000, 30),
    (6000000, 20),
    (7000000, 10),
    (8000000, 8),
    (10000000, 6),
    (12000000, 4),
    (14000000, 3),
    (17000000, 2),
    (20000000, 1),
    (25000000, 0.5),
    (30000000, 0.3),
    (40000000, 0.2),
    (40000000, 0.1),
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
    due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    return uint64(int((7 / 8) * calculate_reward(height) * _mojo_per_ball))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    return uint64(int((1 / 8) * calculate_reward(height) * _mojo_per_ball))


def calculate_community_reward(height: uint32) -> uint64:
    """
    Community Rewards: 6% every block
    """
    return uint64(int((6 / 100) * calculate_reward(height) * _mojo_per_ball))


def calculate_timelord_fee(height: uint32) -> uint64:
    """
    Community Rewards: 2% every block
    """
    return uint64(int((2 / 100) * calculate_reward(height) * _mojo_per_ball))
