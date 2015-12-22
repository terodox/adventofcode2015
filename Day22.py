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
            Spell(
                'Magic Missile',
                mana_cost=53,
                boss_effect=lambda boss: boss.subtract_hit_points(4),
                me_effect=lambda me, timer: me,
                end_effect=lambda me: me,
                timer=0),
            Spell(
                'Drain',
                mana_cost=73,
                boss_effect=lambda boss: boss.subtract_hit_points(2),
                me_effect=lambda me, timer: me.add_hit_points(2),
                end_effect=lambda me: me,
                timer=0),
            Spell(
                'Shield',
                mana_cost=113,
                boss_effect=lambda boss: boss,
                me_effect=lambda me, timer: me.add_armor(7) if timer == 6 else me,
                end_effect=lambda me: me.subtract_armor(7),
                timer=6),
            Spell(
                'Poison',
                mana_cost=173,
                boss_effect=lambda boss: boss.subtract_hit_points(3),
                me_effect=lambda me, timer: me,
                end_effect=lambda me: me,
                timer=6),
            Spell(
                'Recharge',
                mana_cost=229,
                boss_effect=lambda boss: boss,
                me_effect=lambda me, timer: me.add_mana(101),
                end_effect=lambda me: me,
                timer=5)
        }


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
    def __init__(self, name, mana_cost, boss_effect, me_effect, end_effect, timer):
        self.name = name
        self.mana_cost = mana_cost
        self.boss_effect = boss_effect
        self.me_effect = me_effect
        self.end_effect = end_effect
        self.timer = timer

adventDay22 = AdventDayTwentyTwo()
# print("Day 22 Part 1: {answer}".format(answer=adventDay22.answer_part1()))
# print("Day 22 Part 2: {answer}".format(answer=adventDay22.answer_part2()))
