import time
import random
import mqtt_utilities as mu
import requests as req
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:5000/light/'

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        changeLights(msg.payload.decode())

    client.subscribe(mu.TOPIC_MOVEMENT)
    client.on_message = on_message

def changeLights(msg):
    """Turns off/on the lights in the room with id equal to previousRoomId/nextRoomId"""

    previousRoomId, nextRoomId = json.loads(msg)["previousRoomId"], json.loads(msg)["nextRoomId"]

    #retrieve all lights
    response = req.get(url=url, headers=headers)
    lights = response.json()["lights"]

    #turn off the lights of the previous room
    for light in lights:
        if light["room_id"] == previousRoomId:
            light_id = light["id"]
            req.put(url=url+f"{light_id}", headers=headers, json={"on": False})

    #turn on the lights of the next room
    for light in lights:
        if light["room_id"] == nextRoomId:
            light_id = light["id"]
            req.put(url=url+f"{light_id}", headers=headers, json={"on": True})

    # prints to see that lights actually get updated:
    # response = req.get(url=url, headers=headers)
    # lights = response.json()["lights"]
    # for light in lights:
    #     print(light)
    #     print()

def run():
    client = mu.connect_mqtt()[0]
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()