from Day18 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day18UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayEighteen()
        self.test_input = [
            '.#.#.#\n',
            '...##.\n',
            '#....#\n',
            '..#...\n',
            '#.#..#\n',
            '####..\n'
        ]
        self._sut.read_data = lambda: self.test_input

    def test_count_lights(self):
        test_input = [[1, 2], [3, 4]]
        self.assertEqual(10, self._sut.count_lights(test_input))

    def test_get_initial_lights(self):
        lights = self._sut.get_initial_lights()

        result = self._sut.count_lights(lights)

        self.assertEqual(15, result)

    def test_get_neighbors_value(self):
        lights_in = self._sut.get_initial_lights()

        self.assertEqual(1, self._sut.get_neighbors_value(lights_in, 0, 0))

    def test_iterate_lights(self):
        lights_in = self._sut.get_initial_lights()

        lights = self._sut.iterate_lights(lights_in)

        self.assertEqual(0, lights[0][0])
        self.assertEqual(0, lights[0][1])
        self.assertEqual(1, lights[0][2])
        self.assertEqual(1, lights[0][3])
        self.assertEqual(0, lights[0][4])
        self.assertEqual(0, lights[0][5])
        self.assertEqual(0, lights[1][0])
        self.assertEqual(0, lights[1][1])
        self.assertEqual(1, lights[1][2])
        self.assertEqual(1, lights[1][3])
        self.assertEqual(0, lights[1][4])
        self.assertEqual(1, lights[1][5])
        self.assertEqual(0, lights[2][0])
        self.assertEqual(0, lights[2][1])
        self.assertEqual(0, lights[2][2])
        self.assertEqual(1, lights[2][3])
        self.assertEqual(1, lights[2][4])
        self.assertEqual(0, lights[2][5])
        self.assertEqual(0, lights[3][0])
        self.assertEqual(0, lights[3][1])
        self.assertEqual(0, lights[3][2])
        self.assertEqual(0, lights[3][3])
        self.assertEqual(0, lights[3][4])
        self.assertEqual(0, lights[3][5])
        self.assertEqual(1, lights[4][0])
        self.assertEqual(0, lights[4][1])
        self.assertEqual(0, lights[4][2])
        self.assertEqual(0, lights[4][3])
        self.assertEqual(0, lights[4][4])
        self.assertEqual(0, lights[4][5])
        self.assertEqual(1, lights[5][0])
        self.assertEqual(0, lights[5][1])
        self.assertEqual(1, lights[5][2])
        self.assertEqual(1, lights[5][3])
        self.assertEqual(0, lights[5][4])
        self.assertEqual(0, lights[5][5])

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day18UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
