import pytest
from tests import app
# import requests as client
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_register(app):
    response = app.test_client().post("/register", data={
        "email": "akate@gmail.com",
        "password": "akate",
    })
    assert response.status_code == 200


def test_login(app):
    response = app.test_client().post("/login", data={
        "email": "akate@gmail.com",
        "password": "akate",
    })
    assert response.status_code == 200


def test_logout(app):
    response = app.test_client().post('/logout')
    assert response.status_code == 200