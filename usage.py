from datetime import datetime

from camping.api import CampingAPI

a = CampingAPI(
    campground_id=234059, start_date=datetime.now(), end_date=datetime(2023, 7, 22)
)
a.check_campsite_availability()
