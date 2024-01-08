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
        self._rev_comp = None

    @property
    def rev_comp(self):
        return self._rev_comp

    def transcribe_coding_strand(self) -> RNA:
        """
        This method transcribes the DNA sequence as it were a coding strand 
        and returns an instance of `RNA`.

        Returns:
            RNA: an instance of `RNA`.
        """
        return RNA(seq="".join(["U" if i == "T" else i for i in self._seq]))
    
    def get_rev_comp(self) -> None:
        """
        Get the reverse complement of a DNA sequence. A DNA molecule forms a 
        double helix. Both strands run in the opposite direction. Base pairs 
        are always formed between adenine (A) and thymine (T) or cytosine (C) 
        and guanine (G). Therefore, the primary structure of the coding strand 
        can be used to derive the primary structure of the non-coding strand, 
        and vice versa.
        """
        complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
        self._rev_comp = "".join([complement[nt] for nt in self._seq[-1::-1]])