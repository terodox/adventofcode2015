from copy import deepcopy
from Day22 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day22UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTwentyTwo()

    def test_magic_missile(self):
        magic_missile = self.get_spell(self._sut.spells, 'Magic Missile')
        starting_hp = self._sut.boss.hit_points

        magic_missile.boss_immediate_effect(self._sut.boss)

        self.assertEqual(starting_hp - 4, self._sut.boss.hit_points)

    def test_shield(self):
        shield = self.get_spell(self._sut.spells, 'Shield')
        starting_armor = self._sut.me.armor

        shield.me_immediate_effect(self._sut.me)

        self.assertEqual(starting_armor + 7, self._sut.me.armor)

        shield.end_effect(self._sut.me)

        self.assertEqual(starting_armor, self._sut.me.armor)

    def test_drain(self):
        drain = self.get_spell(self._sut.spells, 'Drain')
        me_starting_hp = self._sut.me.hit_points
        boss_starting_hp = self._sut.boss.hit_points

        drain.me_immediate_effect(self._sut.me)
        drain.boss_immediate_effect(self._sut.boss)

        self.assertEqual(me_starting_hp + 2, self._sut.me.hit_points)
        self.assertEqual(boss_starting_hp - 2, self._sut.boss.hit_points)

    def test_poison(self):
        poison = self.get_spell(self._sut.spells, 'Poison')
        boss_starting_hp = self._sut.boss.hit_points

        while poison.timer > 0:
            self._sut.apply_spell(self._sut.me, self._sut.boss, poison)

        self.assertEqual(boss_starting_hp - 18, self._sut.boss.hit_points)

    def test_recharge(self):
        recharge = self.get_spell(self._sut.spells, 'Recharge')
        me_starting_mana = self._sut.me.mana

        while recharge.timer > 0:
            self._sut.apply_spell(self._sut.me, self._sut.boss, recharge)

        self.assertEqual(me_starting_mana + 505, self._sut.me.mana)

    @staticmethod
    def get_spell(spells, spell_name):
        for spell in spells:
            if spell.name == spell_name:
                return spell

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day22UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
