from Day10 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day10UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTen(10)

    def test_transforms_strings_properly(self):
        input_strings = {
            '11': '21',
            '12': '1112',
            '111222': '3132',
            '6644222': '262432'
        }

        for input_string, output_string in input_strings.items():
            result = AdventDayTen.transform_string(input_string)
            self.assertEqual(output_string, result)

    def test_anser_part1(self):
        input_strings = {
            '11': '111221',
            '12': '132112'
        }

        for input_string, output_string in input_strings.items():
            result = AdventDayTen.run_transforms(input_string, 3)
            self.assertEqual(output_string, result)


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day10UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)