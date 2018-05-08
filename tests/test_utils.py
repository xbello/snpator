import utils


def test_can_get_genotypes_from_file():
    assert utils.get_ref_genotypes("tests/test_genotypes.txt") == \
        ["GENO1", "GENO2"]


def test_empty_lines_not_included():
    assert utils.get_ref_genotypes("tests/test_genotypes_empty.txt") == \
        ["GENO1", "GENO2", "GENO3"]

