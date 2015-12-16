from DataReader import AdventDay
import re


class AdventDayFifteen(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 15)
        self.all_ingredients = []
        self.results = 0

    def answer_part1(self):
        self.parse_all_ingredients()

        self.calculate_all_combinations(100)

        return self.results

    def answer_part2(self):
        self.parse_all_ingredients()

        self.calculate_all_combinations_500_calories(100)

        return self.results

    def calculate_all_combinations(self, total_teaspoons):
        for ingredient_one in range(total_teaspoons - 3, 1, -1):
            for ingredient_two in range(1, total_teaspoons - 1 - ingredient_one):
                for ingredient_three in range(1, total_teaspoons - ingredient_two - ingredient_one):
                    for ingredient_four in range(1, total_teaspoons + 1 - ingredient_three - ingredient_two - ingredient_one):
                        ingredient_mix = [ingredient_one, ingredient_two, ingredient_three, ingredient_four]
                        if sum(ingredient_mix) != total_teaspoons:
                            continue
                        mix_value = self.calculate_mix_value(ingredient_mix)
                        if self.results < mix_value:
                            self.results = mix_value

    def calculate_all_combinations_500_calories(self, total_teaspoons):
        for ingredient_one in range(total_teaspoons - 3, 1, -1):
            if ingredient_one % 100 == 0:
                print("Ingredient One: " + str(ingredient_one))
            for ingredient_two in range(1, total_teaspoons - 1 - ingredient_one):
                for ingredient_three in range(1, total_teaspoons - ingredient_two - ingredient_one):
                    for ingredient_four in range(1, total_teaspoons + 1 - ingredient_three - ingredient_two - ingredient_one):
                        ingredient_mix = [ingredient_one, ingredient_two, ingredient_three, ingredient_four]
                        if sum(ingredient_mix) != total_teaspoons:
                            continue
                        if self.calculate_calorie_count(ingredient_mix) == 500:
                            mix_value = self.calculate_mix_value(ingredient_mix)
                            if self.results < mix_value:
                                self.results = mix_value

    def calculate_calorie_count(self, ingredient_mix):
        calories = 0
        for count in range(0, len(ingredient_mix)):
            calories += self.all_ingredients[count].calories * ingredient_mix[count]

        return calories

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

        capacity_total = capacity_total if capacity_total > 0 else 0
        durability_total = durability_total if durability_total > 0 else 0
        flavor_total = flavor_total if flavor_total > 0 else 0
        texture_total = texture_total if texture_total > 0 else 0

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
print("Day 15 Part 2: {answer}".format(answer=adventDay15_2.answer_part2()))
