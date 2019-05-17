import paho.mqtt.client as mqtt
from contextlib import closing
import time

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

if __name__=='__main__':
    topic = "/voice/"
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.connect('10.81.74.41', 1883)

    with closing(open("./audio_data/orpaz_5.m4a", "rb")) as f:
        bytesval = bytearray(f.read())
        mqttc.publish(topic, bytesval)

    rc = 0

    while rc == 0:
        print(rc)
        time.sleep(10)        
        rc = mqttc.loop()
