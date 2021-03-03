import unittest
import fizzBuzz

class TestCase(unittest.TestCase):
	def testYear(self):
		result = fizzBuzz.checkNum(3)
		self.assertEqual(result, "Fizz")

		result = fizzBuzz.checkNum(15)
		self.assertEqual(result, "FizzBuzz")

		result = fizzBuzz.checkNum(4)
		self.assertEqual(result, 4)

		result = fizzBuzz.checkNum(5)
		self.assertEqual(result, "Buzz")
		return
