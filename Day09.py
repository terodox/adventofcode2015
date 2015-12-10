from DataReader import AdventDay
import re


class AdventDayNine(AdventDay):
    cities = {}
    final_paths = {}

    def answer_part1(self):
        self.cities = {}
        self.final_paths = {}
        self.parse_all_paths()
        self.get_all_possible_distances()

        min_distance = 0
        for one_path, one_distance in self.final_paths.items():
            if min_distance == 0 or min_distance > one_distance:
                min_distance = one_distance

        return min_distance

    def answer_part2(self):
        self.cities = {}
        self.final_paths = {}
        self.parse_all_paths()
        self.get_all_possible_distances()

        max_distance = 0
        for one_path, one_distance in self.final_paths.items():
            if max_distance < one_distance:
                max_distance = one_distance

        return max_distance

    def get_all_possible_distances(self):
        for one_city, child_cities in dict(self.cities).items():
            self.build_all_possible_paths(one_city, child_cities, [], 0, 0)

    def build_all_possible_paths(self,
                                 current_city_name,
                                 child_cities,
                                 previous_cities,
                                 total_distance,
                                 previous_distance):
        if current_city_name in previous_cities:
            if len(previous_cities) == len(self.cities.items()):
                self.final_paths[''.join(previous_cities)] = total_distance
            return

        previous = list(previous_cities)
        previous.append(current_city_name)
        total_distance += previous_distance

        for one_city_name, one_city_distance in child_cities.items():
            self.build_all_possible_paths(
                one_city_name,
                self.cities[one_city_name],
                previous,
                total_distance,
                one_city_distance
            )

    def parse_all_paths(self):
        for one_path in self.read_data():
            self.parse_one_path(one_path)

    def parse_one_path(self, one_path):
        path_parts = re.findall(r'([^\s]+)\sto\s([^\s]+)\s=\s([^\s]+)', one_path)[0]
        city1 = path_parts[0]
        city2 = path_parts[1]
        distance = path_parts[2]
        self.add_update_city(city1, city2, int(distance))
        self.add_update_city(city2, city1, int(distance))

    def add_update_city(self, city_name1, city_name2, distance):
        if city_name1 not in self.cities:
            self.cities[city_name1] = {city_name2: distance}
        elif city_name2 not in self.cities[city_name1]:
            self.cities[city_name1][city_name2] = distance


adventDay9 = AdventDayNine(9)
print("Day 9 Part 1: {answer}".format(answer=adventDay9.answer_part1()))
print("Day 9 Part 2: {answer}".format(answer=adventDay9.answer_part2()))