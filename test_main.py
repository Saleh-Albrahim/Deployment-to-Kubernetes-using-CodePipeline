'''
Tests for jwt flask app.
'''
import os
import json
import pytest


import main


SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTU3ODE5NzUsIm5iZiI6MTU5NDU3MjM3NSwiZW1haWwiOiJzQHMuY29tIn0.-We7-MW2OniK6v-1o7ZNXHdxGWJYSpa-vtlKz_M9YQs'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'


@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'
    assert False


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth',
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
