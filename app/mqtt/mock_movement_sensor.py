import time
from paho.mqtt import client as mqtt_client
import mqtt_utilities as mu
import requests as req

def publish(client):
    msg_count = 0
    while True:
        #retrieve active profile (add field)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = req.get(url = 'http://127.0.0.1:5000/user_profile/',
                            headers=headers)
        for profile in response.json()["user_profiles"]:
            print(profile['profile_name'])
        
        #retrieve all room ids of active profile

        #send message with two random (different) room ids


        time.sleep(3)
        msg = f"messages: {msg_count}"
        result = client.publish(mu.TOPIC_MOVEMENT, msg)
        status = result[0]
        if status == 0:
            print(f"Sent `{msg}` to topic `{mu.TOPIC_MOVEMENT}`")
        else:
            print(f"Failed to send message to topic {mu.TOPIC_MOVEMENT}")
        msg_count += 1

def run():
    client = mu.connect_mqtt()[0]
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()