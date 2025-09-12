import requests

class CreatePost:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.response = None
        self.json_data = None

    def create_new_post(self, payload):
        self.response = requests.post(self.base_url, json=payload)
        self.json = self.response.json()
        return self.response

    def check_response_name(self, name):
        assert self.json['name']== 'Apple MacBook Pro 16'

class GetRequest:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.response = None
        self.json_data = None

    def __call__(self, obj_id):
        return self.get_post(obj_id)

    def get_post(self, obj_id):
        url = f"{self.base_url}/{obj_id}"
        self.response = requests.get(url)
        self.json_data = self.response.json()
        return self.json_data

class UpdatePost:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.response = None
        self.json_data = None

    def update_post(self, obj_id, payload):
        url = f"{self.base_url}/{obj_id}"
        self.response = requests.put(url, json=payload)  # PUT для обновления
        self.json_data = self.response.json()
        return self.response

    def check_response_name(self, expected_name):
        assert self.json_data['name'] == expected_name

class DeletePost:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.response = None
        self.json_data = None

    def __call__(self, obj_id):
        return self.delete_post(obj_id)

    def delete_post(self, obj_id):
        url = f"{self.base_url}/{obj_id}"
        self.response = requests.delete(url)
        self.json_data = self.response.json()
        return self.json_data