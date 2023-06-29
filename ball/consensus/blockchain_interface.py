from __future__ import annotations

from decimal import Decimal
from typing import Dict, List, Optional

from blspy import G1Element
from chia_rs import FullBlock

from ball.consensus.block_record import BlockRecord
from ball.types.blockchain_format.sized_bytes import bytes32
from ball.types.blockchain_format.sub_epoch_summary import SubEpochSummary
from ball.types.blockchain_format.vdf import VDFInfo
from ball.types.header_block import HeaderBlock
from ball.types.weight_proof import SubEpochChallengeSegment
from ball.util.ints import uint32


class BlockchainInterface:
    def get_peak(self) -> Optional[BlockRecord]:
        pass

    def get_peak_height(self) -> Optional[uint32]:
        pass

    def block_record(self, header_hash: bytes32) -> BlockRecord:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def height_to_block_record(self, height: uint32) -> BlockRecord:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def get_ses_heights(self) -> List[uint32]:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def get_ses(self, height: uint32) -> SubEpochSummary:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def height_to_hash(self, height: uint32) -> Optional[bytes32]:
        pass

    def contains_block(self, header_hash: bytes32) -> bool:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def remove_block_record(self, header_hash: bytes32) -> None:
        pass

    def add_block_record(self, block_record: BlockRecord) -> None:
        pass

    def contains_height(self, height: uint32) -> bool:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    async def warmup(self, fork_point: uint32) -> None:
        pass

    async def get_block_record_from_db(self, header_hash: bytes32) -> Optional[BlockRecord]:
        pass

    async def get_block_records_in_range(self, start: int, stop: int) -> Dict[bytes32, BlockRecord]:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    async def get_header_blocks_in_range(
        self, start: int, stop: int, tx_filter: bool = True
    ) -> Dict[bytes32, HeaderBlock]:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    async def get_header_block_by_height(
        self, height: int, header_hash: bytes32, tx_filter: bool = True
    ) -> Optional[HeaderBlock]:
        pass

    async def get_block_records_at(self, heights: List[uint32]) -> List[BlockRecord]:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    def try_block_record(self, header_hash: bytes32) -> Optional[BlockRecord]:
        if self.contains_block(header_hash):
            return self.block_record(header_hash)
        return None

    async def persist_sub_epoch_challenge_segments(
        self, sub_epoch_summary_hash: bytes32, segments: List[SubEpochChallengeSegment]
    ) -> None:
        pass

    async def get_sub_epoch_challenge_segments(
        self,
        sub_epoch_summary_hash: bytes32,
    ) -> Optional[List[SubEpochChallengeSegment]]:
        pass

    def seen_compact_proofs(self, vdf_info: VDFInfo, height: uint32) -> bool:
        # ignoring hinting error until we handle our interfaces more formally
        return  # type: ignore[return-value]

    # staking
    async def get_farmer_difficulty_coefficient(
        self, farmer_public_key: G1Element, height: Optional[uint32] = None
    ) -> Decimal:
        raise NotImplementedError("get_farmer_difficulty_coefficient not implemented")

    async def height_to_coefficient(self, block: FullBlock | HeaderBlock) -> Decimal:
        raise NotImplementedError("height_to_coefficient not implemented")
