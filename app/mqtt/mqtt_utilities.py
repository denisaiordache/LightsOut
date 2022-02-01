import random
from paho.mqtt import client as mqtt_client

BROKER = 'broker.emqx.io'
PORT = 1883
TOPIC_MOVEMENT = "user/changedRoom"
# generate client ID with pub prefix randomly
def genId():
    return f'python-mqtt-{random.randint(0, 1000)}'
USERNAME = 'LightsOut'
PASSWORD = 'LightsOut'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    CLIENT_ID = genId()
    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client, CLIENT_ID
