import requests
BASE_URL = 'https://jsonplaceholder.typicode.com'
def get_request():
    response = requests.get(f'{BASE_URL}/albums')
    return response
def get_user_id(userId):
    response = requests.get(f'{BASE_URL}/albums/{userId}')
    return response
def get_id(Id):
    response = requests.get(f"{BASE_URL}/albums/{Id}")
    return response
def get_title(id):
    response = requests.get(f"{BASE_URL}/albums/{id}")
    return response

def post_user(userId, title):
    json_data = {"userId": userId, "title": title}
    response = requests.get(f'{BASE_URL}/albums', json = json_data)
    return response
def put_user(userId, title):
    json_data = {"userId": userId, "title": title}
    response = requests.put(f'{BASE_URL}/albums/{userId}', json = json_data)
    return response
def delete_user(userId):
    response = requests.delete(f'{BASE_URL}/albums/{userId}')
    return response