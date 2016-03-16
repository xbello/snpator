"""Shortcuts to use the Ensembl REST API."""
import requests
import erequests


def get_genotypes(rs_list, individuals):
    """Return a dict with rs as keys and a dict with individuals:genotypes."""
    all_rs = get_list_of_rs(rs_list)

    genotypes = {}.fromkeys(rs_list)

    for rs_json in all_rs:
        genotypes[rs_json["name"]] = {}
        for individual in individuals:
            genotypes[rs_json["name"]].setdefault(individual, [])
            genotypes[rs_json["name"]][individual] = \
                get_individual(individual, rs_json)

    return genotypes


def get_individual(individual, ensembl_json):
    """Return a list with the genotypes of the individual."""

    genotypes = []

    for individual_genotype in ensembl_json["genotypes"]:
        if individual in individual_genotype["sample"]:
            genotypes.append(individual_genotype)

    return genotypes


def get_list_of_rs(list_of_rs):
    """Return a list with all the Ensembl responses for a list of rs."""
    ensembl_uri = \
        "http://rest.ensembl.org/variation/human/{}" +\
        "?content-type=application/json;genotypes=1"

    # Create all the URL request strings
    list_of_urls = [ensembl_uri.format(_) for _ in list_of_rs]

    # Put every request in a pool (unsent)
    responses = (erequests.async.get(_) for _ in list_of_urls)

    # Send every request and get the JSON from each one.
    return [_.json() for _ in erequests.map(responses, size=len(list_of_urls))]


def get_rs(rs_id):
    """Return the JSON for a given rs_id."""
    ensembl_uri = \
        "http://rest.ensembl.org/variation/human/{}".format(rs_id) +\
        "?content-type=application/json;genotypes=1"

    json_response = requests.get(ensembl_uri).json()

    return json_response
