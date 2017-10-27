import unittest
import rpn

class TestBasics(unittest.TestCase):
	
	def test_add(self): # self is always the first argument
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)

	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)