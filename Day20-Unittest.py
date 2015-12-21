from Day20 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day20UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTwenty()

    def test_calculate_count(self):
        test_cases = {
            1: 10,
            2: 30,
            3: 40,
            4: 70,
            5: 60,
            6: 120,
            7: 80,
            8: 150,
            9: 130
        }

        for house, present_count in test_cases.items():
            self.assertEqual(present_count, self._sut.calculate_count(house))

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day20UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
