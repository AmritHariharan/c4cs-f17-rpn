#!/usr/bin/env python3

def calculate(string):
	# create a list
	stack = []

	# tokenize input
	for token in string.split():
		if token == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg2 - arg1
			stack.append(result)
		else:
			stack.append(int(token))

	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()