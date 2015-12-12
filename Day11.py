from DataReader import AdventDay
import re

class AdventDayEleven(AdventDay):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        AdventDay.__init__(self, 11)

    def answer_part1(self):
        input_string = 'hepxcrrq'
        return self.get_next_valid_string(input_string)

    def answer_part2(self):
        input_string = 'hepxxzaa'
        return self.get_next_valid_string(input_string)

    def get_next_valid_string(self, input_string):
        working_string = str(input_string)
        while not self.is_valid(working_string):
            working_string = self.increment_string(working_string)

        return working_string

    def is_valid(self, one_string):
        if len(re.findall(r'[iol]', one_string)):
            return False
        if len(re.findall(r'(.)\1.*?([^\1])\2', one_string)) == 0:
            return False
        current_triplet = ''
        for char in one_string:
            current_triplet += char
            if len(current_triplet) == 4:
                current_triplet = current_triplet[1:]
            if len(current_triplet) == 3:
                if len(re.findall(current_triplet, self.alphabet)):
                    return True
        return False

    def increment_string(self, one_string):
        reversed_string = str(one_string)[::-1]
        reverse_final_string = ''
        increment_next = True
        for char in reversed_string:
            if increment_next:
                increment_next = False
                current_index = self.alphabet.index(char)
                if current_index == 25:
                    current_index = 0
                    increment_next = True
                else:
                    current_index += 1
                reverse_final_string += self.alphabet[current_index]
            else:
                reverse_final_string += char

        final_string = reverse_final_string[::-1]
        return final_string

adventDay11 = AdventDayEleven()
print("Day 11 Part 1: {answer}".format(answer=adventDay11.answer_part1()))
print("Day 11 Part 2: {answer}".format(answer=adventDay11.answer_part2()))