from copy import deepcopy
from DataReader import AdventDay


class AdventDayTwentyTwo(AdventDay):
    def __init__(self):
        AdventDay.__init__(self, 22)

        self.boss = Character(
            name="Boss",
            hit_points=71,
            mana=0,
            armor=0,
            damage=10
        )

        self.me = Character(
            name="Terodox",
            hit_points=50,
            mana=500,
            armor=0,
            damage=0
        )

        self.spells = {
            'MagicMissile': MagicMissile(),
            'Drain': Drain(),
            'Shield': Shield(),
            'Poison': Poison(),
            'Recharge': Recharge()
        }
        self.part_one_min = 1000000000

    def answer_part1(self):
        self.run_all_scenarios(self.me, self.boss, {}, 0, 0)
        return self.part_one_min

    def set_part_one_min(self, maybe_min):
        if maybe_min < self.part_one_min:
            self.part_one_min = maybe_min
            print(maybe_min)

    def run_all_scenarios(self, passed_me, passed_boss, passed_active_spells, total_mana_spent, current_turn):
        if passed_me.hit_points <= 0:
            return
        elif passed_me.mana <= 0:
            return

        me = deepcopy(passed_me)
        boss = deepcopy(passed_boss)

        active_spells = self.cast_active_spells(passed_active_spells, me, boss)

        if boss.hit_points <= 0:
            self.set_part_one_min(total_mana_spent)
            return

        if current_turn % 2 == 0:
            # player turn
            me.hit_points -= 1
            if me.hit_points <= 0:
                return

            for spell_name, spell in self.spells.items():
                if spell_name in active_spells.keys():
                    continue
                new_spell = deepcopy(spell)
                new_me = deepcopy(me)
                new_boss = deepcopy(boss)

                new_spell.immediate_effect(new_me, new_boss)
                new_me.mana -= new_spell.mana_cost

                self.run_all_scenarios(
                    new_me,
                    new_boss,
                    {**active_spells, **{spell_name: new_spell}},
                    total_mana_spent + new_spell.mana_cost,
                    current_turn + 1)
        else:
            # boss turn
            me.hit_points -= boss.damage - me.armor if boss.damage - me.armor > 1 else 1
            self.run_all_scenarios(
                me,
                boss,
                active_spells,
                total_mana_spent,
                current_turn + 1)

    def cast_active_spells(self, active_spells, me, boss):
        still_active_spells = {}
        for spell_name, spell in active_spells.items():
            copied_spell = deepcopy(spell)
            copied_spell.timed_effect(me, boss)
            if copied_spell.timer > 0:
                still_active_spells[spell_name] = copied_spell
        return still_active_spells

class Character:
    def __init__(self, name, hit_points, mana, armor, damage):
        self.name = name
        self.hit_points = hit_points
        self.mana = mana
        self.armor = armor
        self.damage = damage

    def subtract_hit_points(self, how_many):
        if how_many <= 1:
            how_many = 1
        self.hit_points -= how_many

    def add_hit_points(self, how_many):
        self.hit_points += how_many

    def add_mana(self, how_much):
        self.mana += how_much

    def add_armor(self, how_much):
        self.armor += how_much

    def subtract_armor(self, how_much):
        self.armor -= how_much


class Spell:
    pass

class MagicMissile(Spell):
    def __init__(self):
        self.mana_cost = 53
        self.timer = 0

    def immediate_effect(self, me, boss):
        boss.hit_points -= 4

    def timed_effect(self, me, boss):
        pass

class Drain(Spell):
    def __init__(self):
        self.mana_cost = 73
        self.timer = 0

    def immediate_effect(self, me, boss):
        boss.hit_points -= 2
        me.hit_points += 2

    def timed_effect(self, me, boss):
        pass


class Shield(Spell):
    def __init__(self):
        self.mana_cost = 113
        self.timer = 6

    def immediate_effect(self, me, boss):
        me.armor += 7

    def timed_effect(self, me, boss):
        self.timer -= 1
        if self.timer == 0:
            me.armor -= 7


class Poison(Spell):
    def __init__(self):
        self.mana_cost = 173
        self.timer = 6

    def immediate_effect(self, me, boss):
        pass

    def timed_effect(self, me, boss):
        self.timer -= 1
        boss.hit_points -= 3


class Recharge(Spell):
    def __init__(self):
        self.mana_cost = 229
        self.timer = 5

    def immediate_effect(self, me, boss):
        pass

    def timed_effect(self, me, boss):
        self.timer -= 1
        me.mana += 101


adventDay22 = AdventDayTwentyTwo()
print("Day 22 Part 1: {answer}".format(answer=adventDay22.answer_part1()))
# print("Day 22 Part 2: {answer}".format(answer=adventDay22.answer_part2()))
