"""
This module  implements a class representing a nucleic acid. The class 
provides relevant methods to analyze the nucleic acide.
"""


from biorose.sequence.sequence import Sequence


class NucleicAcid(Sequence):
    _MONOMERS = "ACGT"

    def __init__(self, seq: str, id: str = None) -> None:
        super().__init__(seq=seq, id=id)
