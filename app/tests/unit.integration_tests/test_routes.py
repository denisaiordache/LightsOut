...
from flask import Flask
from app.application import hello_world_route
from app.application import user_profile_route
from app.application import room_route
from app.application import light_route

import json
#HELLOWORLD
def test_hello_world_route():
    app = Flask(__name__)
    hello_world_route(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200

#USERS
def test_user_profile_route():

    def test_user_profile_POST_route():
        app = Flask(__name__)
        user_profile_route(app)
        client = app.test_client()
        url = '/user_profile/19/POST'
        
        response = client.get(url)
        assert response.get_data() == b'created user_profile with profile_name 19'
        assert response.status_code == 201

    def test_user_profile_PUT_route():
        app = Flask(__name__)
        user_profile_route(app)
        client = app.test_client()
        url = '/user_profile/19/PUT'
        response = client.get(url)
        assert response.get_data() == b'user_profile 19'
        assert response.status_code == 200

    def test_user_profile_GET_route():
        app = Flask(__name__)
        user_profile_route(app)
        client = app.test_client()
        url = '/user_profile/19/GET'
        
        response = client.get(url)
        assert response.get_data() == b'user_profile 19'
        assert response.status_code == 200

    def test_user_profile_DELETE_route():
        app = Flask(__name__)
        user_profile_route(app)
        client = app.test_client()
        url = '/user_profile/19/DELETE'
        
        response = client.get(url)
        assert response.get_data() =={}
        assert response.status_code == 204

#ROOMS
def test_room_route():

    def test_room_POST_route():
        app = Flask(__name__)
        room_route(app)
        client = app.test_client()
        url = '/room/20/POST'
        
        response = client.get(url)
        assert response.get_data() == b"successfully created room"
        assert response.status_code == 201

    def test_room_PUT_route():
        app = Flask(__name__)
        room_route(app)
        client = app.test_client()
        url = '/room/20/PUT'
        response = client.get(url)
        assert response.get_data() == b'room 20'
        assert response.status_code == 200

    def test_room_GET_route():
        app = Flask(__name__)
        room_route(app)
        client = app.test_client()
        url = '/room/20/GET'
        
        response = client.get(url)
        assert response.get_data() == b'room 20'
        assert response.status_code == 200

    def test_room_DELETE_route():
        app = Flask(__name__)
        room_route(app)
        client = app.test_client()
        url = '/room/20/DELETE'
        
        response = client.get(url)
        assert response.get_data() =={}
        assert response.status_code == 204
#LIGHTS
def test_light_route():

    def test_light_POST_route():
        app = Flask(__name__)
        light_route(app)
        client = app.test_client()
        url = '/light/21/POST'
        
        response = client.get(url)
        assert response.get_data() ==b"successfully created light"
        assert response.status_code == 201

    def test_light_PUT_route():
        app = Flask(__name__)
        light_route(app)
        client = app.test_client()
        url = '/light/21/PUT'
        response = client.get(url)
        assert response.get_data() == b'light 21'
        assert response.status_code == 200

    def test_light_GET_route():
        app = Flask(__name__)
        light_route(app)
        client = app.test_client()
        url = '/light/21/GET'
        
        response = client.get(url)
        assert response.get_data() == b'light 21'
        assert response.status_code == 200

    def test_light_DELETE_route():
        app = Flask(__name__)
        light_route(app)
        client = app.test_client()
        url = '/light/21/DELETE'
        
        response = client.get(url)
        assert response.get_data() =={}
        assert response.status_code == 204

#INTEGRATION
def test_light_INTEGRATION_route():
    app = Flask(__name__)
    light_route(app)
    client = app.test_client()
    url = '/light/21/POST'
        
    response = client.get(url)
    assert response.get_data() ==b"successfully created light"
    assert response.status_code == 201

    url = '/light/21/PUT'
    response = client.get(url)
    assert response.get_data() == b'light 21'
    assert response.status_code == 200

    url = '/light/21/GET'
        
    response = client.get(url)
    assert response.get_data() == b'light 21'
    assert response.status_code == 200

    url = '/light/21/DELETE'
        
    response = client.get(url)
    assert response.get_data() =={}
    assert response.status_code == 204
        
def test_user_profile_INTEGRATION_route():
    app = Flask(__name__)
    user_profile_route(app)
    client = app.test_client()
    url = '/user_profile/21/POST'
        
    response = client.get(url)
    assert response.get_data() ==b"created user_profile with profile_name 19"
    assert response.status_code == 201

    url = '/user_profile/21/PUT'
    response = client.get(url)
    assert response.get_data() == b'user_profile 21'
    assert response.status_code == 200

    url = '/user_profile/21/GET'
        
    response = client.get(url)
    assert response.get_data() == b'user_profile 21'
    assert response.status_code == 200

    url = '/user_profile/21/DELETE'
        
    response = client.get(url)
    assert response.get_data() =={}
    assert response.status_code == 204

def test_room_INTEGRATION_route():
    app = Flask(__name__)
    room_route(app)
    client = app.test_client()
    url = '/room/21/POST'
        
    response = client.get(url)
    assert response.get_data() ==b"successfully created room"
    assert response.status_code == 201

    url = '/room/21/PUT'
    response = client.get(url)
    assert response.get_data() == b'room 21'
    assert response.status_code == 200

    url = '/room/21/GET'
        
    response = client.get(url)
    assert response.get_data() == b'room 21'
    assert response.status_code == 200

    url = '/room/21/DELETE'
        
    response = client.get(url)
    assert response.get_data() =={}
    assert response.status_code == 204

    


