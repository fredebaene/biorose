from biorose.nucleic.dna import DNA
from biorose.nucleic.rna import RNA
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
    seq_file_path = _DATA_DIR / seq_file
    with open(seq_file_path, "r") as f:
        seq = f.read().strip()
    dna = DNA(seq)
    dna.count_monomers()
    assert dna.monomer_counts == exp_res

@pytest.mark.parametrize(
    "dna_seq_file, exp_res_file",
    [("dna_sequence_003.txt", "rna_sequence_001.txt")]
)
def test_coding_strand_transcription(dna_seq_file, exp_res_file):
    """
    This test checks if the `.transcribe_coding_strand()` correctly 
    transcribes a `DNA` instance as if it were a coding strand. The method 
    must return an `RNA` instance.
    """
    dna_seq_file_path = _DATA_DIR / dna_seq_file
    exp_res_file_path = _DATA_DIR / exp_res_file
    with open(dna_seq_file_path, "r") as f:
        dna = DNA(f.read().strip())
    with open(exp_res_file_path, "r") as f:
        exp_res = f.read().strip()
    rna = dna.transcribe_coding_strand()
    assert isinstance(rna, RNA)
    assert rna.seq == exp_res