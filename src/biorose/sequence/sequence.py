"""
This module defines a base class for biological sequences. Biological 
sequences comprise nucleic acids (DNA and RNA) and proteins (amino acid 
sequences).
"""


from typing import Optional


class _Sequence:
    """A base class for biological sequences"""
    def __init__(self, seq: str, id: Optional[str] = None) -> None:
        self._id = id
        self._seq = seq
        self._monomer_counts = {monomer: 0 for monomer in self._MONOMERS}

    @property
    def id(self):
        return self._id

    @property
    def monomer_counts(self):
        return " ".join([str(i) for i in self._monomer_counts.values()])
    
    @property
    def seq(self):
        return self._seq
    
    def count_monomers(self) -> None:
        """
        This method calculates the frequency of each of the monomers that can 
        occur in the sequence.
        """
        for monomer in self._seq:
            self._monomer_counts[monomer] += 1