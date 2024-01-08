"""
This module  implements a class representing a deoxyribose nucleic acid. The 
class provides relevant methods to analyze DNA molecules.
"""


from biorose.nucleic.nucleic import _NucleicAcid
from typing import Optional


class DNA(_NucleicAcid):
    _MONOMERS = "ACGT"

    def __init__(self, seq: str, id: Optional[str] = None) -> None:
        super().__init__(seq=seq, id=id)