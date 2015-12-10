from DataReader import AdventDay


class AdventDayTen(AdventDay):
    cities = {}
    final_paths = {}

    def answer_part1(self):
        input_string = '1113222113'
        result = self.run_transforms(input_string, 40)
        return len(result)

    def answer_part2(self):
        input_string = '1113222113'
        result = self.run_transforms(input_string, 50)
        return len(result)

    @staticmethod
    def run_transforms(input_string, transform_count):
        for one_string in range(0, transform_count):
            input_string = AdventDayTen.transform_string(input_string)
        return input_string

    @staticmethod
    def transform_string(input_string):
        final_string = ''
        initial_string = str(input_string)
        current_string = None
        for char in initial_string:
            if current_string is None:
                current_string = {char: 1}
            elif list(current_string.keys())[0] == char:
                current_string[char] += 1
            else:
                old_string = list(current_string.keys())[0]
                final_string += str(current_string[old_string]) + old_string
                current_string = {char: 1}

        old_string = list(current_string.keys())[0]
        final_string += str(current_string[old_string]) + old_string

        return final_string

adventDay10 = AdventDayTen(10)
print("Day 10 Part 1: {answer}".format(answer=adventDay10.answer_part1()))
print("Day 10 Part 1: {answer}".format(answer=adventDay10.answer_part2()))