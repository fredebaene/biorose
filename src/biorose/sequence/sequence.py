"""
This module implements an interface that defines the methods each 
sequence-specific must implement.
"""


from abc import ABC


class Sequence(ABC):
    def __init__(self, seq: str, id: str = None) -> None:
        self._id = id
        self._seq = seq
        self._monomer_counts = {monomer: 0 for monomer in self._MONOMERS}

    @property
    def monomer_counts(self):
        return " ".join([str(i) for i in self._monomer_counts.values()])
    
    def count_monomers(self) -> None:
        """
        This method calculates the frequency of each of the monomers that can 
        occur in the sequence.
        """
        for monomer in self._seq:
            self._monomer_counts[monomer] += 1

    def _initialize_monomer_counts(self) -> None:
        """
        This method initializes a dictionary to hold the monomer frequencies 
        in the sequence. This dictionary starts out with all count values of 
        zero for every monomer.
        """
        