import requests, os

def fetch():
    """
        Accessing KEGG database
        - Official website link: https://www.kegg.jp/kegg/
        - API documentation link: https://www.kegg.jp/kegg/rest/keggapi.html
    """
    print(fetch.__doc__)

    url = "https://rest.kegg.jp/find/compound/testosterone"
    os.makedirs("outputs", exist_ok=True)
    filename = "outputs/KEGG.txt"

    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print("Data saved to kegg_testosterone.txt")
    else:
        print(f"Failed to retrieve KEGG data: {response.status_code}")