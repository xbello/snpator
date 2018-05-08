import os


def get_ref_genotypes(src="genotypes.txt"):
    """Return a list with the reference genotypes from a file."""
    ref_file = os.path.join(os.path.dirname(__file__), src)

    with open(ref_file) as refs:
        genotypes = [_.rstrip() for _ in refs.readlines() if _.rstrip()]

    return genotypes
