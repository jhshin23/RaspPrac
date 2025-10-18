import paho.mqtt.client as mqtt
import random
import time

ip = input("브로커의 IP 주소")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(ip, 1883)
client.loop_start()

while True:
	room = str(random.randint(0, 3))
	temp = str(random.randint(0, 100))
	humidity = str(random.randint(0, 100))
	client.publish("sensor",room+":"+temp+":"+humidity)
	time.sleep(1)
client.loop_stop()
client.disconnect()
