"""Get a list of rs from Ensembl and turns them into a table."""
import ensemblapi
import table_parser


def main(matrix):
    """Return a list of lines with the checks of the rs in the matrix."""

    rs_list = table_parser.get_rs(matrix)

    if rs_list:
        checks = ensemblapi.get_genotypes(rs_list, ["NA10830", "NA10831"])

        genotypes = table_parser.genotype_to_dict(checks)

        return "\n".join(table_parser.dict_into_table(rs_list, genotypes))
    else:
        return "No rs header detected"


if __name__ == "__main__":
    import tkinter
    from tkinter.filedialog import askopenfilename, asksaveasfile

    root = tkinter.Tk()
    filename = askopenfilename()
    lines = main(filename)

    with asksaveasfile() as writing_handler:
        writing_handler.writelines(lines)
