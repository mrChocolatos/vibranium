import pytest

from lesson_7.brewery_api import BreweryClient
from lesson_7.brewery_static import BREWERY_LIST_KEYS, BREWERY_LIST_IDS


class TestsBrewery:

    def test_check_get_list_all_breweries_keys(self, brewery_endpoint):
        brewery = BreweryClient(brewery_endpoint)
        response = brewery.get_list_all_breweries()
        assert list(response[0].keys()) == BREWERY_LIST_KEYS

    @pytest.mark.parametrize('city', ("san_diego", "norman", "austintown", "jung-gu"))
    def test_get_list_all_breweries_by_city(self, brewery_endpoint, city):
        brewery = BreweryClient(brewery_endpoint)
        response = brewery.get_list_all_breweries_by_city(city)
        assert brewery.check_field_in_list_breweries(city, response, "city")

    @pytest.mark.parametrize('city', ("Cooper", "cross", "Brewing"))
    def test_get_list_all_breweries_by_name(self, brewery_endpoint, city):
        brewery = BreweryClient(brewery_endpoint)
        response = brewery.get_list_all_breweries_by_name(city)
        assert brewery.check_name_in_list_breweries(city, response)

    @pytest.mark.parametrize('brewery_id', BREWERY_LIST_IDS)
    def test_get_brewery_by_id(self, brewery_endpoint, brewery_id):
        brewery = BreweryClient(brewery_endpoint)
        response = brewery.get_brewery_by_id(brewery_id)
        assert response["id"] == brewery_id

    @pytest.mark.parametrize('state', ("new_york", "ohio", "minnesota", "texas"))
    def test_get_list_all_breweries_by_state(self, brewery_endpoint, state):
        brewery = BreweryClient(brewery_endpoint)
        response = brewery.get_list_all_breweries_by_state(state)
        assert brewery.check_field_in_list_breweries(state, response, "state")
