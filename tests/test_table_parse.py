"""Test the table parser."""
import os
from unittest import TestCase

import table_parser


class TestParseTable(TestCase):
    def setUp(self):
        self.sample_file = os.path.join(os.path.dirname(__file__),
                                        "genotypesMatrixFormat.txt")

        self.genotype_json = [{"genotype": "C|C",
                               "gender": "Female",
                               "submission_id": "ss68942927",
                               "individual": "NA18576"},
                              {"genotype": "C|C",
                               "submission_id": "ss44615098",
                               "individual": "NA18576",
                               "gender": "Female"}]

    def test_parse_genotype_json_into_table(self):
        self.assertEqual(
            table_parser.genotype_to_lines(self.genotype_json),
            {"NA18576": "CC/CC"})

    def test_we_get_the_rs_line(self):
        self.assertEqual(table_parser.get_rs(self.sample_file)[:2],
                         ["rs10050860", "rs10065172"])
