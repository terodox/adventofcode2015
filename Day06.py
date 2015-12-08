from DataReader import AdventDay
from enum import Enum
import re


class AdventDaySix(AdventDay):
    lights = {}

    def answer_part1(self):
        command_array = self._parse_file()
        for grid_command in command_array:
            if grid_command.command == CommandType.on:
                self._change_lights_part1(grid_command, True)
            if grid_command.command == CommandType.off:
                self._change_lights_part1(grid_command, False)
            if grid_command.command == CommandType.toggle:
                self._toggle_lights_part1(grid_command)

        count = 0
        for one_key in self.lights.keys():
            if self.lights[one_key]:
                count += 1

        return count

    def answer_part2(self):
        command_array = self._parse_file()
        for grid_command in command_array:
            if grid_command.command == CommandType.on:
                self._change_lights_part2(grid_command, 1)
            if grid_command.command == CommandType.off:
                self._change_lights_part2(grid_command, -1)
            if grid_command.command == CommandType.toggle:
                self._change_lights_part2(grid_command, 2)

        count = 0
        for one_key in self.lights.keys():
            count += self.lights[one_key]

        return count

    def _change_lights_part2(self, grid_command, on_off_value):
        for x_coord in range(int(grid_command.grid_coord_start.x), int(grid_command.grid_coord_end.x) + 1):
            for y_coord in range(int(grid_command.grid_coord_start.y), int(grid_command.grid_coord_end.y) + 1):
                key = str(x_coord) + "," + str(y_coord)

                if key not in self.lights:
                    self.lights[key] = 0

                self.lights[key] += on_off_value
                if self.lights[key] < 0:
                    self.lights[key] = 0

    def _change_lights_part1(self, grid_command, on_off_value):
        for x_coord in range(int(grid_command.grid_coord_start.x), int(grid_command.grid_coord_end.x) + 1):
            for y_coord in range(int(grid_command.grid_coord_start.y), int(grid_command.grid_coord_end.y) + 1):
                self.lights[str(x_coord) + "," + str(y_coord)] = on_off_value

    def _toggle_lights_part1(self, grid_command):
        for x_coord in range(int(grid_command.grid_coord_start.x), int(grid_command.grid_coord_end.x) + 1):
            for y_coord in range(int(grid_command.grid_coord_start.y), int(grid_command.grid_coord_end.y) + 1):
                key = str(x_coord) + "," + str(y_coord)
                if key in self.lights:
                    self.lights[key] = not self.lights[key]
                else:
                    self.lights[key] = True

    def _parse_file(self):
        command_array = []
        for one_string in self.read_data():
            command = self._get_command(one_string)
            all_coords = self._get_coords(one_string)[0:4]
            x1 = all_coords[0]
            y1 = all_coords[1]
            x2 = all_coords[2]
            y2 = all_coords[3]
            command_array.append(GridCommand(
                command=command,
                grid_coord_start=Coordinate(
                    x=x1,
                    y=y1
                ),
                grid_coord_end=Coordinate(
                    x=x2,
                    y=y2
                )
            ))
        return command_array

    @staticmethod
    def _get_command(one_string):
        if str(one_string).startswith("toggle"):
            return CommandType.toggle
        elif str(one_string).startswith("turn on"):
            return CommandType.on
        else:
            return CommandType.off

    @staticmethod
    def _get_coords(one_string):
        results = re.findall(r'.*?(\d+),(\d+) through (\d+),(\d+)', one_string)
        return results[0]


class GridCommand:
    def __init__(self, command, grid_coord_start, grid_coord_end):
        self.command = command
        self.grid_coord_start = grid_coord_start
        self.grid_coord_end = grid_coord_end


class CommandType(Enum):
    on = 1
    off = 2
    toggle = 3


class Coordinate:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

adventDay6 = AdventDaySix(6)
#print("Day 6 part 1: {answer}".format(answer=adventDay6.answer_part1()))
print("Day 6 part 2: {answer}".format(answer=adventDay6.answer_part2()))