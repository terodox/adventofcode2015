from Day17 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day17UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDaySeventeen()

    def test_calculate_answer_for_bits(self):
        test_containers = [20, 15, 10, 5, 5]

        self._sut.containers = test_containers
        self.assertEqual(20, self._sut.calculate_answer_for_bits(1))
        self.assertEqual(15, self._sut.calculate_answer_for_bits(2))
        self.assertEqual(10, self._sut.calculate_answer_for_bits(4))
        self.assertEqual(5, self._sut.calculate_answer_for_bits(8))
        self.assertEqual(5, self._sut.calculate_answer_for_bits(16))
        self.assertEqual(35, self._sut.calculate_answer_for_bits(3))
        self.assertEqual(45, self._sut.calculate_answer_for_bits(7))
        self.assertEqual(50, self._sut.calculate_answer_for_bits(15))
        self.assertEqual(55, self._sut.calculate_answer_for_bits(31))



testSuite = TestSuite()
testSuite.addTest(makeSuite(Day17UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)

