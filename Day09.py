from DataReader import AdventDay
import re


class AdventDayNine(AdventDay):
    def answer_part1(self):
        print("")

    def parse_one_path(self, one_path):
        path_parts = re.findall(r'([^\s]+)\s([^\s]+)\s=\s([^\s]+)', one_path)


class City:
    def __init__(self, city):
        self.city = city
        self.desintations = {}

    def add_destination(self, city, distance):
        self.desintations[city] = distance