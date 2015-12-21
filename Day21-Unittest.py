from Day21 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day21UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTwentyOne()

    def test_do_i_win(self):
        self._sut.boss = Character(12, 2, 7)

        self.assertTrue(self._sut.do_i_win(Character(8, 5, 5)))

    def test_build_all_combinations(self):
        result = self._sut.build_all_combinations()

    def test_apply_item_set(self):
        test_item_set = [
            Item(10, 12, 0),
            Item(10, 0, 10),
            Item(5, 8, 0),
            Item(5, 0, 5),
        ]

        result = self._sut.apply_item_set(test_item_set)

        self.assertEqual(result[1], 30)
        self.assertEqual(result[0].armor, 15)
        self.assertEqual(result[0].attack, 20)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day21UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
