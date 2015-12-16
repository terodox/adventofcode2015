from DataReader import AdventDay
import re


class AdventDaySixteen(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 16)
        self.aunts = {}
        self.aunt_known = {
            'children': '3',
            'cats': '7',
            'samoyeds': '2',
            'pomeranians': '3',
            'akitas': '0',
            'vizslas': '0',
            'goldfish': '5',
            'trees': '3',
            'cars': '2',
            'perfumes': '1'
        }

    def answer_part1(self):
        self.parse_all_aunts()
        for key in self.aunts:
            if self.is_match(self.aunts[key]):
                return key

    def answer_part2(self):
        self.parse_all_aunts()
        for key in sorted(self.aunts):
            if self.is_match_part2(self.aunts[key]):
                return key

    def parse_all_aunts(self):
        for one_string in self.read_data():
            self.parse_one_aunt(one_string)

    def is_match(self, one_aunt):
        for key in one_aunt:
            if one_aunt[key] != self.aunt_known[key]:
                return False

        return True

    def is_match_part2(self, one_aunt):
        for key in one_aunt:
            if key in ['cats', 'trees']:
                if self.aunt_known[key] >= one_aunt[key]:
                    return False
            elif key in ['pomeranians', 'goldfish']:
                if self.aunt_known[key] <= one_aunt[key]:
                    return False
            elif one_aunt[key] != self.aunt_known[key]:
                return False

        return True

    def parse_one_aunt(self, one_string):
        parts = re.findall('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', one_string)[0]
        self.aunts[int(parts[0])] = {
            parts[1]: parts[2],
            parts[3]: parts[4],
            parts[5]: parts[6]
        }

adventDay16_1 = AdventDaySixteen()
adventDay16_2 = AdventDaySixteen()
print("Day 16 Part 1: {answer}".format(answer=adventDay16_1.answer_part1()))
print("Day 16 Part 2: {answer}".format(answer=adventDay16_2.answer_part2()))
