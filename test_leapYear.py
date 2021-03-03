import unittest
import leapYear

class TestCase(unittest.TestCase):
	def testYear(self):
		result = leapYear.testYear(2000)
		self.assertEqual(result, "Year is a leap year")

		return
