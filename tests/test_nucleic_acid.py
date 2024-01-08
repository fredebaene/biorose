from biorose.nucleic.dna import DNA
import pytest


@pytest.mark.parametrize(
    "seq, exp_res",
    [
        (
            (
                "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCT"
                "GATAGCAGC"
            ),
            "20 12 17 21",
        ),
        (
            (
                "GGATTCCTATCACATACACCTAGTGAGTCGGCTCCAGTTCACAGTGCACACATTCGTACAT"
                "GGGGGCTCCGCATCGCGGCAGCTATCTCGTGATGCAACCTAAAAAGAGTTTAGTAGCCCCA"
                "AGATGTCGCCAATCTGGATAGCTCTGGGACTCAATATCTAATACCCTGGTTTCCGCCCTCG"
                "CCAACGGGCCCCATACGCTTTACCTATCTCTTACTCAGGATTTGTCGACTCACCGGCACTC"
                "CGGACAGATCTTAAGACACGCCCTGCAGTTATTTGGTGAGATTTGCAATGATCCAACAAGA"
                "TGCGGTTCCTTGTTTACTGCTCATGGGACTCACAGTACTACACGCCGCGACGTTTTCGGCT"
                "AGGGCGTTGCCGACCTCCTCTACGGTGAAGACAATCCGCGACGTCGCATCTTCGTGTTGAG"
                "CACGATGAATTCACTTGTATGTAGTGCATGCTTTCGTGAGCATCGGTTTAGCCGCGCATCG"
                "CAATCCTTGTCGAATGCTATTAGCCCACCAGAAACCCGCGGGCGACGCTGGTACTGGTGGC"
                "TCGGCTGACACTGAGATCGGCCTGGTGCTAAATCTATGGTCTACCACCGTGCAGCTCTAAT"
                "TGAGAGTGCCCTTTTCTGACTCTCCTCGTGATAGGCGTGTGTACACGGGAGAGGGACATTG"
                "GACCAAACCACCAGGCTAGGAACTGATTTTGGAGATGGCATGCCGTCTCACCAGGGGACGC"
                "GCTGCTCCTGGCGCCGCGAGTAGTTATTGTCTCTGGCGGGATTCTGCCGCTTAGTAACTAT"
                "TGTGTCTCGTTCCTATAGCAGTGCCTCGGGTTACCAACGCCTGCGTCTTCGCCCCAAGCCA"
                "AGGTCTCCGCATGGTGGTACTGGGCATGCGGTCGTGCTCCGCAAAGATTTAAGATTTCAGA"
                "CTCGTTGGGCACTACGAATAGCGTGGGTGGGCGGCGCAGGTGATTCATGTGAAGAACCATA"
                "TAATTTAGGTTTGCTCCTAT"
            ),
            "208 271 260 257",
        )
    ]
)
def test_monomer_counting(seq, exp_res):
    """
    This test checks if the `.count_monomers()` method correctly calculates 
    the frequencies of each of the possible monomers in the sequence.
    """
    na = DNA(seq)
    na.count_monomers()
    assert na.monomer_counts == exp_res