from DataReader import AdventDay
import re


class AdventDayTwentyThree(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 23)

    def answer_part1(self):
        instructions = self.parse_instructions()
        values = {'a': 0, 'b': 0, 'index': 0}
        while values['index'] < len(instructions):
            instruction = instructions[values['index']]
            values = instruction[1](values, instruction[0])

        return values['b']

    def answer_part2(self):
        instructions = self.parse_instructions()
        values = {'a': 1, 'b': 0, 'index': 0}
        while values['index'] < len(instructions):
            instruction = instructions[values['index']]
            values = instruction[1](values, instruction[0])

        return values['b']

    def parse_instructions(self):
        instructions = []
        for one_instruction in self.read_data():
            new_instruction = lambda a: a
            half = re.findall(r'hlf (\w)', one_instruction)
            triple = re.findall(r'tpl (\w)', one_instruction)
            inc = re.findall(r'inc (\w)', one_instruction)
            jump = re.findall(r'jmp ([+-])(\d+)', one_instruction)
            jump_if_even = re.findall(r'jie (\w), ([+-])(\d+)', one_instruction)
            jump_if_one = re.findall(r'jio (\w), ([+-])(\d+)', one_instruction)

            if len(half):
                half = half[0]
                if half[0] == 'a':
                    new_instruction = [0, lambda reg_index, nothing: {'a': int(reg_index['a']/2), 'b': reg_index['b'], 'index': reg_index['index'] + 1}]
                else:
                    new_instruction = [0, lambda reg_index, nothing: {'a': reg_index['a'], 'b': int(reg_index['b']/2), 'index': reg_index['index'] + 1}]
            elif len(triple):
                triple = triple[0]
                if triple[0] == 'a':
                    new_instruction = [0, lambda reg_index, nothing: {'a': reg_index['a'] * 3, 'b': reg_index['b'], 'index': reg_index['index'] + 1}]
                else:
                    new_instruction = [0, lambda reg_index, nothing: {'a': reg_index['a'], 'b': reg_index['b'] * 3, 'index': reg_index['index'] + 1}]
            elif len(inc):
                inc = inc[0]
                if inc[0] == 'a':
                    new_instruction = [0, lambda reg_index, nothing: {'a': reg_index['a'] + 1, 'b': reg_index['b'], 'index': reg_index['index'] + 1}]
                else:
                    new_instruction = [0, lambda reg_index, nothing: {'a': reg_index['a'], 'b': reg_index['b'] + 1, 'index': reg_index['index'] + 1}]
            elif len(jump):
                jump = jump[0]
                jump_value = int(jump[1])
                if jump[0] == '-':
                    jump_value *= -1
                new_instruction = [jump_value, lambda reg_index, jump_by: {'a': reg_index['a'], 'b': reg_index['b'], 'index': reg_index['index'] + jump_by}]
            elif len(jump_if_even):
                jump_if_even = jump_if_even[0]
                jump_value = int(jump_if_even[2])
                if jump_if_even[1] == '-':
                    jump_value *= -1
                if jump_if_even[0] == 'a':
                    new_instruction = [jump_value, lambda reg_index, jump_by: {
                        'a': reg_index['a'],
                        'b': reg_index['b'],
                        'index': reg_index['index'] + jump_by if reg_index['a'] % 2 == 0 else reg_index['index'] + 1}]
                else:
                    new_instruction = [jump_value, lambda reg_index, jump_by: {
                        'a': reg_index['a'],
                        'b': reg_index['b'],
                        'index': reg_index['index'] + jump_by if reg_index['b'] % 2 == 0 else reg_index['index'] + 1}]
            elif len(jump_if_one):
                jump_if_one = jump_if_one[0]
                jump_value = int(jump_if_one[2])
                if jump_if_one[1] == '-':
                    jump_value *= -1
                if jump_if_one[0] == 'a':
                    new_instruction = [jump_value, lambda reg_index, jump_by: {
                        'a': reg_index['a'],
                        'b': reg_index['b'],
                        'index': reg_index['index'] + jump_by if reg_index['a'] == 1 else reg_index['index'] + 1}]
                else:
                    new_instruction = [jump_value, lambda reg_index, jump_by: {
                        'a': reg_index['a'],
                        'b': reg_index['b'],
                        'index': reg_index['index'] + jump_by if reg_index['b'] == 1 else reg_index['index'] + 1}]
            instructions.append(new_instruction)
        return instructions


adventDay23 = AdventDayTwentyThree()
print("Day 23 Part 1: {answer}".format(answer=adventDay23.answer_part1()))
print("Day 23 Part 2: {answer}".format(answer=adventDay23.answer_part2()))