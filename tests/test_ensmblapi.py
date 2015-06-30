"""Tests for the Ensembl API shortcuts."""
import json
import os
from unittest import mock, TestCase

from requests.models import Response

import ensemblapi


class FakeJSON(object):
    def __init__(self, rs):
        self.rs = rs

    def json(self):
        return fixed_get_rs(self.rs)


def avoid_call(request_generator):
    return [FakeJSON(_.url.split("?")[0].split("/")[-1])
            for _ in request_generator]


def fixed_get_rs(rs_id):
    with open(os.path.join(os.path.dirname(__file__),
                           "{}.json".format(rs_id))) as json_file:
        return json.load(json_file)


class TestEnsemblAPI(TestCase):
    def setUp(self):
        self.json_data = self._load_json("rs10050860")
        self.json_data2 = self._load_json("rs10065172")
        self.genotype_json = self._load_json("genotype_test")

    def _load_json(self, json_id):
        with open(os.path.join(os.path.dirname(__file__),
                               "{}.json".format(json_id))) as json_file:
            return json.load(json_file)

    def test_can_extract_data_for_individual(self):

        self.assertCountEqual(
            ensemblapi.get_individual("NA18576", self.json_data),
            [{"genotype": "C|C",
              "gender": "Female",
              "submission_id": "ss68942927",
              "individual": "NA18576"},
             {"genotype": "C|C",
              "submission_id": "ss44615098",
              "individual": "NA18576",
              "gender": "Female"}])

    @mock.patch("ensemblapi.requests.get")
    @mock.patch("ensemblapi.requests.models.Response.json")
    def test_can_get_ensembl_json_for_rs(self, json_mock, get_mock):
        get_mock.return_value = Response()
        json_mock.return_value = self.json_data

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

    @mock.patch("ensemblapi.erequests.map", side_effect=avoid_call)
    def test_can_get_a_list_of_rs(self, mock_get_rs):

        rs_list_json = ensemblapi.get_list_of_rs(["rs10050860",
                                                  "rs10065172"])

        self.assertCountEqual(
            rs_list_json, [self.json_data, self.json_data2])

    #@mock.patch("ensemblapi.get_rs", side_effect=fixed_get_rs)
    @mock.patch("ensemblapi.erequests.map", side_effect=avoid_call)
    def test_fill_a_rs_dict_with_values(self, mock_get_rs):
        self.maxDiff = None
        self.assertEqual(
            ensemblapi.get_genotypes(["rs10050860", "rs10065172"],
                                     ["NA18576"]),
            self.genotype_json)
