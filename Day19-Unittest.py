from Day19 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day19UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayNineteen()

    def test_answer_part1(self):
        combo = [
            'H => HO',
            'H => OH',
            'O => HH',
        ]
        self._sut.read_data = lambda: combo
        self._sut.input_value = 'HOH'
        result = self._sut.answer_part1()

        self.assertEqual(4, result)

    def test_parse_replacements(self):
        test_inputs = {
            'Ti => TiTi': [('Ti', 'TiTi')],
            'e => HF': [('e', 'HF')],
            'e => NAl': [('e', 'NAl')],
            'e => OMg': [('e', 'OMg')]
        }

        for one_test, one_result in test_inputs.items():
            self._sut.read_data = lambda: [one_test]
            result = self._sut.parse_replacements()
            self.assertEqual(one_result, result)

    def test_parse_replacements_part2(self):
        test_inputs = [
            'Ti => TiTi',
            'e => HF',
            'e => NAl',
            'e => OMg'
        ]

        self._sut.read_data = lambda: test_inputs
        result = self._sut.parse_replacements_part2()

        self.assertEqual(['TiTi'], result['Ti'])
        self.assertEqual(['NAl', 'OMg', 'HF'], result['e'])


    def test_replace_one_instance(self):
        self.assertEqual([0, 'HOOH'], self._sut.replace_one_instance('HOH', 'H', 'HO', 0))
        self.assertEqual([2, 'HOHO'], self._sut.replace_one_instance('HOH', 'H', 'HO', 1))
        self.assertEqual([0, 'OHOH'], self._sut.replace_one_instance('HOH', 'H', 'OH', 0))
        self.assertEqual([2, 'HOOH'], self._sut.replace_one_instance('HOH', 'H', 'OH', 2))

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day19UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
