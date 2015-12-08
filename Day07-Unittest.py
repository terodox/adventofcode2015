from Day07 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase
from unittest import mock


class Day07UnitTests(TestCase):
    _sut = AdventDaySeven(7)
    simpler_data_set = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i'
    ]

    def setUp(self):
        self._sut = AdventDaySeven(7)

    def test_Maps_Wire_Properly(self):
        self._sut.read_data = lambda: self.simpler_data_set

        self._sut.parse_input()
        result = self._sut.wiring

        self.assertEqual('x', result['x'].name)
        self.assertEqual(1, len(result['x'].inputs))
        self.assertEqual('123', result['x'].inputs[0])
        self.assertEqual(Operator.Noop, result['y'].operator)
        self.assertEqual('y', result['y'].name)
        self.assertEqual(1, len(result['y'].inputs))
        self.assertEqual('456', result['y'].inputs[0])
        self.assertEqual(Operator.Noop, result['y'].operator)
        self.assertEqual('d', result['d'].name)
        self.assertEqual(2, len(result['d'].inputs))
        self.assertEqual('x', result['d'].inputs[0])
        self.assertEqual('y', result['d'].inputs[1])
        self.assertEqual(Operator.And, result['d'].operator)
        self.assertEqual('e', result['e'].name)
        self.assertEqual(2, len(result['e'].inputs))
        self.assertEqual('x', result['e'].inputs[0])
        self.assertEqual('y', result['e'].inputs[1])
        self.assertEqual(Operator.Or, result['e'].operator)
        self.assertEqual('f', result['f'].name)
        self.assertEqual(2, len(result['f'].inputs))
        self.assertEqual('x', result['f'].inputs[0])
        self.assertEqual('2', result['f'].inputs[1])
        self.assertEqual(Operator.LShift, result['f'].operator)
        self.assertEqual('g', result['g'].name)
        self.assertEqual(2, len(result['g'].inputs))
        self.assertEqual('y', result['g'].inputs[0])
        self.assertEqual('2', result['g'].inputs[1])
        self.assertEqual(Operator.RShift, result['g'].operator)
        self.assertEqual('h', result['h'].name)
        self.assertEqual(1, len(result['h'].inputs))
        self.assertEqual('x', result['h'].inputs[0])
        self.assertEqual(Operator.Not, result['h'].operator)
        self.assertEqual('i', result['i'].name)
        self.assertEqual(1, len(result['i'].inputs))
        self.assertEqual('y', result['i'].inputs[0])
        self.assertEqual(Operator.Not, result['i'].operator)

    def test_Calculates_Wire_values_properly(self):
        truth_values = {
            'x': 123,
            'y': 456,
            'h': 65412,
            'i': 65079,
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114
        }

        self._sut.read_data = lambda: self.simpler_data_set

        self._sut.parse_input()
        for one_key in truth_values:
            result = self._sut.calculate_value(one_key)
            self.assertEqual(truth_values[one_key], result)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day07UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite);