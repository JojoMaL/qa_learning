
import requests
import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_get_user():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = r.json()

    assert r.status_code == 200
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] == "Sincere@april.biz"
    assert r.headers["Content-Type"].startswith("application/json")

@pytest.mark.api
def test_get_user_not_found():
    r = requests.get("https://jsonplaceholder.typicode.com/users/9999")

    assert r.status_code == 404
    assert r.headers["Content-Type"].startswith("application/json")

@pytest.mark.api
def test_create_user():
    r = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json={"name": "Jose", "email": "jose@example.com"}
    )
    data = r.json()

    assert r.status_code == 201
    assert data["name"] == "Jose"
    assert data["email"] == "jose@example.com"
    assert "id" in data
    assert r.headers["Content-Type"].startswith("application/json")

@pytest.mark.api
def test_create_user_without_email():
    r = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json={"name": "Jose"}
    )

    print(r.status_code)
    print(r.json())

@pytest.mark.api
def test_update_user_email():
    r = requests.get("https://jsonplaceholder.typicode.com/users/1")
    original = r.json()

    r = requests.patch(
        "https://jsonplaceholder.typicode.com/users/1",
        json={"email": "nuevo@example.com"}
    )
    data = r.json()

    assert r.status_code == 200
    assert data["email"] == "nuevo@example.com"
    assert data["name"] == original["name"]
    assert data["username"] == original["username"]

    print(r.status_code)
    print(r.json())


@pytest.fixture
def user_payload():
    return {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "jose@example.com",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    }


@pytest.mark.api
def test_update_user_put(user_payload):
    r = requests.put("https://jsonplaceholder.typicode.com/users/1",
        json = user_payload)

    data = r.json()
    assert r.status_code == 200
    assert data["email"] == "jose@example.com"
    assert data["name"] == "Leanne Graham"
    assert data["username"] == "Bret"
    assert data["address"]["city"] == "Gwenborough"
    assert data["address"]["geo"]["lat"] == "-37.3159" 
    assert data["company"]["name"] == "Romaguera-Crona" 
    print(r.status_code)
    print(r.json())

@pytest.mark.api
def test_update_user_put_complete(user_payload):
    payload = user_payload

    r = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=payload
    )

    data = r.json()

    assert r.status_code == 200
    assert data == payload

@pytest.mark.api
def test_delete_user():
    r = requests.delete(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert r.status_code == 200
    assert r.json() == {}

@pytest.mark.api
def test_auth_without_token():
    r = requests.get("https://dummyjson.com/auth/me")

    assert r.status_code == 401

@pytest.mark.api
def test_auth_with_token():
    r = requests.post(
        "https://dummyjson.com/auth/login",
        json={
            "username": "emilys",
            "password": "emilyspass"
        }
    )

    assert r.status_code == 200
    data = r.json()
    token = data["accessToken"]
   
    r = requests.get(
        "https://dummyjson.com/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert r.status_code == 200