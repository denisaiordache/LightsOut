import time
import datetime as dt
import mqtt_utilities as mu
import requests as req
import json

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:5000/user_profile/'
SLEEP_HOUR = ''
WAKEUP_HOUR = ''

def updateHours(msg):
    actual_msg = json.loads(msg)
    SLEEP_HOUR = actual_msg['newSleepHour']
    WAKEUP_HOUR = actual_msg['newWakeUpHour']

def publish_and_subscribe(client):

    #listens for a change in the SLEEP-HOUR and WAKEUP-HOUR and updates them
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        updateHours(msg.payload.decode())

    client.subscribe(mu.TOPIC_HOURCHANGE)
    client.on_message = on_message

    #check if current time is equal to recorded values and inform correspondingly
    while True:
        current_time = dt.datetime.now().strftime("%H:%M")
        if current_time in (SLEEP_HOUR, WAKEUP_HOUR):
            msg = json.dumps({"isSleepEvent": current_time==SLEEP_HOUR})
            result = client.publish(mu.TOPIC_LIGHTSHIFT, msg)
            status = result[0]
            if status == 0:
                print(f"Sent `{msg}` to topic `{mu.TOPIC_LIGHTSHIFT}`")
            else:
                print(f"Failed to send message to topic {mu.TOPIC_LIGHTSHIFT}")
        time.sleep(5)

def run():
    client = mu.connect_mqtt()[0]
    client.loop_start()
    publish_and_subscribe(client)

if __name__ == '__main__':
    run()