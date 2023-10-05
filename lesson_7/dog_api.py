import asyncio
import os
import aiohttp
import pytest
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
        response = requests.get(self.dog_endpoint+ f"/breed/{breed}/images")
        return response.json()

    def get_list_all_sub_breeds(self, breed):
        response = requests.get(self.dog_endpoint + f"/breed/{breed}/list")
        return response.json()
