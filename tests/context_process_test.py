
import datetime
from os import getenv

def test_context_variables_environment(client):

    response = client.get("/")
    env = getenv('FLASK_ENV', None)
    test_string = f"Environment: {env}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_variables_year(client):

    response = client.get("/")
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    year = date.strftime("%Y")
    test_string = f"Copyright: {year}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_currency_format(client):

    response = client.get("/")
    test_string = f"$100"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data