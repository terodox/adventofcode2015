from DataReader import DataReader


class AdventDayThree:
    def get_answer_part1(self):
        #2572
        position = Position(0, 0)
        houses = {self.get_dict_key_from_position(position): True}
        for move in DataReader.read_data(day=3)[0]:
            position = AdventDayThree.adjust_pos_for_move(position, move)
            houses[self.get_dict_key_from_position(position)] = True

        return len(houses.keys())

    def get_answer_part2(self):
        #2631
        santa = Position(0, 0)
        robot = Position(0, 0)
        houses = {self.get_dict_key_from_position(santa): True}
        move_count = 0
        for move in DataReader.read_data(day=3)[0]:
            move_count += 1
            if move_count % 2:
                santa = self.adjust_pos_for_move(santa, move)
                houses[self.get_dict_key_from_position(santa)] = True
            else:
                robot = self.adjust_pos_for_move(robot, move)
                houses[self.get_dict_key_from_position(robot)] = True

        return len(houses.keys())

    @staticmethod
    def adjust_pos_for_move(position, move):
        if move == '^':
            position.y += 1
        elif move == 'v':
            position.y -= 1
        elif move == '>':
            position.x += 1
        elif move == '<':
            position.x -= 1
        return position

    @staticmethod
    def get_dict_key_from_position(position):
        return str(position.x) + ',' + str(position.y)


class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

advent_day3 = AdventDayThree()
print("Day 3 Part 1: {answer}".format(answer=advent_day3.get_answer_part1()))
print("Day 3 Part 2: {answer}".format(answer=advent_day3.get_answer_part2()))
