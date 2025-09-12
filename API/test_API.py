from Conftests import create_post_endpoint
from Conftests import obj_id
from Conftests import get_request_endpoint
from Conftests import update_post_endpoint
from Conftests import delete_post_endpoint

def test_create_object(create_post_endpoint):
    payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
        }
    }
    create_post_endpoint.create_new_post(payload=payload)
    create_post_endpoint.check_response_name(payload["name"])

def test_read_object(get_request_endpoint, obj_id):
    response_data = get_request_endpoint.get_post(obj_id)
    assert get_request_endpoint.response.status_code == 200
    assert response_data['id'] == obj_id
    assert response_data['name'] == "Apple MacBook Pro 22"
    assert response_data['data']['year'] == 2045
    assert response_data['data']['price'] == 1839.99
    assert response_data['data']['CPU model'] == "Intel Core i14"
    assert response_data['data']['Hard disk size'] == "1 T"

def test_update_object(update_post_endpoint,obj_id):
    payload = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2019,
            "price": 1849.20,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    update_post_endpoint.update_post(obj_id, payload=payload)
    update_post_endpoint.check_response_name('Apple MacBook Pro 17')

def test_remove_object(get_request_endpoint,delete_post_endpoint,obj_id):
    delete_post_endpoint.delete_post(obj_id)
    assert delete_post_endpoint.response.status_code == 200
    get_request_endpoint.get_post(obj_id)
    assert get_request_endpoint.response.status_code == 404
