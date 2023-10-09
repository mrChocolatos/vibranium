import requests


def test_check_status_code(url):
    assert requests.get(url).status_code == 200
