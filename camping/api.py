class CampingAPI:
    BASE_URL: str = "https://ridb.recreation.gov/api/v1"

    def __init__(self, api_key: str):
        self.headers: dict = {"Accept": "application/json", "apikey": api_key}
