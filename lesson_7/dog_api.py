import requests


class DogClient:
    def __init__(self, dog_endpoint):
        self.dog_endpoint = dog_endpoint

    def get_list_dog_breeds(self):
        response = requests.get(self.dog_endpoint + "/breeds/list/all")
        return response.json()

    def get_random_breed_image(self):
        response = requests.get(self.dog_endpoint + "/breeds/image/random")
        return response.json()

    def get_list_dog_images_by_breed(self, breed):
        response = requests.get(self.dog_endpoint + f"/breed/{breed}/images")
        return response.json()

    def get_list_all_sub_breeds(self, breed):
        response = requests.get(self.dog_endpoint + f"/breed/{breed}/list")
        return response.json()

    def get_list_random_images_by_breed(self, breed):
        response = requests.get(self.dog_endpoint + f"/breed/{breed}/images/random")
        return response.json()

    def get_breed_from_response_url(self, url: str):
        result = url.split("/")
        breed = result[4].split('-')
        return breed[0]

    def get_breed_from_list_urls(self, list_urls: list):
        list_breed = []
        for url in list_urls:
            list_breed.append(self.get_breed_from_response_url(url))
        return list_breed
