import requests


class CampingAPI:
    BASE_URL: str = "https://ridb.recreation.gov/api/v1"


    def __init__(self, api_key: str):
        self.headers: dict = {"Accept": "application/json", "apikey": api_key}


    def get_endpoint(self, endpoint: str, params: dict) -> str:
        url = f"{self.BASE_URL}/{endpoint}"
        resp = requests.get(url, headers=self.headers, params=params)
        return resp.json()


    def get_campground_id(self, campground_name: str) -> str:
        endpoint: str = "facilities"
        params = {"query": campground_name, "limit": 1}
        resp = self.get_endpoint(endpoint=endpoint, params=params)
        campground_id = resp.get("RECDATA")
        return campground_id

    def get_available_campsites(self, campground_id: str, start_date, end_date):
        pass

