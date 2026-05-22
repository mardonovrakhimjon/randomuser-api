import requests



class RandomClient:
    def __init__(self):
        self.base_url = "https://randommer.io"

    def get_cultures(self):
        url = f"{self.base_url}/api/Misc/Cultures"

        headers = {
            "X-Api-Key": "17e2134fdcc64646add29d6807821072"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    

print(RandomClient().get_cultures())
