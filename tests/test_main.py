import main


def test_can_get_genotypes_from_file():
    assert main.get_ref_genotypes("tests/test_genotypes.txt") == \
        ["GENO1", "GENO2"]
