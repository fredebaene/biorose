"""
This module  implements a class representing a deoxyribose nucleic acid. The 
class provides relevant methods to analyze RNA molecules.
"""


from biorose.nucleic.nucleic import _NucleicAcid
from typing import Optional


class RNA(_NucleicAcid):
    _MONOMERS = "ACGU"

    def __init__(self, seq: str, id: Optional[str] = None) -> None:
        super().__init__(seq=seq, id=id)