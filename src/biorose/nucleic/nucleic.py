"""
This module  implements a class representing a nucleic acid. The class 
provides relevant methods to analyze the nucleic acide.
"""


class NucleicAcid:
    def __init__(self, seq: str, id: str = None) -> None:
        self._id = id
        self_seq = seq