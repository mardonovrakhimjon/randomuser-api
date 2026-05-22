import requests



class FinanceClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_crypto_address(self):
        url = f"{self.base_url}/api/Finance/CryptoAddress"

        headers = {
            "X-Api-Key": "17e2134fdcc64646add29d6807821072"
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
            "X-Api-Key": "17e2134fdcc64646add29d6807821072"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_crypto_countries(self):
        url = f"{self.base_url}/api/Finance/Countries"

        headers = {
            "X-Api-Key": "17e2134fdcc64646add29d6807821072"
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
            "X-Api-Key": "17e2134fdcc64646add29d6807821072"
        }

        query_params = {
            "vat": "vat",
        }
        query_params = {
            "country": "country",
        }

        
        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


client = FinanceClient()
# print(client.get_crypto_address())
# print(client.get_crypto_address_types())
# print(client.get_crypto_countries())
print(client.get_vat_validator())