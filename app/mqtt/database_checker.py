import time
import random
import mqtt_utilities as mu
import requests as req
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:5000/user_profile/'

def publish(client):
    previousSleepHour = ""
    previousWakeUpHour = ""
    while True:

        #retrieve active profile
        response = req.get(url=url, headers=headers)
        for profile in response.json()["user_profiles"]:
            if profile["is_active"]:
                activeProfile = profile
                break
        
        #check if sleep / wake-up hour have changed
        send_message_flag = False
        if activeProfile["wake_up_hour"] != previousWakeUpHour:
            previousWakeUpHour = activeProfile["wake_up_hour"]
            send_message_flag = True
        if activeProfile["sleep_hour"] != previousSleepHour:
            previousSleepHour = activeProfile["sleep_hour"]
            send_message_flag = True
        
        #send the message if there is an update to inform about
        if send_message_flag:
            msg = json.dumps({"newSleepHour": previousSleepHour, 
                                "newWakeUpHour": previousWakeUpHour,
                                "profile_name": activeProfile["profile_name"]})
            result = client.publish(mu.TOPIC_HOURCHANGE, msg)
            status = result[0]
            if status == 0:
                print(f"Sent `{msg}` to topic `{mu.TOPIC_HOURCHANGE}`")
            else:
                print(f"Failed to send message to topic {mu.TOPIC_HOURCHANGE}")

        time.sleep(2)#time.sleep(60)

def run():
    client = mu.connect_mqtt()[0]
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()