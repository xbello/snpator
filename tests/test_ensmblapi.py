"""Tests for the Ensembl API shortcuts."""
from unittest import TestCase

import ensemblapi


class TestEnsemblAPI(TestCase):

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
