names = ["SonHeongmin", "HwangHeechan", "ParkSung", "HongSuhon", "HongMyungbo"]

def find_longest_name():
	long = len(names[0])	
	longest_name = names[0]
	for i in range(1, len(names)):
		if len(names[i]) > long:
			long = len(names[i])	
			longest_name = names[i]	
	return longest_name

print("예제 문자열: ", end = "")
for i in range(len(names)):
	print(names[i], end = "")
	if i < len(names)-1 :
		print(", ", end = "")
print()
print("가장 긴 문자열: "+find_longest_name())
