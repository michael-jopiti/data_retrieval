import requests
import json

def save_data(url, filename, headers=None):
    """Fetch data from the given URL and save it as a JSON file."""
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    else:
        print(f"Failed to retrieve data from {url}: {response.status_code}")

def main():
    """Retrieve testosterone-binding enzymes from multiple databases and save to files."""
    
    # UniProt
    print(f"Accessing UniProt database" +
          "\n\t Official website @ https://www.uniprot.org/" +
          "\n\t API documentation @ https://www.uniprot.org/api-documentation/uniprotkb")

    uniprot_url = "https://rest.uniprot.org/uniprotkb/search?query=testosterone+binding&format=json"
    save_data(uniprot_url, "uniprot_testosterone.json")

    # KEGG (KEGG API does not return JSON, so we save as text)
    print(f"Accessing KEGG database" +
        "\n\t Official website @ https://www.kegg.jp/kegg/" +
        "\n\t API documentation @ https://www.kegg.jp/kegg/rest/keggapi.html")

    kegg_url = "https://rest.kegg.jp/find/compound/testosterone"

    response = requests.get(kegg_url)
    if response.status_code == 200:
        with open("kegg_testosterone.txt", "w") as f:
            f.write(response.text)
        print("Data saved to kegg_testosterone.txt")
    else:
        print(f"Failed to retrieve KEGG data: {response.status_code}")

    # RCSB PDB
    print(f"Accessing RCSB PDB database" +
    "\n\t Official website @ https://www.rcsb.org/" +
    "\n\t API documentation @ https://data.rcsb.org/#data-api")

    # rcsb_url = "https://search.rcsb.org/rcsbsearch/v2/query?json={\"query\":{\"type\":\"terminal\",\"service\":\"text\",\"parameters\":{\"value\":\"testosterone\"}},\"return_type\":\"entry\"}"
    # save_data(rcsb_url, "rcsb_testosterone.json")

    # ChEMBL
    print(f"Accessing RCSB PDB database" +
    "\n\t Official website @ https://www.ebi.ac.uk/chembl/" +
    "\n\t API documentation @ https://www.ebi.ac.uk/chembl/api/data/docs")

    chembl_url = "https://www.ebi.ac.uk/chembl/api/data/mechanism.json?target_chembl_id=CHEMBL148"
    save_data(chembl_url, "chembl_testosterone.json")

    # # BRENDA (Requires API key - replace YOUR_API_KEY)
    # brenda_headers = {"Authorization": "YOUR_API_KEY"}
    # brenda_url = "https://www.brenda-enzymes.org/soap.php"  # Modify if you have the correct API endpoint
    # save_data(brenda_url, "brenda_testosterone.json", headers=brenda_headers)

if __name__ == "__main__":
    main()
