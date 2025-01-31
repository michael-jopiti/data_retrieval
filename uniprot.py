import requests
import json

def main():
    """Retrieving testosterone binding proteins and saving to file"""
    url = "https://rest.uniprot.org/uniprotkb/search?query=testosterone+binding&format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open("testosterone_binding_proteins.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to testosterone_binding_proteins.json")
    else:
        print("Failed to retrieve data:", response.status_code)

if __name__ == "__main__":
    main()
