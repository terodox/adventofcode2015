from unittest import TestSuite, makeSuite, TextTestRunner, TestCase
from unittest import mock
from Day05 import AdventDayFive


class Day05UnitTests(TestCase):
    def test_FindsAtBeginning(self):
        adventDay5 = AdventDayFive(5)
        test_string = 'ajabbbb'
        adventDay5.read_data = lambda: [test_string]
        result = adventDay5.answer_part2()
        self.assertEqual(1, result)

    def test_FindsAtEnd(self):
        adventDay5 = AdventDayFive(5)
        test_string = 'bbbbaja'
        adventDay5.read_data = lambda: [test_string]
        result = adventDay5.answer_part2()
        self.assertEqual(1, result)

    def test_FindsInMiddle(self):
        adventDay5 = AdventDayFive(5)
        test_string = 'bbajabb'
        adventDay5.read_data = lambda: [test_string]
        result = adventDay5.answer_part2()
        self.assertEqual(1, result)

    def test_DoesNotMatchThreConsecutiveLetters(self):
        adventDay5 = AdventDayFive(5)
        test_string = 'bbbaja'
        adventDay5.read_data = lambda: [test_string]
        result = adventDay5.answer_part2()
        self.assertEqual(0, result)

    def test_IsNiceExamples(self):
        adventDay5 = AdventDayFive(5)
        adventDay5.read_data = lambda: ['qjhvhtzxzqqjkmpb','xxyxx']
        result = adventDay5.answer_part2()
        self.assertEqual(2, result)

    def test_IsNaughtyExamples(self):
        adventDay5 = AdventDayFive(5)
        adventDay5.read_data = lambda: ['uurcxstgmygtbstg','ieodomkazucvgmuy','aaaa']
        result = adventDay5.answer_part2()
        self.assertEqual(0, result)


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day05UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite);