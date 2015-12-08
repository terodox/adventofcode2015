from DataReader import DataReader


class AdventDayOne:
    @staticmethod
    def get_answer_part1():
        result = 0
        for paren in DataReader.read_data(1)[0]:
            result += 1 if paren == '(' else -1

        return result

    @staticmethod
    def get_answer_part2():
        result = 0
        char_step = 0;
        for paren in DataReader.read_data(1)[0]:
            char_step += 1
            result += 1 if paren == '(' else -1
            if result < 0:
                return char_step


print("Part 1: {answer}".format(answer=AdventDayOne.get_answer_part1()))
print("Part 2: {answer}".format(answer=AdventDayOne.get_answer_part2()))
