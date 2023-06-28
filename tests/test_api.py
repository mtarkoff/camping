from camping.api import CampingAPI


def test_api_key_to_header():
    my_fake_key: str = "not_a_key"
    assert CampingAPI(my_fake_key).headers.get("apikey") == my_fake_key
