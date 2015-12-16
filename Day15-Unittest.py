from Day15 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day15UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayFifteen()

    def test_parse_one_ingredient(self):
        ingredient = 'Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8'

        self._sut.parse_one_ingredient(ingredient)

        self.assertEqual('Sugar', self._sut.all_ingredients[0].name)
        self.assertEqual(-1, self._sut.all_ingredients[0].capacity)
        self.assertEqual(0, self._sut.all_ingredients[0].durability)
        self.assertEqual(0, self._sut.all_ingredients[0].flavor)
        self.assertEqual(2, self._sut.all_ingredients[0].texture)
        self.assertEqual(8, self._sut.all_ingredients[0].calories)

    def test_parse_calculate_mix_value(self):
        butterscotch = 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8'
        cinnamon = 'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'

        self._sut.parse_one_ingredient(butterscotch)
        self._sut.parse_one_ingredient(cinnamon)

        self.assertEqual(62842880, self._sut.calculate_mix_value([44, 56]))


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day15UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
