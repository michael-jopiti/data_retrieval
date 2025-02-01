import requests, json, os

def fetch():
    """
    Accessing UniProt database
        - Official website link: https://www.uniprot.org/
        - API documentation link: https://www.uniprot.org/api-documentation/uniprotkb
    """
    print(fetch.__doc__)

    url = "https://rest.uniprot.org/uniprotkb/search?query=testosterone+binding&format=json"
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/UniProt.txt"


    response = requests.get(url, headers=None)

    if response.status_code == 200:
        data = response.json()
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    else:
        print(f"Failed to retrieve data from {url}: {response.status_code}")