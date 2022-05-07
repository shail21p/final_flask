"""This test the homepage"""

def test_request_about(client):
    """This ensures that the Index page gets the correct HTML response of status code 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_welcome(client):
    """This ensures that the Index page gets the correct HTML response of status code 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_request_index(client):
    """This ensures that the Index page gets the correct HTML response of status code 200"""
    response = client.get("/")
    assert response.status_code == 200



def test_request_page_not_found(client):
    """This ensures that a page that doesn't exist gets
    the correct HTML response of status code 404"""
    response = client.get("/page55")
    assert response.status_code == 404