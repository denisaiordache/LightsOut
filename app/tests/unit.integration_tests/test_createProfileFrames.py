
from flask import Flask
from app.GUI.createProfileFrame import CreateProfileFrame
from app.GUI.createProfileFrame import getCheckboxValue
from app.GUI.createProfileFrame import handleSubmit
from app.dateloc import *

import requests
import json


def test_createProfileFrames():
    app = Flask(__name__)
    CreateProfileFrame(app)
    client = app.test_client()

    profile_frame = client.CreateProfileFrame()

    #HandleSubmit
    data_set = {"profile_name": profile_frame.profile_name_box.get(),
                    "wake_up_hour": profile_frame.wake_up_hour_box.get(),
                    "sleep_hour" : profile_frame.sleep_hour_box.get(),
                    "timer": profile_frame.timer_box.get(),
                    "same_as_outside_lights":profile_frame.same_as_outside_lights_value.get(),
                    "is_active": True
                    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    json_data = json.dumps(data_set)
    response = requests.post(url = 'http://127.0.0.1:5000/user_profile/' + str(profile_frame.profile_name_box.get()),
                                json = data_set,
                                headers=headers
                                )
    assert response.status_code == 201



