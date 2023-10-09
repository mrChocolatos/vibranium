import pytest

from lesson_7.dog_api import DogClient
from lesson_7.breeds import BREEDS


class TestDogApi:

    @pytest.mark.parametrize('breed', ("hound", "basenji", "bulldog"))
    def test_get_list_dogs(self, dog_endpoint, breed):
        dog_client = DogClient(dog_endpoint)
        response = dog_client.get_list_dog_images_by_breed(breed)
        breeds_from_response = dog_client.get_breed_from_list_urls(response["message"])
        assert breeds_from_response.count(breed) == len(breeds_from_response)

    def test_get_list_all_breeds(self, dog_endpoint):
        dog_client = DogClient(dog_endpoint)
        response = dog_client.get_list_dog_breeds()
        assert BREEDS == response["message"] and response["status"] == "success"

    def test_get_random_image_by_breed(self, dog_endpoint):
        dog_client = DogClient(dog_endpoint)
        response = dog_client.get_random_breed_image()
        response_breed = dog_client.get_breed_from_response_url(response["message"])
        assert response_breed in BREEDS

    @pytest.mark.parametrize('breed', ("hound", "basenji", "bulldog"))
    def test_get_list_all_sub_breeds(self, dog_endpoint, breed):
        dog_client = DogClient(dog_endpoint)
        response = dog_client.get_list_all_sub_breeds(breed)
        assert BREEDS[breed] == response["message"]

    @pytest.mark.parametrize('breed', ("hound", "basenji", "bulldog"))
    def test_get_list_random_images_by_breed(self, dog_endpoint, breed):
        dog_client = DogClient(dog_endpoint)
        response = dog_client.get_list_random_images_by_breed(breed)
        assert dog_client.get_breed_from_response_url(response["message"]) == breed
