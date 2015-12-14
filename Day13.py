from DataReader import AdventDay
import re


class AdventDayThirteen(AdventDay):
    ME = 'me'

    def __init__(self):
        self.all_guests = {}
        self.all_possibilities = {}
        AdventDay.__init__(self, 13)

    def answer_part1(self):
        for one_item in self.read_data():
            self.parse_one_line(one_item)

        return self.calculate_max_happiness()

    def answer_part2(self):
        for one_item in self.read_data():
            self.parse_one_line(one_item)

        me = Guest(self.ME)
        for one_guest_name in self.all_guests.keys():
            self.all_guests[one_guest_name].guests[self.ME] = 0
            me.guests[one_guest_name] = 0

        self.all_guests[self.ME] = me

        return self.calculate_max_happiness()

    def calculate_max_happiness(self):
        for one_guest_name, one_guest_obj in self.all_guests.items():
            self.every_permutation(one_guest_name, [], 0)

        return max(self.all_possibilities.values())

    def every_permutation(self, current_guest_name, previous, total_happiness):
        guest_count = len(self.all_guests.keys())

        if current_guest_name in previous:
            if len(previous) == guest_count and current_guest_name == previous[0]:
                all_guests = ''.join(previous)
                self.all_possibilities[all_guests] = total_happiness
            return

        previous_guests = previous[:]
        previous_guests.append(current_guest_name)
        for one_guest_name, guest_happiness in self.all_guests[current_guest_name].guests.items():
            current_next_happiness = guest_happiness
            next_current_happiness = self.all_guests[one_guest_name].guests[current_guest_name]
            self.every_permutation(one_guest_name,
                                   previous_guests,
                                   total_happiness + current_next_happiness + next_current_happiness)

    def parse_one_line(self, one_string):
        # Mallory would lose 89 happiness units by sitting next to George.
        parts = re.findall(r'^(\w+)\swould\s(\w+)\s(\d+).*?(\w+)\.$', one_string)[0]
        if parts[0] not in self.all_guests.keys():
            self.all_guests[parts[0]] = Guest(parts[0])

        pos_neg = 1
        if parts[1] == 'lose':
            pos_neg = -1

        self.all_guests[parts[0]].guests[parts[3]] = pos_neg * int(parts[2])


class Guest:
    def __init__(self, name):
        self.name = name
        self.name = ''
        self.guests = {}

    def add_guest(self, guest_name, happiness):
        self.guests[guest_name] = happiness

adventDay13 = AdventDayThirteen()
#print("Day 13 Part 1: {answer}".format(answer=adventDay13.answer_part1()))
print("Day 13 Part 2: {answer}".format(answer=adventDay13.answer_part2()))