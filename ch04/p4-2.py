list = [18, 19, 5, 18, 18, 13, 15, 2, 11, 19]

def count_num_in_list():
	number_count_dict = {}
	number_count_dict[list[0]] = 1

	for i in range(1, len(list)):
		if number_count_dict.get(list[i]) != None:
			number_count_dict[list[i]] += 1
		else:
			number_count_dict[list[i]] = 1
			

	return number_count_dict.items()

def print_result(dict_items):
	for i in dict_items:
		print("<%d: %d개>"%(i[0], i[1]),end = " ")
	print()

print_result(count_num_in_list())
