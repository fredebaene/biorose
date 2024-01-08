"""
This module  implements a class representing a nucleic acid. The class 
provides relevant methods to analyze the nucleic acide.
"""


from biorose.sequence.sequence import Sequence


class NucleicAcid(Sequence):
    _MONOMERS = {"A", "C", "G", "T"}

    def __init__(self, seq: str, id: str = None) -> None:
        self._id = id
        self_seq = seq

    def count_monomers(self) -> None:
        """
        This method calculates the frequency of each of the monomers that can 
        occur in the sequence.
        """
        self._monomer_counts = {monomer: 0 for monomer in self._MONOMERS}
