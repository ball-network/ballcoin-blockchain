from dataclasses import dataclass
from typing import Optional

from ball.types.blockchain_format.sized_bytes import bytes32
from ball.types.blockchain_format.vdf import VDFInfo, VDFProof
from ball.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class SignagePoint(Streamable):
    cc_vdf: Optional[VDFInfo]
    cc_proof: Optional[VDFProof]
    rc_vdf: Optional[VDFInfo]
    rc_proof: Optional[VDFProof]
    timelord_fee_puzzle_hash: Optional[bytes32]
