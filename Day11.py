from DataReader import AdventDay
import re

class AdventDayEleven(AdventDay):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        AdventDay.__init__(self, 11)

    def answer_part1(self):
        print("")

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
        print("")
