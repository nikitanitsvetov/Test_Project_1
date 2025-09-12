import pytest
import requests
from API_classes import DeletePost
from API_classes import GetRequest
from API_classes import CreatePost
from API_classes import UpdatePost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()

@pytest.fixture()
def get_request_endpoint():
    return GetRequest()

@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()

@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()

@pytest.fixture()
def obj_id():
    payload = {
        "name": "Apple MacBook Pro 22",
        "data": {
            "year": 2045,
            "price": 1839.99,
            "CPU model": "Intel Core i14",
            "Hard disk size": "1 T"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')



