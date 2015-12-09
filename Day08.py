from DataReader import AdventDay, DataReader
import re


class AdventDayEight(AdventDay):
    CARRAIGE_RETURN_LENGTH = 1

    def answer_part1(self):
        str_total = 0
        literal_total = 0
        for one_string in self.read_data():
            str_total += self.calculate_string_length(one_string)
            literal_total += self.calculate_literal_length(one_string)

        return literal_total - str_total

    def answer_part2(self):
        literal_total = 0
        escaped_length = 0
        for one_string in self.read_data():
            literal_total += self.calculate_literal_length(one_string)
            escaped_length += self.calculate_escaped_string_length(one_string)

        return escaped_length - literal_total

    @staticmethod
    def calculate_string_length(one_string):
        fix_string_start = str(one_string)[1:]
        fix_string_ending = fix_string_start.replace('"\n', '')
        backslashes_fixed = fix_string_ending.replace('\\\\', 'H')
        double_quotes_fixed = backslashes_fixed.replace('\\\"', 'H')
        hex_codes_fixed = re.sub(r'\\x[\w][\w]', 'H', double_quotes_fixed)
        return len(hex_codes_fixed)

    def calculate_literal_length(self, one_string):
        str_length = len(one_string)
        return str_length - self.CARRAIGE_RETURN_LENGTH

    @staticmethod
    def calculate_escaped_string_length(one_string):
        fix_string_ending = str(one_string).replace('\n', '')
        backslashes_fixed = fix_string_ending.replace('\\', 'HH')
        quotes_fixed = backslashes_fixed.replace('\"', 'HH')
        return len(quotes_fixed) + 2


adventDay8 = AdventDayEight(8)
print("Day 8 Part 1: {answer}".format(answer=adventDay8.answer_part1()))
print("Day 8 Part 2: {answer}".format(answer=adventDay8.answer_part2()))