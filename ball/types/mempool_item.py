from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ball.consensus.cost_calculator import NPCResult
from ball.types.blockchain_format.coin import Coin
from ball.types.blockchain_format.sized_bytes import bytes32
from ball.types.spend_bundle import SpendBundle
from ball.util.ints import uint32, uint64
from ball.util.streamable import Streamable, streamable


@streamable
@dataclass(frozen=True)
class MempoolItem(Streamable):
    spend_bundle: SpendBundle
    fee: uint64
    npc_result: NPCResult
    cost: uint64
    spend_bundle_name: bytes32
    additions: List[Coin]
    removals: List[Coin]
    height_added_to_mempool: uint32

    def __lt__(self, other: MempoolItem) -> bool:
        return self.fee_per_cost < other.fee_per_cost

    @property
    def fee_per_cost(self) -> float:
        return int(self.fee) / int(self.cost)

    @property
    def name(self) -> bytes32:
        return self.spend_bundle_name
