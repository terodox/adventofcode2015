from copy import deepcopy
from Day22 import *
from unittest import TestSuite, makeSuite, TextTestRunner, TestCase


class Day22UnitTests(TestCase):
    def setUp(self):
        self._sut = AdventDayTwentyTwo()

    def test_magic_missile(self):
        magic_missile = self.get_spell(self._sut.spells, 'Magic Missile')
        starting_hp = self._sut.boss.hit_points

        magic_missile.boss_effect(self._sut.boss)
        magic_missile.me_effect(self._sut.me, 0)

        self.assertEqual(starting_hp - 4, self._sut.boss.hit_points)

    def test_shield(self):
        shield = self.get_spell(self._sut.spells, 'Shield')
        starting_armor = self._sut.me.armor

        shield.me_effect(self._sut.me, timer=6)

        self.assertEqual(starting_armor + 7, self._sut.me.armor)

        shield.end_effect(self._sut.me)

        self.assertEqual(starting_armor, self._sut.me.armor)

    @staticmethod
    def get_spell(spells, spell_name):
        for spell in spells:
            if spell.name == spell_name:
                return spell

testSuite = TestSuite()
testSuite.addTest(makeSuite(Day22UnitTests))
runner = TextTestRunner(verbosity=2)
runner.run(testSuite)
