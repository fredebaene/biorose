from biorose.nucleic.nucleic import NucleicAcid
import pytest


@pytest.mark.parametrize(
    "seq, exp_res",
    [
        (
            (
                "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCT"
                "GATAGCAGC"
            ),
            "20 12 17 21"
        )
    ]
)
def test_monomer_counting(seq, exp_res):
    """
    This test checks if the `.count_monomers()` method correctly calculates 
    the frequencies of each of the possible monomers in the sequence.
    """
    na = NucleicAcid(seq)
    na.count_monomers()
    assert na.monomer_counts == exp_res