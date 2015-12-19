from DataReader import AdventDay


class AdventDayEighteen(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 18)

    def answer_part1(self):
        lights = self.get_initial_lights()
        for count in range(0, len(lights)):
            lights = self.iterate_lights(lights)
        return self.count_lights(lights)

    def answer_part2(self):
        lights = self.get_initial_lights()

        lights = self.turn_on_corners(lights)

        for count in range(0, len(lights)):
            lights = self.iterate_lights(lights)
            lights = self.turn_on_corners(lights)
        return self.count_lights(lights)

    @staticmethod
    def turn_on_corners(lights):
        lights[0][0] = 1
        lights[0][len(lights[0]) - 1] = 1
        lights[len(lights) - 1][0] = 1
        lights[len(lights) - 1][len(lights[0]) - 1] = 1
        return lights

    def iterate_lights(self, lights_in):
        lights_out = [[0 for _ in range(len(lights_in[0]))] for _ in range(len(lights_in))]
        for row in range(0, len(lights_in)):
            for column in range(0, len(lights_in[0])):
                neighbors_value = self.get_neighbors_value(lights_in, row, column)
                if lights_in[row][column] and neighbors_value in [2, 3]:
                    lights_out[row][column] = 1
                elif not lights_in[row][column] and neighbors_value == 3:
                    lights_out[row][column] = 1
                else:
                    lights_out[row][column] = 0

        return lights_out


    @staticmethod
    def get_neighbors_value(lights, row, column):
        neighbors_value = 0
        for vertical in range(-1, 2):
            y = vertical + row
            if len(lights) > y >= 0:
                for horizontal in range(-1, 2):
                    x = horizontal + column
                    if len(lights) > x >= 0:
                        if x == column and y == row:
                            continue
                        neighbors_value += lights[y][x]
        return neighbors_value

    @staticmethod
    def count_lights(lights):
        return sum(sum(lights, []))

    def get_initial_lights(self):
        lights = []
        for one_string in self.read_data():
            column_list = []
            one_string = one_string[:len(one_string) - 1]
            for char in one_string:
                if char is '#':
                    column_list.append(1)
                else:
                    column_list.append(0)
            lights.append(column_list)
        return lights

adventDay18_1 = AdventDayEighteen()
adventDay18_2 = AdventDayEighteen()
print("Day 18 Part 1: {answer}".format(answer=adventDay18_1.answer_part1()))
print("Day 18 Part 2: {answer}".format(answer=adventDay18_2.answer_part2()))
