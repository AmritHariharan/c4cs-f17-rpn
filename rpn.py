#!/usr/bin/env python3

import operator
import readline
from termcolor import colored

ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}

cols = {
	'+': 'cyan',
	'-': 'cyan',
	'*': 'cyan',
	'/': 'cyan',
	'neg': 'red',
	'pos': 'green',
}

def validCol(token):
	try:
		val = int(token)
		if val < 0:
			return 'neg'
		else:
			return 'pos'
	except ValueError:
		return token

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
			print(*[colored(i, cols[validCol(i)]) for i in stack])
	return stack.pop()

def main():
	print(colored('RPN CALCULATOR', 'red'))
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()