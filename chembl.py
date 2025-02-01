import requests, os
def fetch():
    """
    Accessing ChEMBL database
    - Official website link @ https://www.ebi.ac.uk/chembl/
    - Official API documentation @ https://www.ebi.ac.uk/chembl/api/data/docs
    """
    print(fetch.__doc__)

    url = "https://www.ebi.ac.uk/chembl/api/data/mechanism.json?target_chembl_id=CHEMBL148"
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/ChEMBL.txt"

    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print("Data saved to chembl_testosterone.txt")
    else:
        print(f"Failed to retrieve KEGG data: {response.status_code}")