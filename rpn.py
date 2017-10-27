#!/usr/bin/env python3

import operator

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
}

def calculate(string):
	# create a list
	stack = []

	# tokenize input
	for token in string.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			stack.append(function(arg1, arg2))
			
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()