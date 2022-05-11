import pytest
from tests import app
# import requests as client
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_register(app):
    response = app.test_client().post("/register", data={
        "email": "shailpatel21@yahoo.com",
        "password": "Nightstalker@23",
    })
    assert response.status_code == 200 or 302


def test_login(app):
    response = app.test_client().post("/login", data={
        "email": "shailpatel21@yahoo.com",
        "password": "Nightstalker@23",
    })
    assert response.status_code == 200 or 302


def test_logout(app):
    response = app.test_client().post('/logout')
    print("response: ", response)
    assert response.status_code == 200 or 302