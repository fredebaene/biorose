"""
This module implements an interface that defines the methods each 
sequence-specific must implement.
"""


from abc import ABC


class Sequence(ABC):
    def __init__(self, seq: str, id: str = None) -> None:
        self._id = id
        self._seq = seq
    
    def count_monomers(self) -> None:
        """
        This method calculates the frequency of each of the monomers that can 
        occur in the sequence.
        """
        self._monomer_counts = {monomer: 0 for monomer in self._MONOMERS}
        for monomer in self._seq:
            self._monomer_counts[monomer] += 1