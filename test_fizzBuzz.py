import unittest
import fizzBuzz

class TestCase(unittest.TestCase):
	def testYear(self):
		result = fizzBuzz.checkNum(3)
		self.assertEqual(result, "Fizz")

		return
