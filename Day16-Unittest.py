from Day16 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day16UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDaySixteen()

    def test_parse_one_aunt(self):
        test = 'Sue 28: goldfish: 8, trees: 7, akitas: 10'

        self._sut.parse_one_aunt(test)

        self.assertTrue(28 in self._sut.aunts.keys())
        self.assertDictEqual({
            'goldfish': '8',
            'trees': '7',
            'akitas': '10'
        }, self._sut.aunts[28])

    def test_is_match_true(self):
        test = 'Sue 33: trees: 3, cars: 2, perfumes: 1'
        self._sut.parse_one_aunt(test)

        result = self._sut.is_match(self._sut.aunts[33])

        self.assertTrue(result)

    def test_is_match_false(self):
        test = 'Sue 33: trees: 33, cars: 2, perfumes: 1'
        self._sut.parse_one_aunt(test)

        result = self._sut.is_match(self._sut.aunts[33])

        self.assertFalse(result)

    def test_is_match_part2_true(self):
        test = 'Sue 33: trees: 9, cars: 2, goldfish: 1'
        self._sut.parse_one_aunt(test)

        result = self._sut.is_match_part2(self._sut.aunts[33])

        self.assertTrue(result)

    def test_is_match_part2_false_trees(self):
        test = 'Sue 33: trees: 3, cars: 2, goldfish: 9'
        self._sut.parse_one_aunt(test)

        result = self._sut.is_match_part2(self._sut.aunts[33])

        self.assertFalse(result)

    def test_is_match_part2_false_goldfish(self):
        test = 'Sue 33: trees: 2, cars: 2, goldfish: 1'
        self._sut.parse_one_aunt(test)

        result = self._sut.is_match_part2(self._sut.aunts[33])

        self.assertFalse(result)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day16UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
