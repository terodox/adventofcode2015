from DataReader import DataReader


class AdventDayTwo:
    @staticmethod
    def answer_part_one():
        total_size = 0;
        for wrapping in DataReader.read_data(day=2):
            dimensions = wrapping.replace('\n', '').split('x')
            int_dimensions = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]
            int_dimensions = sorted(int_dimensions)

            total_size += 3 * (int_dimensions[0] * int_dimensions[1])
            total_size += 2 * (int_dimensions[1] * int_dimensions[2])
            total_size += 2 * (int_dimensions[2] * int_dimensions[0])
        return total_size

    @staticmethod
    def answer_part_two():
        total_size = 0;
        for wrapping in DataReader.read_data(day=2):
            dimensions = wrapping.replace('\n', '').split('x')
            int_dimensions = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]
            int_dimensions = sorted(int_dimensions)

            total_size += int_dimensions[0] * int_dimensions[1] * int_dimensions[2]
            total_size += (2 * int_dimensions[0]) + (2 * int_dimensions[1])

        return total_size


print("Part 1: {answer}".format(answer=AdventDayTwo.answer_part_one()))
print("Part 2: {answer}".format(answer=AdventDayTwo.answer_part_two()))
