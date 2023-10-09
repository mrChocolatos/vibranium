import requests


class JsonPlaceholderClient:
    def __init__(self, json_placeholder_api):
        self.json_placeholder_api = json_placeholder_api

    def create_post_for_user(self, title: str, body: str, user_id: int):
        return requests.post(self.json_placeholder_api + "/posts",
                             json={
                                 "title": title,
                                 "body": body,
                                 "userId": user_id,
                             },
                             headers={
                                 "Content-type": "application/json",
                                 "charset": "UTF-8"
                             }).json()

    def update_post_for_user(self, post_id: int, title: str, body: str, user_id: int):
        return requests.put(self.json_placeholder_api + f"/posts/{post_id}",
                            json={
                                "id": post_id,
                                "title": title,
                                "body": body,
                                "userId": user_id,
                            },
                            headers={
                                "Content-type": "application/json",
                                "charset": "UTF-8"
                            }).json()

    def get_post_by_id(self, post_id):
        return requests.get(self.json_placeholder_api + f"/posts/{post_id}").json()

    def get_list_all_posts(self):
        return requests.get(self.json_placeholder_api + "/posts").json()

    def patch_post_for_user(self, post_id: int, title: str):
        return requests.patch(self.json_placeholder_api + f"/posts/{post_id}",
                              json={
                                  "title": title
                              },
                              headers={
                                  "Content-type": "application/json",
                                  "charset": "UTF-8"
                              }).json()

    def check_contains_fields_in_response(self, target_fileds, response):
        return True if target_fileds == response[0].keys() else False
