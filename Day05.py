from DataReader import *
import re
from itertools import groupby


class AdventDayFive(AdventDay):
    def answer_part1(self):
        count = 0
        for one_string in self.read_data():
            if len(re.findall(r'ab|cd|pq|xy', one_string)):
                continue

            if len(re.findall(r'a|e|i|o|u', one_string)) < 3:
                continue

            if len(re.findall(r'(.)\1+', one_string)) > 0:
                count += 1

        return count

    def answer_part2(self):
        count = 0
        for one_string in self.read_data():
            if len(re.findall(r'(..).*?\1', one_string)) == 0:
                continue

            if len(re.findall(r'(.).\1', one_string)) > 0:
                count += 1
#            previous = ['', '']
#            for char in one_string:
#                if previous[1] == char and previous[0] != char:
#                    count += 1
#                    break
#                previous[1] = previous[0]
#                previous[0] = char

        return count


print("Day 5 Part 1: {answer}".format(answer=AdventDayFive(5).answer_part1()))
print("Day 5 Part 2: {answer}".format(answer=AdventDayFive(5).answer_part2()))