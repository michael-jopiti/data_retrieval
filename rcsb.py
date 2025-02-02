import requests, os, json
from Bio.PDB import PDBList

from rcsbsearchapi import rcsb_attributes as attrs

def fetch(met="Testosterone"):
    """
    Accessing RCSB PDB database
        - Official website @ https://www.rcsb.org/
        - Official API documentation @ https://data.rcsb.org/#data-api
        - Download Documentation @ https://data.rcsb.org/redoc/rcsb-restful-api-docs.json
        - Example notebooks @ https://github.com/rcsb/py-rcsbsearchapi/blob/master/notebooks/quickstart.ipynb


    |_> make sure to istall Biopython (Bio.PDB), and rcsbsearchapi library @ https://rcsbsearchapi.readthedocs.io/en/latest/
    """
    print(fetch.__doc__)
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/RCSB_PDB.txt"
    
    # url = "https://search.rcsb.org/rcsbsearch/v2/query"

    # Query for metabolite's (searched by UniProt ID) first interacting hit 
    url = f"https://rest.uniprot.org/uniprotkb/search?query={met}&format=json"

    response = requests.get(url, headers=None).json()
    # print([print(entry["primaryAccession"]) for entry in response["results"]])
    
    interacting_partner = [entry["primaryAccession"] for entry in response["results"]][0]


    #  with investigational or experimental drugs bound
    q1 = attrs.rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession == interacting_partner
    q2 = attrs.rcsb_entity_source_organism.scientific_name == "Homo sapiens"
    q3 = attrs.drugbank_info.drug_groups == "investigational"
    q4 = attrs.drugbank_info.drug_groups == "experimental"

    # Structures matching UniProt ID P00533 AND from humans
    #  AND (investigational OR experimental drug group)
    query = q1 & q2 & (q3 | q4)

    with open(filename, "w") as f:
        for i, hit in enumerate(list(query())):
            f. write(
                    (
                    f"Hit #{i}: {hit} \n"
                    f"{'-' * 30}\n"
                )
            )

        print(f"Data saved to: {filename}")