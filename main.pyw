"""Get a list of rs from Ensembl and turns them into a table."""
import ensemblapi
import table_parser
from utils import get_ref_genotypes


def main(matrix):
    """Return a list of lines with the checks of the rs in the matrix."""

    rs_list = table_parser.get_rs(matrix)

    if rs_list:
        checks = ensemblapi.get_genotypes(rs_list, get_ref_genotypes())

        genotypes = table_parser.genotype_to_dict(checks)

        return "\n".join(table_parser.dict_into_table(rs_list, genotypes))
    else:
        return "No rs header detected"


if __name__ == "__main__":
    import tkinter
    from tkinter.filedialog import askopenfilename, asksaveasfile

    root = tkinter.Tk()
    filename = askopenfilename(title="Abrir archivo con matriz de genotipos")

    if filename:
        lines = main(filename)

        with asksaveasfile(
                title="Grabar resultados como...") as writing_handler:
            writing_handler.writelines(lines)
