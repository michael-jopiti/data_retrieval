import requests, os
import pandas as pd
import json
from chembl_webresource_client.new_client import new_client

from rdkit import Chem
from rdkit.Chem import Draw

def fetch(met="Testosterone"):
    """
    Accessing ChEMBL database
    - Official website link @ https://www.ebi.ac.uk/chembl/
    - Official API documentation @ https://www.ebi.ac.uk/chembl/api/data/docs
    - Python webresource libraray @ https://github.com/chembl/chembl_webresource_client
     |_ Make sure to pip install chembl_webresource_client
    """
    print(fetch.__doc__)

    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/ChEMBL_{met}"


    # Search for molecular ID in ChEMBL
    compound_data = new_client.molecule.search(met)
    
    # Convert QuerySet to list and then to JSON formatted string
    compound_data_list = list(compound_data)
    json_compound_data = json.dumps(compound_data_list, indent=4)  # Converts to JSON formatted string

    # Save data to file
    with open(filename + "_raw" + ".json", "w") as f:
        f.write(json_compound_data)

    # for i, key in enumerate(compound_data[0].keys()):
    #     print(f"Key #{i}: {key}")

    metabolite_ID = compound_data[0]['molecule_chembl_id']
    metabolite_smiles = compound_data[0]['molecule_structures']['canonical_smiles']

    print(f"{met}'s ID: {metabolite_ID}")
    print(f"{met}' canonical SMILES: {metabolite_smiles}")

    target_data = compound_data[0].get('target', [])
    print(len(target_data))

    mol = Chem.MolFromSmiles(metabolite_smiles)
    # Draw molecule
    Draw.MolToFile(mol, f"outputs/{met}_molecules.png", size=(300, 300))

    # Step 1: Search for Cholesterol in ChEMBL to get its ChEMBL ID & SMILES
    # compound_query = new_client.molecule.search(met)
    # if not compound_query:
    #     print(f"No ChEMBL ID found for {met}")
    #     return

    # cholesterol_chembl_id = compound_query[0]['molecule_chembl_id']
    # smiles = compound_query[0].get('molecule_structures', {}).get('canonical_smiles', 'No SMILES found')
    # print(f"Found ChEMBL ID for {met}: {cholesterol_chembl_id}")
    # print(f"SMILES: {smiles}")

    # # Step 2: Fetch binding site information for Cholesterol
    # url = f"https://www.ebi.ac.uk/chembl/api/data/binding_site.json?molecule_chembl_id={cholesterol_chembl_id}"
    # response = requests.get(url)

    # if response.status_code == 200:
    #     data = response.json()
    #     with open(filename, "w") as f:
    #         f.write(f"ChEMBL ID: {cholesterol_chembl_id}\n")
    #         f.write(f"SMILES: {smiles}\n\n")
    #         for site in data.get("binding_sites", []):
    #             f.write(f"Binding Site ID: {site.get('site_id', 'N/A')}\n")
    #             f.write(f"Target Name: {site.get('target_pref_name', 'N/A')}\n")
    #             f.write(f"Target ChEMBL ID: {site.get('target_chembl_id', 'N/A')}\n")
    #             f.write(f"{'-'*40}\n")

    #     print(f"Data saved to {filename}")

    # else:
    #     print(f"Failed to retrieve ChEMBL data: {response.status_code}")