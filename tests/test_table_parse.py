"""Test the table parser."""
import os
from unittest import TestCase

import table_parser


class TestParseTable(TestCase):
    def setUp(self):
        self.sample_file = os.path.join(os.path.dirname(__file__),
                                        "genotypesMatrixFormat.txt")

    def test_we_get_the_rs_line(self):
        self.assertEqual(table_parser.get_rs(self.sample_file)[:2],
                         ["rs10050860", "rs10065172"])
