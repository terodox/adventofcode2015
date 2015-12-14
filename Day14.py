from DataReader import AdventDay
import re


class AdventDayFourteen(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 14)
        self.all_reindeer = []
        self.all_results = []

    def answer_part1(self):
        total_race_time = 2503
        self.parse_all_reindeer()
        self.calculate_all_reindeer(total_race_time)
        return max(self.all_results)

    def answer_part2(self):
        self.parse_all_reindeer()
        return self.calculate_points()

    def calculate_points(self):
        for second in range(1, 2504):
            second_results = []
            for one_reindeer in self.all_reindeer:
                self.calculate_one_reindeer(one_reindeer, second)
                second_results.append(one_reindeer.total_distance)

            leader_distance = max(second_results)

            for one_reindeer in self.all_reindeer:
                if one_reindeer.total_distance == leader_distance:
                    one_reindeer.total_points += 1

        most_points = 0
        for one_reindeer in self.all_reindeer:
            most_points = max(most_points, one_reindeer.total_points)

        return most_points

    def calculate_one_reindeer(self, one_reindeer, current_time):
        one_lap = one_reindeer.run_time + one_reindeer.rest_time
        partial_lap_remaining = current_time % one_lap
        currently_running = 1\
            if partial_lap_remaining != 0 and one_reindeer.run_time >= partial_lap_remaining\
            else 0
        if currently_running == 1:
            one_reindeer.total_distance += one_reindeer.speed

    def calculate_all_reindeer(self, total_race_time):
        for one_reindeer in self.all_reindeer:
            one_lap = one_reindeer.run_time + one_reindeer.rest_time
            one_lap_distance = (one_reindeer.speed * one_reindeer.run_time)

            distance = int(total_race_time / one_lap) * one_lap_distance

            partial_lap_remaining = total_race_time % one_lap
            partial_time = one_reindeer.run_time\
                if one_reindeer.run_time < partial_lap_remaining\
                else partial_lap_remaining
            distance += partial_time * one_reindeer.speed

            self.all_results.append(distance)

    def parse_all_reindeer(self):
        for one_string in self.read_data():
            self.parse_one_reindeer(one_string)

    def parse_one_reindeer(self, one_string):
        pieces = re.findall(r'(\d+)[^\d]+(\d+)[^\d]+(\d+)', one_string)[0]
        one_reindeer = Reindeer(pieces[0], pieces[1], pieces[2])
        self.all_reindeer.append(one_reindeer)


class Reindeer:
    def __init__(self, speed, run_time, rest_time):
        self.speed = int(speed)
        self.run_time = int(run_time)
        self.rest_time = int(rest_time)
        self.total_distance = 0
        self.total_points = 0

adventDay14_1 = AdventDayFourteen()
adventDay14_2 = AdventDayFourteen()
print("Day 14 Part 1: {answer}".format(answer=adventDay14_1.answer_part1()))
print("Day 14 Part 2: {answer}".format(answer=adventDay14_2.answer_part2()))