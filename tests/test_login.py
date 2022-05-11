import pytest
import requests as client
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

# @pytest.fixture
def test_register():
    response = client.post("http://localhost:5000/register", data={
        "email": "shailpatel21@yahoo.com",
        "password": "Nightstalker@23",
    })
    assert response.status_code == 200


# @pytest.fixture
def test_login():
    response = client.post("http://localhost:5000/login", data={
        "email": "shailpatel21@yahoo.com",
        "password": "Nightstalker@23",
    })
    assert response.status_code == 200


# @pytest.fixture
def test_logout():
    response = client.post('http://localhost:5000/logout')
    assert response.status_code == 200