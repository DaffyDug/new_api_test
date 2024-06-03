import pytest
from test_api import *

def test_get_users():
    response = get_request()
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_users_id():
    response = get_user_id(2)
    assert response.status_code == 200
    assert response.json()['userId'] == 2
def test_get_id():
    response = get_id(3)
    assert response.status_code == 200
    assert response.json()['id'] == 3

def test_get_title():
    id = 3
    response = get_title(id)
    assert response.status_code == 200
    assert response.json()['title'] == "omnis laborum odio"

def test_negative():
    response = get_user_id(345)
    assert response.status_code == 404

def test_post_users():
    response = post_user(3, "omnis laborum odio")
    assert response.status_code_code == 201
    assert response.json()['userId'] == 3
    assert response.json()['title'] == "omnis laborum odio"

def test_put_user():
    response = put_user(4, "non esse culpa molestiae omnis sed optio")
    assert response.status_code == 200
    assert response.json()['userId'] == 4
    assert response.json()['title'] == "non esse culpa molestiae omnis sed optio"

def test_delete_user():
    response = delete_user(3)
    assert response.status_code == 204