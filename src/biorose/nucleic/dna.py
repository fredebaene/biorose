"""
This module  implements a class representing a deoxyribose nucleic acid. The 
class provides relevant methods to analyze DNA molecules.
"""


from biorose.nucleic.nucleic import _NucleicAcid
from biorose.nucleic.rna import RNA
from typing import Optional


class DNA(_NucleicAcid):
    _MONOMERS = "ACGT"

    def __init__(self, seq: str, id: Optional[str] = None) -> None:
        super().__init__(seq=seq, id=id)

    def transcribe_coding_strand(self) -> RNA:
        """
        This method transcribes the DNA sequence as it were a coding strand 
        and returns an instance of `RNA`.

        Returns:
            RNA: an instance of `RNA`.
        """
        return RNA(seq="".join(["U" if i == "T" else i for i in self._seq]))