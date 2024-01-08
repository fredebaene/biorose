"""
This module implements an interface that defines the methods each 
sequence-specific must implement.
"""


from abc import ABC


class Sequence(ABC):
    def __init__(self, seq: str, id: str = None) -> None:
        self._id = id
        self_seq = seq

    def count_monomers(self) -> None:
        """
        This method calculates the frequency of each of the monomers that can 
        occur in the sequence.
        """
        raise NotImplementedError