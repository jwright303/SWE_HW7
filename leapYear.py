def testYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return "Year is a leap year"
			else:
				return "Year is not a leap year"
		else:
			return "Year is a leap year"
	else:
		return "Year is not a leap year"

def main():
	return

main()
