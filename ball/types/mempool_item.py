from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from ball.consensus.cost_calculator import NPCResult
from ball.types.blockchain_format.coin import Coin
from ball.types.blockchain_format.sized_bytes import bytes32
from ball.types.spend_bundle import SpendBundle
from ball.util.generator_tools import additions_for_npc
from ball.util.ints import uint32, uint64
from ball.util.streamable import recurse_jsonify


@dataclass(frozen=True)
class MempoolItem:
    spend_bundle: SpendBundle
    fee: uint64
    npc_result: NPCResult
    spend_bundle_name: bytes32
    height_added_to_mempool: uint32

    # If present, this SpendBundle is not valid at or before this height
    assert_height: Optional[uint32] = None

    # If presemt, this SpendBundle is not valid once the block height reaches
    # the specified height
    assert_before_height: Optional[uint32] = None
    assert_before_seconds: Optional[uint64] = None

    def __lt__(self, other: MempoolItem) -> bool:
        return self.fee_per_cost < other.fee_per_cost

    def __hash__(self) -> int:
        return hash(self.spend_bundle_name)

    @property
    def fee_per_cost(self) -> float:
        return int(self.fee) / int(self.cost)

    @property
    def name(self) -> bytes32:
        return self.spend_bundle_name

    @property
    def cost(self) -> uint64:
        assert self.npc_result.conds is not None
        return uint64(self.npc_result.conds.cost)

    @property
    def additions(self) -> List[Coin]:
        return additions_for_npc(self.npc_result)

    @property
    def removals(self) -> List[Coin]:
        return self.spend_bundle.removals()

    def to_json_dict(self) -> Dict[str, Any]:
        return {
            "spend_bundle": recurse_jsonify(self.spend_bundle),
            "fee": recurse_jsonify(self.fee),
            "npc_result": recurse_jsonify(self.npc_result),
            "cost": recurse_jsonify(self.cost),
            "spend_bundle_name": recurse_jsonify(self.spend_bundle_name),
            "additions": recurse_jsonify(self.additions),
            "removals": recurse_jsonify(self.removals),
        }
