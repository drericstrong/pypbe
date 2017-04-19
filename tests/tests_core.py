# -*- coding: utf-8 -*-
"""
    pypbe test_core
    ~~~~~~~~~~~~~~~~~~
    A set of unit tests for pypbe.

    :copyright: (c) 2017 Eric Strong.
    :license: Refer to LICENSE.txt for more information.
"""

import unittest
from pypbe.core import PBE

# These tests are for static methods in the main class, PBE
# More work needs to be done. I did some manual verification of the guts
# of _roll_array and _roll_arrays, but it might be worth separating these
# functions further into sub_functions for better testing.
class TestStaticPBE(unittest.TestCase):
    def test_findPBEMapping_default(self):
        test = PBE._find_pb_mapping('none')
        correct = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        self.assertEqual(test, correct)

    def test_findPBEMapping_known(self):
        test1 = PBE._find_pb_mapping('PF')
        correct1 = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        self.assertEqual(test1, correct1)
        test2 = PBE._find_pb_mapping('3e')
        correct2 = {3: -7, 4: -5, 5: -3, 6: -2, 7: -1, 8: 0, 9: 1, 10: 2,
                    11: 3, 12: 4, 13: 5, 14: 6, 15: 8, 16: 10, 17: 13, 18: 16}
        self.assertEqual(test2, correct2)
        test3 = PBE._find_pb_mapping('3.5e')
        self.assertEqual(test3, correct2)
        test4 = PBE._find_pb_mapping('5e')
        self.assertEqual(test4, correct2)
        test5 = PBE._find_pb_mapping('4e')
        correct5 = {3: -12, 4: -9, 5: -7, 6: -5, 7: -3, 8: -2, 9: -1, 10: 0,
                    11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 9, 17: 12, 18: 16}
        self.assertEqual(test5, correct5)

    # num_hist, num_dice, dice_type, add_val, num_ability, best_dice, reroll
    def test_rollArray_numHist_length(self):
        test = PBE._roll_array(100, 4, 6, 2, 6, 3, 0)
        test_size = len(test)
        correct = 100
        self.assertEqual(test_size, correct)

    # num_dice, dice_type, add_val, num_ability, best_ability, best_dice,
    # reroll, num_arrays)
    def test_constructTitle_normal(self):
        test = PBE._construct_title(3, 6, 0, 6, 6, 3, 0, 1)
        correct = "Sum 3d6, 6 Abilities"
        self.assertEqual(test, correct)

    def test_constructTitle_bestDice(self):
        test = PBE._construct_title(4, 6, 0, 6, 6, 3, 0, 1)
        correct = "Sum 4d6k3, 6 Abilities"
        self.assertEqual(test, correct)

    def test_constructTitle_add(self):
        test = PBE._construct_title(4, 6, 1, 6, 6, 3, 0, 1)
        correct = "Sum 4d6+1k3, 6 Abilities"
        self.assertEqual(test, correct)

    def test_constructTitle_extraAbility(self):
        test = PBE._construct_title(4, 6, 1, 7, 7, 3, 0, 1)
        correct = "Sum 4d6+1k3, 7 Abilities"
        self.assertEqual(test, correct)

    def test_constructTitle_bestAbility(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 0, 1)
        correct = "Sum 4d6+1k3, 7k6 Abilities"
        self.assertEqual(test, correct)

    def test_constructTitle_reroll1s(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 1, 1)
        correct = "Sum 4d6+1k3, 7k6 Abilities, Reroll 1s"
        self.assertEqual(test, correct)

    def test_constructTitle_reroll1s2s(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 2, 1)
        correct = "Sum 4d6+1k3, 7k6 Abilities, Reroll 1s/2s"
        self.assertEqual(test, correct)

    def test_constructTitle_arrays(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 2, 4)
        correct = "Sum 4d6+1k3, 7k6 Abilities, 4 Arrays, Reroll 1s/2s"
        self.assertEqual(test, correct)

if __name__ == '__main__':
    unittest.main()
