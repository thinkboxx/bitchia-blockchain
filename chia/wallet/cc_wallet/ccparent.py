from dataclasses import dataclass
from typing import Optional

from bitchia.types.blockchain_format.sized_bytes import bytes32
from bitchia.util.ints import uint64
from bitchia.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CCParent(Streamable):
    parent_name: bytes32
    inner_puzzle_hash: Optional[bytes32]
    amount: uint64
