# terrible conversion because no switch
def convertSpelledNum(line) -> str:
	if "one" in line:
		line = line.replace("one", "1")
	if "two" in line:
		line = line.replace("two", "2")
	if "three" in line:
		line = line.replace("three", "3")
	if "four" in line:
		line = line.replace("four", "4")
	if "five" in line:
		line = line.replace("five", "5")
	if "six" in line:
		line = line.replace("six", "6")
	if "seven" in line:
		line = line.replace("seven", "7")
	if "eight" in line:
		line = line.replace("eight", "8")
	if "nine" in line:
		line = line.replace("nine", "9")

	return line

#out = open("./rsc/output", "w")
with open('./rsc/input') as f:
	inputLines = f.read().splitlines()

	digitList = []
	for line in inputLines:
		line = convertSpelledNum(line)
		#out.write(line + "\n")
		digit = ''.join(filter(str.isdigit, line))
		if len(digit) == 1:
			digit = digit + digit
		elif len(digit) > 1:
			digit = digit[0] + digit[len(digit)-1]

		#out.write(digit + "\n")
		digitList.append(int(digit))

	print(sum(digitList))
out.close()
