"""Parse a SNPs list of genotype."""

# Threshold for the number of "rs" in a line to be the header.
THRESHOLD = 5


def get_rs(filename):
    """Return a list with the rs of the file."""
    rs_list = []
    with open(filename) as snp_table:
        for line in snp_table:
            columns = line.split()

            if len([_ for _ in columns if _.startswith("rs")]) > THRESHOLD:
                rs_list = columns

    return rs_list
