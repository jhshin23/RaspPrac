import paho.mqtt.client as mqtt

def on_connect(client, userdata, flag, rc, prop=None):
	client.subscribe("chat")
	print("입력하면 바로 전송합니다")

def on_message(client, userdata, msg):
	message_str = msg.payload.decode("utf-8")
	if (message_str.find("("+username+")") == 0):
		return
	print(message_str)

ip = input("브로커의 IP 주소>>")
username = input("사용자이름>>")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip, 1883)
client.loop_start()

while True:
	text = input()
	if (text == "exit"): 
		break
	client.publish("chat", "("+username+")"+text)
	
client.loop_stop()
client.disconnect()
