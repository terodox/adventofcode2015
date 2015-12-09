from Day09 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day09UnitTests(TestCase):
    sample_paths = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]

    def setUp(self):
        self._sut = AdventDayNine(9)
        self._sut.cities = {}

    def test_Paths_are_parsed_properly(self):
        self._sut.parse_one_path(self.sample_paths[0])
        self.assertIn('London', self._sut.cities)
        self.assertIn('Dublin', self._sut.cities)
        self.assertIn('Dublin', self._sut.cities['London'])
        self.assertIn('London', self._sut.cities['Dublin'])
        self.assertEquals(464, self._sut.cities['London']['Dublin'])
        self.assertEquals(464, self._sut.cities['Dublin']['London'])

    def test_Cities_are_added_properly(self):
        self.assertNotIn('London', self._sut.cities)

        self._sut.add_update_city('London', 'Dublin', 500)

        self.assertIn('London', self._sut.cities)
        self.assertIn('Dublin', self._sut.cities['London'])
        self.assertEquals(500, self._sut.cities['London']['Dublin'])

        self._sut.add_update_city('London', 'York', 1000)

        self.assertIn('London', self._sut.cities)
        self.assertIn('Dublin', self._sut.cities['London'])
        self.assertEquals(500, self._sut.cities['London']['Dublin'])
        self.assertIn('London', self._sut.cities)
        self.assertIn('York', self._sut.cities['London'])
        self.assertEquals(1000, self._sut.cities['London']['York'])

    def test_List_is_parsed_properly(self):
        self._sut.read_data = lambda: self.sample_paths

        self._sut.parse_all_paths()

        self.assertEquals(len(self.sample_paths), len(self._sut.cities.items()))

    def test_Gets_correct_anser_count(self):
        self._sut.read_data = lambda: self.sample_paths
        self._sut.parse_all_paths()

        result = self._sut.get_all_possible_distances()

        self.assertEquals(6, len(result))


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day09UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)