"""Shortcuts to use the Ensembl REST API."""
import requests


def get_rs(rs_id):
    """Return the JSON for a given rs_id."""
    ensembl_uri = \
        "http://rest.ensembl.org/variation/human/{}".format(rs_id) +\
        "?content-type=application/json;genotypes=1"

    json = requests.get(ensembl_uri).json()
    print(json)

    return json
