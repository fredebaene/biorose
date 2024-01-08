from biorose.nucleic.dna import DNA
from pathlib import Path
import pytest


_DATA_DIR = Path(__file__).parent.parent / "data"


@pytest.mark.parametrize(
    "seq_file, exp_res",
    [
        ("dna_sequence_001.txt", "20 12 17 21"),
        ("dna_sequence_002.txt", "208 271 260 257"),
    ]
)
def test_monomer_counting(seq_file, exp_res):
    """
    This test checks if the `.count_monomers()` method correctly calculates 
    the frequencies of each of the possible monomers in the sequence.
    """
    file_path = _DATA_DIR / seq_file
    with open(file_path, "r") as f:
        seq = f.read().strip()
    dna = DNA(seq)
    dna.count_monomers()
    assert dna.monomer_counts == exp_res