import math
from DataReader import AdventDay


class AdventDayTwenty(AdventDay):

    def __init__(self):
        AdventDay.__init__(self, 20)

    @staticmethod
    def answer_part1():
        input_value = 36000000
        house = {}
        for iterator in range(1, int(input_value / 10)):
            for internal_loop in range(iterator, int(input_value / 10), iterator):
                if internal_loop not in house.keys():
                    house[internal_loop] = 0
                house[internal_loop] += iterator * 10

        for key in sorted(house.keys()):
            if house[key] >= input_value:
                return key

    @staticmethod
    def answer_part2():
        target = 36000000
        part_two = None
        iterator_value = 0
        while not part_two:
            iterator_value += 1
            divisors = AdventDayTwenty.get_divisors(iterator_value)
            if not part_two:
                if not part_two and \
                        sum(divisor_value for divisor_value in divisors
                            if iterator_value / divisor_value <= 50) * 11 >= target:
                    part_two = iterator_value
        return part_two

    @staticmethod
    def get_divisors(n):
        small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
        large_divisors = [n / d for d in small_divisors if n != d * d]
        return small_divisors + large_divisors

adventDay20_1 = AdventDayTwenty()
# print("Day 20 Part 1: {answer}".format(answer=adventDay20_1.answer_part1()))
print("Day 20 Part 2: {answer}".format(answer=adventDay20_1.answer_part2()))
