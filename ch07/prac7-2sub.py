import paho.mqtt.client as mqtt

def on_connect(client, userdata, flag, rc, prop=None):
	client.subscribe("sensor")

def on_message(client, userdata, msg):
	m = str(msg.payload.decode("utf-8"))
	tokens = m.split(":")
	room = tokens[0]
	temp = tokens[1]
	humidity = tokens[2]
	print("방:", room, "온도:", temp, "습도:", humidity)

ip = input("브로커의 IP 주소>>")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip, 1883)
client.loop_forever()

