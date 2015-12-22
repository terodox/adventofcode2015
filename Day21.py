from copy import deepcopy
from DataReader import AdventDay


class AdventDayTwentyOne(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 21)
        self.store = {
            'Weapons': [
                Item(8, 4, 0),
                Item(10, 5, 0),
                Item(25, 6, 0),
                Item(40, 7, 0),
                Item(74, 8, 0)
            ],
            'Armor': [
                Item(0, 0, 0), # No Armore option
                Item(13, 0, 1),
                Item(31, 0, 2),
                Item(53, 0, 3),
                Item(75, 0, 4),
                Item(102, 0, 5)
            ],
            'Rings': [
                Item(0, 0, 0), # No ring option
                Item(0, 0, 0), # No ring option
                Item(25, 1, 0),
                Item(50, 2, 0),
                Item(100, 3, 0),
                Item(20, 0, 1),
                Item(40, 0, 2),
                Item(80, 0, 3)
            ]
        }
        self.boss = Character(104, 1, 8)
        self.me = Character(100, 0, 0)

    def answer_part1(self):
        item_combinations = self.build_all_combinations()
        min_cost = -9
        for combination in item_combinations:
            current_run = self.apply_item_set(combination)
            if min_cost == -9 or min_cost > current_run[1]:
                i_win = self.do_i_win(current_run[0])
                if i_win:
                    min_cost = current_run[1]
        return min_cost

    def answer_part2(self):
        item_combinations = self.build_all_combinations()
        max_cost = 0
        for combination in item_combinations:
            current_run = self.apply_item_set(combination)
            if max_cost < current_run[1]:
                i_win = self.do_i_win(current_run[0])
                if not i_win:
                    max_cost = current_run[1]
        return max_cost

    def apply_item_set(self, item_combination):
        equipped = deepcopy(self.me)
        cost = 0
        for item in item_combination:
            equipped.attack += item.attack
            equipped.armor += item.armor
            cost += item.cost

        return [equipped, cost]

    def build_all_combinations(self):
        item_combinations = []
        for weapon in self.store['Weapons']:
            for armor in self.store['Armor']:
                for ring1 in self.store['Rings']:
                    for ring2 in self.store['Rings']:
                        if ring1 != ring2:
                            item_combinations.append([weapon, armor, ring1, ring2])
        return item_combinations

    def do_i_win(self, me):
        boss = deepcopy(self.boss)

        while me.hit_points > 0:
            boss.hit_points -= max(me.attack - boss.armor, 1)
            if boss.hit_points <= 0:
                return True
            me.hit_points -= max(boss.attack - me.armor, 1)

        return False


class Character:
    def __init__(self, hit_points, armor, attack):
        self.hit_points = hit_points
        self.armor = armor
        self.attack = attack


class Item:
    def __init__(self, cost, attack, armor):
        self.cost = cost
        self.attack = attack
        self.armor = armor

adventDay21 = AdventDayTwentyOne()
print("Day 21 Part 1: {answer}".format(answer=adventDay21.answer_part1()))
print("Day 21 Part 2: {answer}".format(answer=adventDay21.answer_part2()))
