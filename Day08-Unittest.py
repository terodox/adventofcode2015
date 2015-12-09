from Day08 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day08UnitTests(TestCase):
    _sut = AdventDayEight(8)
    str_truths =     [0, 3, 7,  1, 1, 4,  27, 32, 3,  25, 27, 6,  27]
    literal_truths = [2, 5, 10, 6, 4, 11, 48, 41, 10, 32, 33, 12, 33]

    def test_Calculate_string_length_properly(self):
        all_data = []
        with open("Day08-UnittestData.txt") as data:
            all_data = data.readlines()

        count = 0
        for one_string in all_data:
            self.assertEqual(self.str_truths[count], self._sut.calculate_string_length(one_string))
            count += 1

    def test_Calculate_literal_length_properly(self):
        all_data = []
        with open("Day08-UnittestData.txt") as data:
            all_data = data.readlines()

        count = 0
        for one_string in all_data:
            self.assertEqual(self.literal_truths[count], self._sut.calculate_literal_length(one_string))
            count += 1

    def test_Answer_calculated_correctly(self):
        all_data = []
        with open("Day08-UnittestData.txt") as data:
            all_data = data.readlines()

        self._sut.read_data = lambda: all_data
        result = self._sut.answer_part1()

        should_be = sum(self.literal_truths) - sum(self.str_truths)

        self.assertEqual(should_be, result)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day08UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)