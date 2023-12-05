file = open('./rsc/input', 'r')
content = file.read()

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getNum(str):
	digits = []
	for i, c in enumerate(str):
		if c.isdigit():
			digits.append(int(c))
		for j, num in enumerate(nums):
			if str[i:].startswith(num):
				digits.append(j)
	return digits[0] * 10 + digits[-1]

def sum(arr):
	acc = 0
	for i in arr:
		acc += getNum(i)
	return acc

print(sum(content.split()))
