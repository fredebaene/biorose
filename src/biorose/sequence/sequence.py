"""
This module implements an interface that defines the methods each 
sequence-specific must implement.
"""


from typing import Protocol, runtime_checkable


class Sequence(Protocol):
    def count_monomers(self) -> None:
        ...