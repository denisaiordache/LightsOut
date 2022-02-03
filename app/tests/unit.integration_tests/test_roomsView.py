from asyncio.windows_events import NULL

from flask import Flask
from app.GUI.roomsView import MyRoomsFrame
from app.GUI.roomsView import RoomFrame
import requests
import json

def test_MyRoomsFrame():
    app = Flask(__name__)
    MyRoomsFrame(app)
    client = app.test_client()
    
    def test_get_user():
        response = client.get_user(1234)
        assert response.get_data() is NULL

        response = client.get_user('4321')
        assert response.get_data() is not NULL

    def test_getCurrentUser():
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.get('http://127.0.0.1:5000/user_profile/-1', json={}, headers=headers)
        users = response.json()['user_profiles']

        response = client.get_user('1234')
        assert response.delete_data() is not NULL

def test_RoomFrame():
    app = Flask(__name__)
    MyRoomsFrame(app)
    client = app.test_client()
    room = client.create.RoomFrame
    
    def test_createLight():
        response = client.createLight()
        assert response.status_code == 201

    def test_updateLight():
        response = client.updateLight()
        assert response.status_code == 200
        
    def test_deleteLight():
        response = client.deleteLight()
        assert response.status_code == 204
    
    def test_deleteRoom():
        response = client.deleteRoom()
        assert response.status_code == 204

    







        

 

