# 1 Ball coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_ballcoin = 1000000000000
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

def calculate_reward(height: int, index: int = -1) -> int:
    _height, _reward = _reward_per[index]
    if height >= _height if index == -1 else height < _height:
        return _reward
    else:
        index += 1
        return calculate_reward(height, index)
        
print(calculate_reward(100000000))