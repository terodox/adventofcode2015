from DataReader import AdventDay
import re


class AdventDayNineteen(AdventDay):
    input_value = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

    def __init__(self):
        AdventDay.__init__(self, 19)
        self.answers_part2 = 0

    def answer_part1(self):
        answers = set()
        replacements_array = self.parse_replacements()
        for one_replacement in replacements_array:
            replacement = one_replacement[0]
            replace_with = one_replacement[1]
            start_point = 0
            while start_point != -1:
                new_combination = self.replace_one_instance(self.input_value, replacement, replace_with, start_point)
                if new_combination[0] != -1:
                    answers.add(new_combination[1])
                    start_point = new_combination[0] + 1
                    if start_point == len(self.input_value):
                        start_point = -1
                else:
                    start_point = -1

        return len(answers)

    def answer_part2(self):
        replacements = self.parse_replacements_part2()
        self.tear_down_string(self.input_value, 0, '', replacements)
        return min(self.answers_part2)

    def tear_down_string(self, input_value, replacement_count, previous_value, replacements):
        if input_value == 'e':
            if self.answers_part2 != 0 and replacement_count < self.answers_part2:
                self.answers_part2 = replacement_count
            return
        if self.answers_part2 != 0 and replacement_count >= self.answers_part2:
            return
        if input_value == previous_value:
            return

        for replacement, options in replacements.items():
            for one_option in options:
                start_point = 0
                while start_point != -1:
                    result = self.replace_one_instance(input_value, one_option, replacement, start_point)
                    if result[0] != -1:
                        self.tear_down_string(result[1], replacement_count + 1, input_value, replacements)
                        if result[1] == 'e':
                            return
                        start_point = result[0]
                        if start_point == len(input_value):
                            start_point = -1
                    else:
                        start_point = -1
        return

    def parse_replacements_part2(self):
        replacements = {}
        for one_string in self.read_data():
            parts = re.findall(r'(\w+) => (\w+)', one_string)[0]
            if parts[0] not in replacements.keys():
                replacements[parts[0]] = []
            replacements[parts[0]].append(parts[1])

        sorted_replacements = {}
        for replacement, value in replacements.items():
            sorted_replacements[replacement] = sorted(value, key=len, reverse=True)

        return sorted_replacements


    @staticmethod
    def replace_one_instance(input, replacement, replace_with, start_point):
        index = input.find(replacement, start_point)
        if index == -1:
            return [-1, '']
        begin_part = input[:index]
        end_part = re.sub(replacement, replace_with, input[index:], 1)
        return [index, begin_part + end_part]

    def parse_replacements(self):
        replacements = []
        for one_string in self.read_data():
            parts = re.findall(r'(\w+) => (\w+)', one_string)[0]
            replacements.append(parts)

        return replacements


adventDay19_1 = AdventDayNineteen()
adventDay19_2 = AdventDayNineteen()
print("Day 19 Part 1: {answer}".format(answer=adventDay19_1.answer_part1()))
print("Day 19 Part 2: {answer}".format(answer=adventDay19_2.answer_part2()))
