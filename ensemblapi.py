"""Shortcuts to use the Ensembl REST API."""
import requests


def get_individual(individual, ensembl_json):
    """Return a list with the genotypes of the individual."""

    genotypes = []

    for individual_genotype in ensembl_json["genotypes"]:
        if individual in individual_genotype["individual"]:
            genotypes.append(individual_genotype)

    return genotypes


def get_rs(rs_id):
    """Return the JSON for a given rs_id."""
    ensembl_uri = \
        "http://rest.ensembl.org/variation/human/{}".format(rs_id) +\
        "?content-type=application/json;genotypes=1"

    json_response = requests.get(ensembl_uri).json()

    return json_response
