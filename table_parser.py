"""Parse a SNPs list of genotype."""
# Threshold for the number of "rs" in a line to be the header.
THRESHOLD = 5


def dict_into_table(rs_header, genotypes):
    """Return a list with lines TAB splitted with the genotypes."""
    header = "\t" + "\t".join(rs_header)

    lines = [header]

    individuals = {}

    #for rs, genotype in genotypes.items():
    for rs in rs_header:
        genotype = genotypes[rs]
        for individual in genotype.keys():
            individuals.setdefault(individual, [])
            individuals[individual].append(genotype[individual])

    for individual, genotypes in individuals.items():
        lines.append("\t".join([individual, "\t".join(genotypes)]))

    return lines


def genotype_to_dict(all_genotypes):
    """Return a list of dict with the genotypes in the dict."""

    rows = {}

    for rs, individuals in all_genotypes.items():
        rows.setdefault(rs, {})
        for individual, genotypes in individuals.items():
            rows[rs].setdefault(individual, "")
            for genotype in genotypes:
                rows[rs][individual] =\
                    genotype["genotype"].replace("|", "")
                break

    return rows


def get_rs(filename):
    """Return a list with the rs of the file."""
    rs_list = []
    with open(filename) as snp_table:
        for line in snp_table:
            columns = line.split()

            if len([_ for _ in columns if _.startswith("rs")]) >= THRESHOLD:
                rs_list = columns

    return rs_list
