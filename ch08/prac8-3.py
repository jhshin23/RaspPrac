import time
import RPi.GPIO as GPIO
	
try:
	def led_on_off(pin, value):
		GPIO.output(pin, value)
	def measureDistance(trig, echo):
		time.sleep(0.2) # 초음파 센서의 준비 시간을 위해 필연적인 200밀리초 지연
		GPIO.output(trig, 1) # trig 핀에 1(High) 출력
		GPIO.output(trig, 0) # trig 핀 신호 High->Low. 초음사 발사 지시
		
		while(GPIO.input(echo) == 0): # echo 핀 값이 0->1로 바뀔 때까지 루프
			pass
	
		# echo 핀 값이 1이면 초음파가 발사되었음
		pulse_start = time.time() # 초음파 발사 시간 기록
		while(GPIO.input(echo) == 1): # echo 핀 값이 1->0으로 바뀔 때까지 루프
			pass
	
		# echo 핀 값이 0이 되면 초음파 수신하였음
		pulse_end = time.time() # 초음파가 되돌아 온 시간 기록
		pulse_duration = pulse_end - pulse_start # 경과 시간 계산
		return pulse_duration*340*100/2 # 거리 계산하여 리턴(단위 cm)
	def button_pressed(channel):
		global trig
		global echo
		global led_yellow
		distance = measureDistance(trig, echo)
		if distance < 20.0:
			print("%3.2f, 거리가 20cm 이하" % distance)
			led_on_off(led_yellow, 1)
		else:
			print("%3.2f, 거리가 20cm 이상" % distance)
			led_on_off(led_yellow, 0)
		
	led_yellow = 6
	
	trig = 20 # GPIO20 
	echo = 16 # GPIO16
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(trig, GPIO.OUT)
	GPIO.setup(echo, GPIO.IN)
	GPIO.setup(6, GPIO.OUT)
	
	button = 21
	GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
	GPIO.add_event_detect(button, GPIO.RISING, button_pressed, bouncetime=100)
#	i=0
	while True:
		time.sleep(0.1)
#		print(i)
#		i+=1
#		time.sleep(1)
except KeyboardInterrupt:
	print("\n종료")
finally:
	GPIO.cleanup()				
	
