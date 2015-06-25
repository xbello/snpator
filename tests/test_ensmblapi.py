"""Tests for the Ensembl API shortcuts."""
import json
import os
from unittest import TestCase

import ensemblapi


class TestEnsemblAPI(TestCase):
    def test_can_extract_data_for_individual(self):
        with open(os.path.join(os.path.dirname(__file__),
                               "rs10050860.json")) as json_file:
            json_data = json.load(json_file)

        self.assertCountEqual(
            ensemblapi.get_individual("NA18576", json_data),
            [{"genotype": "C|C",
              "gender": "Female",
              "submission_id": "ss68942927",
              "individual": "NA18576"},
             {"genotype": "C|C",
              "submission_id": "ss44615098",
              "individual": "NA18576",
              "gender": "Female"}])


class TestOnlineAccesses(TestCase):
    def test_can_get_ensembl_json_for_rs(self):
        rs_json = ensemblapi.get_rs("rs10050860")
        self.assertEqual(
            rs_json["mappings"],
            [{"location": "5:96786506-96786506",
              "assembly_name": "GRCh38",
              "end": 96786506,
              "seq_region_name": "5",
              "strand": 1,
              "coord_system": "chromosome",
              "allele_string": "C/T",
              "start": 96786506}])

        self.assertTrue("genotypes" in rs_json.keys())
