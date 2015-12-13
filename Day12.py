from DataReader import AdventDay
import re
import json


class AdventDayTwelve(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 12)

    def answer_part1(self):
        the_one_string = self.read_data()[0]
        return self.sum_all_numbers(the_one_string)

    def answer_part2(self):
        the_one_string = self.read_data()[0]

        json_obj = json.loads(the_one_string)
        final_obj = self.remove_red_data(json_obj)
        final_string = json.dumps(final_obj)

        input_len = len(the_one_string)
        rr_len = len(final_string)

        return self.sum_all_numbers(final_string)

    @staticmethod
    def sum_all_numbers(input_string):
        all_number_strings = re.findall(r'(\-?\d+)', input_string)
        all_numbers = []
        for one_string in all_number_strings:
            all_numbers.append(int(one_string))

        return sum(all_numbers)

    def remove_red_data(self, json_obj):
        if type(json_obj) is dict:
            if 'red' in dict(json_obj).values():
                return {}
            else:
                final_obj = {}
                for one_key, one_value in json_obj.items():
                    final_obj[one_key] = self.remove_red_data(one_value)

                return final_obj
        elif type(json_obj) is list:
            # list case
            final_obj = []
            for one_thing in json_obj:
                final_obj.append(self.remove_red_data(one_thing))
            return final_obj
        else:
            return json_obj

adventDay12 = AdventDayTwelve()
print("Day 12 Part 1: {answer}".format(answer=adventDay12.answer_part1()))
print("Day 12 Part 1: {answer}".format(answer=adventDay12.answer_part2()))