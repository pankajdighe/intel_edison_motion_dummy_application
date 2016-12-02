import time
import paho.mqtt.client as mqtt
import random

mqttc=mqtt.Client()
mqttc.connect("iot.eclipse.org",1883,60)
mqttc.loop_start()

#read temperature
def read_motion_data():
    return random.randint(0, 500)

#publish temperature
while 1:
    t=read_motion_data()
    print "Publishing data"
    (result,mid)=mqttc.publish("topic/GeneralizedIoT/motion",t,2)
    time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()