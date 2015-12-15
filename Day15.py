from DataReader import AdventDay
import re


class AdventDayFifteen(AdventDay):
    all_ingredients = []
    results = []

    def __init__(self):
        AdventDay.__init__(self, 15)

    def answer_part1(self):
        print("")

    def answer_part2(self):
        print("")

    def calculate_all_combinations(self):
        ingredient_mix = [97, 1, 1, 1]
        while ingredient_mix[0] >= 1:
            self.results.append(self.calculate_mix_value(ingredient_mix))

    def calculate_mix_value(self, ingredient_mix):
        capacity_total = 0
        durability_total = 0
        flavor_total = 0
        texture_total = 0

        for count in range(0, len(ingredient_mix)):
            capacity_total += ingredient_mix[count] * self.all_ingredients[count].capacity
            durability_total += ingredient_mix[count] * self.all_ingredients[count].durability
            flavor_total += ingredient_mix[count] * self.all_ingredients[count].flavor
            texture_total += ingredient_mix[count] * self.all_ingredients[count].texture

        return capacity_total * durability_total * flavor_total * texture_total

    def reset_ingredient_count(self):
        for name, ingredient in self.all_ingredients:
            ingredient.count = 0

    def parse_all_ingredients(self):
        for one_string in self.read_data():
            self.parse_one_ingredient(one_string)

    def parse_one_ingredient(self, one_string):
        parts = re.findall(r'^(\w+):.*?(-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+), \w+ (-?\d+)', one_string)[0]
        self.all_ingredients.append(Ingredient(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            parts[5]
        ))

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)
        self.count = 0


adventDay15_1 = AdventDayFifteen()
adventDay15_2 = AdventDayFifteen()
print("Day 15 Part 1: {answer}".format(answer=adventDay15_1.answer_part1()))
print("Day 15 Part 2: {answer}".format(answer=adventDay15_1.answer_part2()))