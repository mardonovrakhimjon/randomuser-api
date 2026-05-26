import requests

from config import TOKEN

class RandomClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_cultures(self):
        url = f"{self.base_url}/api/Misc/Cultures"

        headers = {
            "X-Api-Key": TOKEN
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def get_random_address(self):
        url = f"{self.base_url}/api/Misc/Random-Address"

        headers = {"X-Api-Key": TOKEN}
        query_params = {
            "culture": "en",
            "number": 32
        }

        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    

print(RandomClient().get_random_address())
