import time
import random
from paho.mqtt import client as mqtt_client
import mqtt_utilities as mu
import requests as req

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:5000/user_profile/'

def publish(client):
    msg_count = 0
    while True:
        room_ids = []

        #retrieve active profile
        response = req.get(url=url, headers=headers)
        for profile in response.json()["user_profiles"]:
            if profile["is_active"]:
                #retrieve all room ids of active profile
                for room in profile["rooms"]:
                    room_ids.append(room["id"])

        #send message with two random (different) room ids
        time.sleep(3)
        index1, index2 = random.sample(range(0, len(room_ids)), 2)
        previousRoomId = room_ids[index1]
        nextRoomId = room_ids[index2]
        msg = {"previousRoomId": previousRoomId, "nextRoomId": nextRoomId}
        print(msg)
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