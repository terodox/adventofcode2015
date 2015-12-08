from unittest import TestSuite, makeSuite, TextTestRunner, TestCase
from unittest import mock
from Day06 import AdventDaySix, CommandType, GridCommand, Coordinate


class Day06UnitTests(TestCase):
    _sut = AdventDaySix(6)

    def setUp(self):
        self._sut = AdventDaySix(6)
        self._sut.read_data = lambda: [
            'turn off 199,133 through 461,193',
            'toggle 322,558 through 977,958',
            'turn on 226,196 through 599,390'
        ]

    def test_parse_command_parses_command_correctly(self):
        results = self._sut._parse_file()

        self.assertEqual(CommandType.off, results[0].command)
        self.assertEqual(CommandType.toggle, results[1].command)
        self.assertEqual(CommandType.on, results[2].command)

    def test_parse_command_parses_coord_start_correctly(self):
        results = self._sut._parse_file()

        self.assertEqual('199', results[0].grid_coord_start.x)
        self.assertEqual('133', results[0].grid_coord_start.y)
        self.assertEqual('322', results[1].grid_coord_start.x)
        self.assertEqual('558', results[1].grid_coord_start.y)
        self.assertEqual('226', results[2].grid_coord_start.x)
        self.assertEqual('196', results[2].grid_coord_start.y)

    def test_parse_command_parses_coord_end_correctly(self):
        results = self._sut._parse_file()

        self.assertEqual('461', results[0].grid_coord_end.x)
        self.assertEqual('193', results[0].grid_coord_end.y)
        self.assertEqual('977', results[1].grid_coord_end.x)
        self.assertEqual('958', results[1].grid_coord_end.y)
        self.assertEqual('599', results[2].grid_coord_end.x)
        self.assertEqual('390', results[2].grid_coord_end.y)

    def test_change_lights_true(self):
        self._sut.lights = {
            '1,1': True,
            '2,1': True,
            '3,1': False,
            '4,1': True,
            '1,2': True,
            '2,2': True,
            '3,2': False,
            '4,2': True
        }

        grid_command = GridCommand(
            command=CommandType.on,
            grid_coord_start=Coordinate(x=1, y=1),
            grid_coord_end=Coordinate(x=5, y=2)
        )

        self._sut._change_lights_part1(grid_command, True)

        self.assertTrue(self._sut.lights['1,1'])
        self.assertTrue(self._sut.lights['2,1'])
        self.assertTrue(self._sut.lights['3,1'])
        self.assertTrue(self._sut.lights['4,1'])
        self.assertTrue(self._sut.lights['5,1'])
        self.assertTrue(self._sut.lights['1,2'])
        self.assertTrue(self._sut.lights['2,2'])
        self.assertTrue(self._sut.lights['3,2'])
        self.assertTrue(self._sut.lights['4,2'])
        self.assertTrue(self._sut.lights['5,2'])


testSuite = TestSuite()
testSuite.addTest(makeSuite(Day06UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite);