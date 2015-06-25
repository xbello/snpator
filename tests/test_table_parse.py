"""Test the table parser."""
from collections import OrderedDict
import json
import os
from unittest import TestCase

import table_parser


class TestParseTable(TestCase):
    def setUp(self):
        self.sample_file = os.path.join(os.path.dirname(__file__),
                                        "genotypesMatrixFormat.txt")

        self.genotype_json = {
            "rs10065172": {"NA18576":
                           [{"gender": "Female",
                             "individual": "NA18576",
                             "submission_id": "ss44615098",
                             "genotype": "C|C"},
                            {"gender": "Female",
                             "individual": "NA18576",
                             "submission_id": "ss68942927",
                             "genotype": "C|C"}]}}

        with open(os.path.join(os.path.dirname(__file__),
                               "genotype_test.json")) as json_file:
            self.multiple_rs_genotype = json.load(json_file)

    def test_parse_genotype_json_into_dict(self):
        self.assertEqual(
            table_parser.genotype_to_dict(self.genotype_json),
            {"rs10065172": {"NA18576": "CC/CC"}})

        self.assertEqual(
            table_parser.genotype_to_dict(self.multiple_rs_genotype),
            {"rs10050860": {"NA18576": "CC/CC"},
             "rs10065172": {"NA18576": "TT"}})

    def test_parse_genotype_dict_into_table(self):
        self.assertEqual(
            table_parser.dict_into_table({"rs10065172": {"NA18576": "CC/CC"}}),
            ["\trs10065172", "NA18576\tCC/CC"])

        rs_dict = OrderedDict()
        rs_dict["rs10050860"] = {"NA18576": "CC/CC"}
        rs_dict["rs10065172"] = {"NA18576": "TT"}

        self.assertEqual(
            table_parser.dict_into_table(rs_dict),
            ["\trs10050860\trs10065172", "NA18576\tCC/CC\tTT"])

    def test_we_get_the_rs_line(self):
        self.assertEqual(table_parser.get_rs(self.sample_file)[:2],
                         ["rs10050860", "rs10065172"])
