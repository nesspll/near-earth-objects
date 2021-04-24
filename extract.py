"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # neo collections
    coll_neos = []
    with open(neo_csv_path, 'r') as csv_neos:
        neos_reader = csv.DictReader(csv_neos)
        for row in neos_reader:
            diameter = float('nan')
            name = None
            if (row['diameter'] != '' and row['diameter'] != None):
                diameter = float(row['diameter'])
            if (row['name'] != '' and row['name'] != None):
                name = row['name']
            neo_found = NearEarthObject(designation=row['pdes'], name=name, diameter=diameter, hazardous=row['pha'])
            coll_neos.append(neo_found)
    return coll_neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    coll_cat = []
    with open(cad_json_path, 'r') as cad_json_file:
        cad_file = json.load(cad_json_file)
        for approach_item in cad_file['data']:
            ca_item = dict(zip(cad_file['fields'], approach_item))
            coll_cat.append(CloseApproach(designation=ca_item['des'], time=ca_item['cd'], distance=float(ca_item['dist']),
                                          velocity=float(ca_item['v_rel'])))
    return coll_cat

# print(load_neos('data/neos.csv'))
