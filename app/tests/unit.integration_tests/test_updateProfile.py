from asyncio.windows_events import NULL
from pickle import TRUE
from flask import Flask
from app.GUI.updateProfile import UpdateProfileFrame

import requests
import json


def test_UpdateProfileFrame():
   
    app = Flask(__name__)
    client = app.test_client()
    update = client.create.UpdateProfileFrame()

    def test_get_user():
        response = update.get_user('1111')
        assert response.get_data() is not NULL

        response = update.get_user('1001')
        assert response.get_data() is not NULL

        response = update.get_user('1011')
        assert response.get_data() is not NULL

        response = update.get_user('1101')
        assert response.get_data() is  NULL
        

    def test_delete_user():
        response = update.delete_user('1111')
        assert response.delete_data() is not NULL

        response = update.delete_user('1001')
        assert response.delete_data() is not NULL

        response = update.delete_user('1011')
        assert response.delete_data() is not NULL

        response = update.delete_user('1101')
        assert response.delete_data() is  NULL


    def test_getCurrentUser():
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.get('http://127.0.0.1:5000/user_profile/-1', json={}, headers=headers)
        users = response.json()['user_profiles']

        response = update.get_user('1011')
        assert response.delete_data() is not NULL

        response = update.getCurrentUser
        assert response.get_data() in users == TRUE

        response = update.delete_user('1001')
        assert response.delete_data() is not NULL

    
    