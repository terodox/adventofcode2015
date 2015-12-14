from Day14 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day14UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayFourteen()

    def test_parse_one_reindeer(self):
        self._sut.parse_one_reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
        self.assertEqual(14, self._sut.all_reindeer[0].speed)
        self.assertEqual(10, self._sut.all_reindeer[0].run_time)
        self.assertEqual(127, self._sut.all_reindeer[0].rest_time)

    def test_calculate_one_reindeer(self):
        self._sut.parse_one_reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.')
        self._sut.calculate_all_reindeer(1000)
        self.assertEqual(1120, self._sut.all_results[0])



testSuite = TestSuite()
testSuite.addTest(makeSuite(Day14UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)