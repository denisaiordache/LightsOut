import time
import mqtt_utilities as mu
import requests as req
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url_user = 'http://127.0.0.1:5000/user_profile/'
url_light = 'http://127.0.0.1:5000/light/'

def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        changeLightsIntensity(msg.payload.decode())

    client.subscribe(mu.TOPIC_LIGHTSHIFT)
    client.on_message = on_message

def changeLightsIntensity(msg):
    """Gradually shift intensity up or down"""

    actual_msg = json.loads(msg)
    isSleepEvent = actual_msg["isSleepEvent"]

    #retrieve active profile
    response = req.get(url=url_user, headers=headers)
    for profile in response.json()["user_profiles"]:
        if profile["is_active"]:
            activeProfile = profile
            break

    #retrieve active user profile's light's ids
    light_ids = []
    for room in activeProfile["rooms"]:
        for light in room["lights"]:
            light_ids.append(light["id"])

    #make sure lights are at their default values for this event (100 for sleep, 0 for wake up)
    if isSleepEvent:
        for light_id in light_ids:
            response = req.put(url=url_light+f"{light_id}", headers=headers, json={"intensity": 100})
    else:
        for light_id in light_ids:
            response = req.put(url=url_light+f"{light_id}", headers=headers, json={"intensity": 0})

    #separate each change into 10 increments
    for increment in range(1, 11):
        time.sleep(60)
        for light_id in light_ids:
            if isSleepEvent:
                req.put(url=url_light+f"{light_id}", headers=headers, json={"intensity": 100-increment*10})
            else:
                req.put(url=url_light+f"{light_id}", headers=headers, json={"intensity": increment*10})

    # prints to see that lights actually get updated:
    # response = req.get(url=url_light, headers=headers)
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