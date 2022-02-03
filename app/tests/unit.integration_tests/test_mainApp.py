...
from flask import Flask
from sqlalchemy import null

from app.GUI.mainApp import App
import requests
import json

def test_getCurrentUser():
    app = Flask(__name__)
    App(app)
    client = app.test_client()
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.get('http://127.0.0.1:5000/user_profile/-1', json={}, headers=headers)
    users = response.json()['user_profiles']

    response = client.getCurrentUser()
    assert response.get_data() in users == True
 

def test_hidePages():
    app = Flask(__name__)
    App(app)
    client = app.test_client()
    ok =client.getCurrentUser()

    if ok is None:
        assert client.app.userIsLogged == False
        assert client.app.profileButton['state'] == 'disabled'
        assert client.app.roomsButton['state'] == 'disabled'
        assert client.app.createButton['state'] == 'normal'
    else:
       assert client.app.userIsLogged == True
       assert client.app.createButton['state'] == 'disabled'
       assert client.app.profileButton['state'] == 'normal'
       assert client.app.roomsButton['state'] == 'normal'

