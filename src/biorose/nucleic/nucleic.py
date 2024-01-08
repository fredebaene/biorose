"""
This module  implements a class representing a nucleic acid. The class 
provides relevant methods to analyze the nucleic acids.
"""


from biorose.sequence.sequence import Sequence
from typing import Optional


class _NucleicAcid(Sequence):
    def __init__(self, seq: str, id: Optional[str] = None) -> None:
        super().__init__(seq=seq, id=id)
