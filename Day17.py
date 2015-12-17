from DataReader import AdventDay


class AdventDaySeventeen(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 17)
        self.containers = []
        self.results = []
        self.min_containers = []

    def answer_part1(self):
        self.load_containers()
        self.find_container_combinations(150)

        return len(self.results)

    def answer_part2(self):
        min_result = self.results[0]
        for one_result in self.results:
            if one_result['count'] < min_result['count']:
                min_result = one_result

        final_count = 0
        for one_result in self.results:
            if one_result['count'] == min_result['count']:
                final_count += 1

        return final_count

    def load_containers(self):
        for one_container in self.read_data():
            self.containers.append(int(one_container))

        self.containers = sorted(self.containers)

    def find_container_combinations(self, size):
        twenty_bits_all_on = (1 << len(self.containers)) - 1
        for bits in range(1, twenty_bits_all_on + 1):
            result = self.calculate_answer_for_bits(bits)
            if result['value'] == size:
                self.results.append(result)

    def calculate_answer_for_bits(self, bits):
        total_value = 0
        container_count = 0
        for index in range(0, len(self.containers)):
            and_mask = (1 << index)
            if bits & and_mask > 0:
                total_value += self.containers[index]
                container_count += 1

        return {'value': total_value, 'count': container_count, 'bits': bits}

adventDay17_1 = AdventDaySeventeen()
print("Day 17 Part 1: {answer}".format(answer=adventDay17_1.answer_part1()))
print("Day 17 Part 2: {answer}".format(answer=adventDay17_1.answer_part2()))
