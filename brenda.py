import os, json
from dotenv import load_dotenv
from zeep import Client, helpers
import hashlib

os.makedirs("outputs", exist_ok=True)
filename = "outputs/BRENDA_response.json"

load_dotenv()

class Account:
    """ Class to store information about user """
    def __init__(self, email, password):
        self.email = email
        self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    

def fetch():
    """
    Accessing BRENDA database
        - Official website @  https://www.brenda-enzymes.org/
        - API documentation @  https://www.brenda-enzymes.org/soap.php
        - After registration to the website -> download SOAPpy and get the personal API key at:  
        https://www.brenda-enzymes.org/soap.php#python
    """
    print(fetch.__doc__)
    
    account = Account(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
    
    # Check if the file exists
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping API call.")
    else:
        # BRENDA WSDL & Authentication
        wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
        client = Client(wsdl)

        # API Parameters
        parameters = (
            account.email, account.password, "ecNumber*1.1.1.1", "organism*Homo sapiens",
            "kmValue*", "kmValueMaximum*", "substrate*", "commentary*", "ligandStructureId*", "literature*"
        )

        # Make API Call
        result = client.service.getKmValue(*parameters)
        
        # Convert into list instead of zeep class
        result = helpers.serialize_object(result)
        print(type(result))

        # Wrap response in a dict if it's a list
        resultJson = {"response": result}

        # Save response to file
        with open(filename, "w") as f:
            json.dump(resultJson, f, indent=4)

        print(f"Downloaded and saved to {filename}")

    # Load and print response from the saved file
    with open(filename, "r") as f:
        data = json.load(f)
        print(f"Keys in data: {data.keys()}")  # Check top-level keys

        print(f"Element present in the response {len(data['response'])}")
