from lesson_7.dog_api import DogClient


class TestDogApi:
    def test_get_list_dogs(self, dog_endpoint):
        dog_client = DogClient(dog_endpoint)
        assert dog_client.get_list_dog_images_by_breed("hound")
