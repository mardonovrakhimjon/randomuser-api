import requests

from config import TOKEN

class FinanceClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_crypto_address(self):
        url = f"{self.base_url}/api/Finance/CryptoAddress"

        headers = {
            "X-Api-Key": TOKEN
        }
        query_params = {
            "cryptoType": "Bitcoin",
        }
        
        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


    def get_crypto_address_types(self):
        url = f"{self.base_url}/api/Finance/CryptoAddress/types"

        headers = {
            "X-Api-Key": TOKEN
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_countries_code(self, countryCode):
        url = f"{self.base_url}/api/Finance/Iban/{countryCode}"

        headers = {
            "X-Api-Key": TOKEN
        }
        path_params = {
            "countryCode": countryCode
        }

        response = requests.get(url, headers=headers, params=path_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_crypto_countries(self):
        url = f"{self.base_url}/api/Finance/Countries"

        headers = {
            "X-Api-Key": TOKEN
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_vat_validator(self):
        url = f"{self.base_url}/api/Finance/Vat/Validator"

        headers = {
            "X-Api-Key": TOKEN
        }

        query_params = {
            "vat": "vat",
            "country": "USA"
        }

        response = requests.post(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


client = FinanceClient()
# print(client.get_crypto_address())
# print(client.get_crypto_address_types())
# print(client.get_countries_code("US"))
# print(client.get_crypto_countries())
# print(client.get_vat_validator())