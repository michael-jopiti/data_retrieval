import requests, os

def fetch(met="testosterone"):
    """
    Accessing KEGG database for the given metabolite
        - Official website link: https://www.kegg.jp/kegg/
        - API documentation link: https://www.kegg.jp/kegg/rest/keggapi.html
    """
    print(fetch.__doc__)

    # Search for the compound by metabolite name
    url_compound_ID = f"https://rest.kegg.jp/find/compound/{met}"
    response_ID = requests.get(url_compound_ID).text

    # Extract the first compound ID from the search results
    compound_ids = [line.split('\t')[0] for line in response_ID.splitlines()]
    if not compound_ids:
        print(f"No compounds found for {met}.")
        return

    first_compound_id = compound_ids[0]  # Get the first compound ID
    print(f"Using compound ID: {first_compound_id}")

    # Fetch detailed data for the first compound ID
    url = f"https://rest.kegg.jp/get/{first_compound_id}"
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/KEGG_{met}.txt"

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"Data saved to {filename}")
    else:
        print(f"Failed to retrieve KEGG data for {first_compound_id}: {response.status_code}")

