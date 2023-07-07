from datetime import datetime

import requests
from fake_useragent import UserAgent


class CampingAPI:
    BASE_URL: str = "https://www.recreation.gov/api"

    def __init__(self, campground_id: str, start_date: datetime, end_date: datetime):
        self.headers: dict = {"User-Agent": UserAgent().random}
        self.campground_id: str = campground_id
        self.check_in: datetime = start_date
        self.check_out: datetime = end_date
        self.num_days: int = (self.check_out - self.check_in).days

    def clean_start_date(self) -> str:
        start_date = datetime(self.check_in.year, self.check_in.month, 1)
        return f"{start_date.isoformat()}.000Z"

    def get_availability(self) -> dict:
        url = (
            f"{self.BASE_URL}/camps/availability/campground/{self.campground_id}/month"
        )
        params = {"start_date": self.clean_start_date()}
        resp = requests.get(url=url, headers=self.headers, params=params).json()
        return resp

    def check_campsite_availability(self):
        # filter campsite availability
        campsite_availability: dict = dict()
        for campsite_id, attributes in self.get_availability().get("campsites").items():
            campsite_availability[campsite_id] = sum(
                status
                for date, status in attributes.get("quantities").items()
                if status == 1
                and self.check_in
                <= datetime.strptime(date[:10], "%Y-%m-%d")
                < self.check_out
            )
        has_availability = [
            f"https://www.recreation.gov/camping/campsites/{campsite}"
            for campsite, days in campsite_availability.items()
            if days == self.num_days
        ]
        return has_availability
