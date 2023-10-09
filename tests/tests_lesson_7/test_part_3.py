import pytest

from lesson_7.placeholder_api import JsonPlaceholderClient
from lesson_7.json_placeholder_static import RESPONSE_ALL_POSTS_FIELDS_LIST


class TestJsonApi:

    def test_get_list_all_posts(self, json_placeholder_endpoint):
        json_api = JsonPlaceholderClient(json_placeholder_endpoint)
        response = json_api.get_list_all_posts()
        assert RESPONSE_ALL_POSTS_FIELDS_LIST == list(response[0].keys())

    def test_get_post_by_id(self, json_placeholder_endpoint):
        json_api = JsonPlaceholderClient(json_placeholder_endpoint)
        response = json_api.get_post_by_id(1)
        assert RESPONSE_ALL_POSTS_FIELDS_LIST == list(response.keys())

    @pytest.mark.parametrize('title, body, user_id', [("test_title1", "test_body1", 1),
                                                      ("test_title2", "test_body2", 5),
                                                      ("test_title3", "test_body3", 10)])
    def test_create_post_for_user(self, json_placeholder_endpoint, title, body, user_id):
        json_api = JsonPlaceholderClient(json_placeholder_endpoint)
        response = json_api.create_post_for_user(title, body, user_id)
        assert response['title'] == title
        assert response['body'] == body
        assert response['userId'] == user_id

    @pytest.mark.parametrize('post_id, title, body, user_id', [(1, "test_title1", "test_body1", 1),
                                                               (2, "test_title2", "test_body2", 5),
                                                               (3, "test_title3", "test_body3", 10)])
    def test_update_post_for_user(self, json_placeholder_endpoint, post_id, title, body, user_id):
        json_api = JsonPlaceholderClient(json_placeholder_endpoint)
        response = json_api.update_post_for_user(post_id, title, body, user_id)
        assert response['title'] == title
        assert response['body'] == body
        assert response['userId'] == user_id

    @pytest.mark.parametrize('post_id, title', [(1, "test_title1"),
                                                (2, "test_title2"),
                                                (3, "test_title3")])
    def test_patch_post_for_user(self, json_placeholder_endpoint, post_id, title):
        json_api = JsonPlaceholderClient(json_placeholder_endpoint)
        old_post = json_api.get_post_by_id(post_id)
        response = json_api.patch_post_for_user(post_id, title)

        assert response['title'] == title
        assert response['body'] == old_post['body']
        assert response['userId'] == old_post['userId']
