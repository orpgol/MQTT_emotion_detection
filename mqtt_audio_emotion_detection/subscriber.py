import paho.mqtt.client as mqtt
from contextlib import closing

def on_message(client, obj, msg):
    print("Writing audio")
    with closing(open("./audio_data/out_orpaz.m4a", "wb")) as f:
        f.write(msg.payload)

if __name__=='__main__':
    topic = "/voice/"
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.connect('10.81.74.41', 1883)

    mqttc.subscribe(topic, 0)

    rc = 0

    while rc == 0:
        rc = mqttc.loop()
    print("rc: " + str(rc))
