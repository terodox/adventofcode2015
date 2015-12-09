from DataReader import AdventDay
import re


class AdventDayNine(AdventDay):
    cities = {}

    def answer_part1(self):
        self.parse_all_paths()
        all_distances = self.get_all_possible_distances()

    def get_all_possible_distances(self):
        final_paths = {}
        for one_city, child_cities in dict(self.cities).items():
            final = self.build_all_possible_paths(one_city, child_cities, [], 0)
            final_paths

        return final_paths

    def build_all_possible_paths(self, current_city_name, child_cities, previous_cities, distance):
        previous = list(previous_cities)
        previous.append(current_city_name)

        final_paths = {}

        for one_city, one_city_distance in dict(child_cities).items():
            # Add check for if city is already in previous_cities
            if one_city in previous_cities:
                final_paths[''.join(previous_cities)] = distance

            new_distance = distance + one_city_distance
            final_path, final_distance = self.build_all_possible_paths(one_city, self.cities[one_city], previous, new_distance)
            final_paths[final_path] = final_distance

        return final_paths

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
