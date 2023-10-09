import requests


class BreweryClient:
    def __init__(self, brewery_api):
        self.brewery_api = brewery_api

    def get_list_all_breweries(self):
        response = requests.get(self.brewery_api + "/breweries")
        return response.json()

    def get_list_all_breweries_by_city(self, city):
        response = requests.get(self.brewery_api + f"/breweries?by_city={city}")
        return response.json()

    def get_list_all_breweries_by_name(self, name):
        response = requests.get(self.brewery_api + f"/breweries?by_name={name}")
        return response.json()

    def get_list_all_breweries_by_state(self, name):
        response = requests.get(self.brewery_api + f"/breweries?by_state={name}")
        return response.json()

    def get_brewery_by_id(self, brewery_id):
        response = requests.get(self.brewery_api + f"/breweries/{brewery_id}")
        return response.json()

    def check_field_in_list_breweries(self, field_value: str, list_breweries: list, filed: str):
        field_value = field_value.split('_')
        field_value = " ".join([i.capitalize() for i in field_value])
        for item in list_breweries:
            if item[filed] != field_value:
                raise AssertionError(f"{field_value} not equal {item[filed]}")
        else:
            return True

    def check_name_in_list_breweries(self, name: str, list_breweries: list):
        name = name.lower()
        for item in list_breweries:
            if name not in item["name"].lower():
                raise AssertionError(f"{name} not in {item['name']}")
        else:
            return True
