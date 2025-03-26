import requests

URL = "https://dummyjson.com"

class APIclient:
    def __init__(self, user_name, password): 
        self.base_url = URL
        self.auth_url = URL + "/auth/login"
        self.auth = {"username": user_name, "password": password}
        self.token = None

    def connectivity_test(self):
        response = requests.post(self.auth_url, json=self.auth)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return response.json()

