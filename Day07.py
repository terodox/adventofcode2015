from DataReader import AdventDay
from enum import Enum
import re
import ctypes


class AdventDaySeven(AdventDay):
    wiring = {}

    def answer_part1(self):
        self.parse_input()
        return self.calculate_value_part1('a')

    def answer_part2(self):
        self.parse_input()
        return self.calculate_value_part2('a')

    def calculate_value_part1(self, wire_name):
        current_wire = self.wiring[wire_name]
        if current_wire.value is None:
            if current_wire.operator == Operator.Noop and self.represents_int(current_wire.inputs[0]):
                self.wiring[wire_name].value = int(current_wire.inputs[0])
                return self.wiring[wire_name].value

            values = []
            for one_wire_name in current_wire.inputs:
                if self.represents_int(one_wire_name):
                    values.append(int(one_wire_name))
                else:
                    values.append(self.calculate_value_part1(one_wire_name))

            self.wiring[wire_name].value = self.apply_operator(current_wire.operator, values)
            return self.wiring[wire_name].value
        else:
            return current_wire.value

    def calculate_value_part2(self, wire_name):
        if wire_name is 'b':
            return 3176

        current_wire = self.wiring[wire_name]
        if current_wire.value is None:
            if current_wire.operator == Operator.Noop and self.represents_int(current_wire.inputs[0]):
                self.wiring[wire_name].value = int(current_wire.inputs[0])
                return self.wiring[wire_name].value

            values = []
            for one_wire_name in current_wire.inputs:
                if self.represents_int(one_wire_name):
                    values.append(int(one_wire_name))
                else:
                    values.append(self.calculate_value_part2(one_wire_name))

            self.wiring[wire_name].value = self.apply_operator(current_wire.operator, values)
            return self.wiring[wire_name].value
        else:
            return current_wire.value

    @staticmethod
    def apply_operator(operator, values):
        if operator == Operator.LShift:
            return ctypes.c_uint16(values[0] << values[1]).value
        if operator == Operator.RShift:
            return ctypes.c_uint16(values[0] >> values[1]).value
        if operator == Operator.And:
            return ctypes.c_uint16(values[0] & values[1]).value
        if operator == Operator.Or:
            return ctypes.c_uint16(values[0] | values[1]).value
        if operator == Operator.Not:
            return ctypes.c_uint16(~values[0]).value
        if operator == Operator.Noop:
            return values[0]

    def parse_input(self):
        for one_string in self.read_data():
            one_wire = self.parse_wire(one_string)
            self.wiring[one_wire.name] = one_wire

    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def parse_wire(one_input):
        operator = Operator.Noop
        one_wire = None
        one_string = str(one_input).lower()
        if 'not' in one_string:
            find_result = re.findall(r'NOT ([^\s]+).*->\s([^\s]+)', one_input)
            pieces = find_result[0]
            one_wire = Wire(
                name=pieces[1],
                inputs=[pieces[0]],
                operator=Operator.Not
            )
        elif 'lshift' in one_string:
            operator = Operator.LShift
        elif 'rshift' in one_string:
            operator = Operator.RShift
        elif 'and' in one_string:
            operator = Operator.And
        elif 'or' in one_string:
            operator = Operator.Or
        else:
            find_result = re.findall(r'([^\s]+).*->\s([^\s]+)', one_input)
            pieces = find_result[0]
            one_wire = Wire(
                name=pieces[1],
                inputs=[pieces[0]],
                operator=Operator.Noop
            )

        if one_wire is None:
            find_result = re.findall(r'([^\s]+)\s([^\s]+)\s([^\s]+)\s->\s([^\s]+)', one_input)
            pieces = find_result[0]
            one_wire = Wire(
                name=pieces[3],
                inputs=[pieces[0], pieces[2]],
                operator=operator
            )

        return one_wire


class Wire:
    def __init__(self, name, inputs, operator):
        if type(operator) is not Operator:
            raise ValueError("Must be of type {type}".format(type=type(Operator)))

        self.name = name
        self.inputs = inputs
        self.operator = operator
        self.value = None


class Operator(Enum):
    LShift = 0
    RShift = 1
    And = 2
    Or = 3
    Not = 4
    Noop = 99

adventDay7 = AdventDaySeven(7)
print("Day 7 part 1: {answer}".format(answer=adventDay7.answer_part1()))
print("Day 7 part 2: {answer}".format(answer=adventDay7.answer_part2()))
