from Day11 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day11UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayEleven()

    def test_IsValidFindsValidStringsProperly(self):
        valid_strings = [
            'abcdffaa',
            'ghjaabcc'
        ]

        for one_string in valid_strings:
            self.assertTrue(self._sut.is_valid(one_string))

    def test_IsValidFindsBadStringsProperly(self):
        invalid_strings = [
            'hijklmmn',
            'abbceffg',
            'abbcegjk'
        ]

        for one_string in invalid_strings:
            self.assertFalse(self._sut.is_valid(one_string))

    def test_IncrementWorksProperly(self):
        test_cases = {
            'a': 'b',
            'az': 'ba',
            'azzz': 'baaa',
            'zzzzzzzz': 'aaaaaaaa'
        }

        for one_string, one_result in test_cases.items():
            result = self._sut.increment_string(one_string)
            self.assertEqual(one_result, result)

    def test_get_next_valid_string_works(self):
        test_cases = {
            'abcdefgh': 'abcdffaa',
            # 'ghijklmn': 'ghjaabcc'
        }

        for one_string, one_result in test_cases.items():
            result = self._sut.get_next_valid_string(one_string)
            self.assertEqual(one_result, result)

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day11UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)