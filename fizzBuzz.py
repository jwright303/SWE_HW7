def checkNum(num):
	if num % 3 == 0:
		if num % 5 == 0:
			return "FizzBuzz"
		else:
			return "Fizz"
	elif num % 5 == 0:
		return "Buzz"
	else:
		return num
	return

def main():
	for i in range(1, 101):
		print(checkNum(i))
		
	return
main()
