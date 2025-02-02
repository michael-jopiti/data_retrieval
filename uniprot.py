import requests, json, os

def fetch(met="testosterone"):
    """
    Accessing UniProt database
        - Official website link: https://www.uniprot.org/
        - API documentation link: https://www.uniprot.org/api-documentation/uniprotkb
        - Query syntax: https://www.uniprot.org/help/text-search

    -> Limit of 25 results from API calls
    """
    print(fetch.__doc__)

    url = f"https://rest.uniprot.org/uniprotkb/search?query={met}+binding&format=json"
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/UniProt_{met}"

    response = requests.get(url, headers=None)

    if response.status_code == 200:
        data = response.json()
        print(f"Data received: {len(data['results'])} entries")

        # Open the parsed file to write data
        with open(filename + "_parsed.txt", "w") as f_parsed:
            for i, key in enumerate(data['results']):
                # Get the protein's UniProt ID
                uniProtId = key.get('uniProtkbId', 'No UniProt ID found')
                
                # Get the protein's full name (value)
                protein_name = key.get('protein', {}).get('recommendedName', {}).get('fullName', {}).get('value', 'No protein name found')
                
                # Get the evidence code for the full name
                evidence_code = key.get('protein', {}).get('recommendedName', {}).get('fullName', {}).get('evidences', [{}])[0].get('evidenceCode', 'No evidence code found')
                
                # Get the protein sequence
                sequence = key.get('sequence', {}).get('value', 'No sequence found')

                # Format the parsed data to write to the file
                parsed_data = (
                    f"Protein #{i + 1}:\n"
                    f"  UniProt ID: {uniProtId}\n"
                    f"  Protein Name: {protein_name}\n"
                    f"  Evidence Code: {evidence_code}\n"
                    f"  Sequence: {sequence}\n"
                    f"{'-' * 30}\n"
                )

                # Write the parsed data into the file
                f_parsed.write(parsed_data)

        print(f"Parsed data saved to {filename}_parsed.txt")

        # Optionally, save the entire response data to a JSON file
        with open(filename + ".txt", "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}.txt")

        return 

    else:
        print(f"Failed to retrieve data from {url}: {response.status_code}")
