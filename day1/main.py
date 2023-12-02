
with open('./rsc/input') as f:
	inputLines = f.read().splitlines()

	digitList = []
	for line in inputLines:
		digit = ''.join(filter(str.isdigit, line))
		if len(digit) == 1:
			digit = digit + digit
		if len(digit) > 1:
			digit = digit[0] + digit[len(digit)-1]

		digitList.append(int(digit))

	print(sum(digitList))
