from Day12 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day12UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTwelve()

    def test_remove_red(self):
        test_cases = {
            '{"c":"red","d":100}': 0,
            '[1,{"c":"red","b":2},3]': 4,
            '[1,{"c":"red","b":{"a":2}},3]': 4
        }

        for one_string, one_result in test_cases.items():
            json_obj = json.loads(one_string)
            result = self._sut.remove_red_data(json_obj)
            value = self._sut.sum_all_numbers(json.dumps(result))
            self.assertEqual(one_result, value)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day12UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)