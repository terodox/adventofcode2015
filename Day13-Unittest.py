from Day13 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day13UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayThirteen()

    def test_parse_one_line(self):
        test_cases = [
            'Alice would gain 54 happiness units by sitting next to Bob.',
            'Alice would lose 79 happiness units by sitting next to Carol.'
        ]

        guest_name = 'Alice'
        success_result = {
            'guests': {
                'Bob': 54,
                'Carol': -79
            }
        }

        for one_test in test_cases:
            self._sut.parse_one_line(one_test)

        self.assertTrue(guest_name in self._sut.all_guests.keys())
        self.assertDictEqual(success_result['guests'], self._sut.all_guests[guest_name].guests)

    def test_every_permutation(self):
        starter_data = [
            'Alice would gain 54 happiness units by sitting next to Bob.',
            'Alice would lose 79 happiness units by sitting next to Carol.',
            'Alice would lose 2 happiness units by sitting next to David.',
            'Bob would gain 83 happiness units by sitting next to Alice.',
            'Bob would lose 7 happiness units by sitting next to Carol.',
            'Bob would lose 63 happiness units by sitting next to David.',
            'Carol would lose 62 happiness units by sitting next to Alice.',
            'Carol would gain 60 happiness units by sitting next to Bob.',
            'Carol would gain 55 happiness units by sitting next to David.',
            'David would gain 46 happiness units by sitting next to Alice.',
            'David would lose 7 happiness units by sitting next to Bob.',
            'David would gain 41 happiness units by sitting next to Carol.'
        ]

        for one_item in starter_data:
            self._sut.parse_one_line(one_item)

        for one_guest_name, one_guest_obj in self._sut.all_guests.items():
            self._sut.every_permutation(one_guest_name, [], 0)

        self.assertEqual(330, max(self._sut.all_possibilities.values()))



testSuite = TestSuite()
testSuite.addTest(makeSuite(Day13UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)