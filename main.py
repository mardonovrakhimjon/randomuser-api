import requests



class RammerClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_card(self):
        url = f"{self.base_url}/api/Card/"

        headers = {
            "X-Api-Key": "27ed4274794b4b8f970d384778f42752"
        }
        query_params = {
            "type": "Visa",
        }

        response = requests.get(url, headers=headers, params=query_params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


    def get_get_card_types(self):
        url = f"{self.base_url}/api/Card/Types"

        headers = {
            "X-Api-Key": "27ed4274794b4b8f970d384778f42752"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None


client = RammerClient()
print(client.get_card())
print(client.get_get_card_types())
