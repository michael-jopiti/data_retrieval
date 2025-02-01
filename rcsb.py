import requests, os

def fetch():
    """
    Accessing RCSB PDB database
        - Official website @ https://www.rcsb.org/
        - Official API documentation @ https://data.rcsb.org/#data-api
    """
    print(fetch.__doc__)

    # url = "https://search.rcsb.org/rcsbsearch/v2/query?json={\"query\":{\"type\":\"terminal\",\"service\":\"text\",\"parameters\":{\"value\":\"testosterone\"}},\"return_type\":\"entry\"
    url = "not_RCSB.net"
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/RCSB.txt"

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print("Data saved to kegg_testosterone.txt")
    else:
        print(f"Failed to retrieve RCSB data: {response.status_code}")