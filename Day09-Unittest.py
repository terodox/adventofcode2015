from Day09 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day09UnitTests(TestCase):
    _sut = AdventDayNine(9)
    sample_paths = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]

    def test_Paths_are_parsed_properly(self):
        result = self._sut.parse_one_path(self.sample_paths[0])
        result.city = 'London'
        result.desintations = {'Dublin': 464}


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day09UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)