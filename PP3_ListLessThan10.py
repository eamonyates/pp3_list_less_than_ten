a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []


def less_than_five(list):
	while True:
		try:
			user_num = int(input("Please provide a number between 0 and 100: "))
			if user_num > 100:
				print ("You must choose a number smaller than 100")
				continue
			elif user_num < 0:
				print ("You must choose a number greater than 0")
				continue
		except ValueError:
			print ("You must enter a number")
		else:
			break

	for number in list:
		if number < user_num:
			b.append(number)
	print (b)


if __name__ == "__main__":
	less_than_five(a)
