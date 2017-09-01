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


# These tests are for the user-supplied inputs during PBE object construction
class TestPBEInput(unittest.TestCase):
    def test_numdice_string_input(self):
        with self.assertRaises(ValueError):
            PBE("wrong", 6)

    def test_uppercase_PBEmap(self):
        pbe = PBE(3, 6, pbe_map="PF")
        correct = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                   11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        self.assertEqual(pbe.pbe_map, correct)

    def test_pbemap_int_input(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, pbe_map=4)

    def test_custompbemap_int_input(self):
        with self.assertRaises(TypeError):
            PBE(3, 6, custom_pbe_map=4)

    def test_keepdice_greater_numdice(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, keep_dice=4)

    def test_keepatt_greater_numatt(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, num_attribute=6, keep_attribute=7)

    def test_rerolls_greater_dicetype(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, reroll=6)

    def test_lowval_default(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, add_val=-1)
        with self.assertRaises(ValueError):
            PBE(2, 6)
        with self.assertRaises(ValueError):
            PBE(5, 6, keep_dice=2)
        with self.assertRaises(ValueError):
            PBE(5, 6, keep_dice=3, add_val=-1)

    def test_highval_default(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, add_val=1)
        with self.assertRaises(ValueError):
            PBE(4, 6)
        with self.assertRaises(ValueError):
            PBE(5, 6, keep_dice=4)
        with self.assertRaises(ValueError):
            PBE(5, 6, keep_dice=3, add_val=1)
    
    def test_lowval_highrolllimit(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, roll_high_limit = 2)
        with self.assertRaises(ValueError):
            PBE(2, 6, add_val=2, roll_high_limit=3)
    
    def test_highval_lowrolllimit(self):
        with self.assertRaises(ValueError):
            PBE(3, 6, roll_low_limit = 19)
        with self.assertRaises(ValueError):
            PBE(2, 6, add_val=1, roll_low_limit=14)
    

# These tests are for static methods in the main class, PBE
# More work needs to be done. I did some manual verification of the guts
# of _roll_array and _roll_arrays, but it might be worth separating these
# functions further into sub_functions for better testing.
class TestStaticPBE(unittest.TestCase):
    def test_findPBEMapping_default(self):
        test = PBE._find_pb_mapping('pf')
        correct = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        self.assertEqual(test, correct)

    def test_findPBEMapping_known(self):
        test1 = PBE._find_pb_mapping('pf')
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
        test = PBE._roll_array(100, 4, 6, 2, 6, 3, 0, None, None)
        test_size = len(test)
        correct = 100
        self.assertEqual(test_size, correct)

    # num_dice, dice_type, add_val, num_ability, best_ability, best_dice,
    # reroll, num_arrays)
    def test_constructTitle_normal(self):
        test = PBE._construct_title(3, 6, 0, 6, 6, 3, 0, 1)
        correct = "Sum 3d6, 6 Attrs"
        self.assertEqual(test, correct)

    def test_constructTitle_bestDice(self):
        test = PBE._construct_title(4, 6, 0, 6, 6, 3, 0, 1)
        correct = "Sum 4d6k3, 6 Attrs"
        self.assertEqual(test, correct)

    def test_constructTitle_add(self):
        test = PBE._construct_title(4, 6, 1, 6, 6, 3, 0, 1)
        correct = "Sum 4d6+1k3, 6 Attrs"
        self.assertEqual(test, correct)

    def test_constructTitle_extraAbility(self):
        test = PBE._construct_title(4, 6, 1, 7, 7, 3, 0, 1)
        correct = "Sum 4d6+1k3, 7 Attrs"
        self.assertEqual(test, correct)

    def test_constructTitle_bestAbility(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 0, 1)
        correct = "Sum 4d6+1k3, 7k6 Attrs"
        self.assertEqual(test, correct)

    def test_constructTitle_reroll1s(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 1, 1)
        correct = "Sum 4d6+1k3, 7k6 Attrs, Reroll 1s"
        self.assertEqual(test, correct)

    def test_constructTitle_reroll1s2s(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 2, 1)
        correct = "Sum 4d6+1k3, 7k6 Attrs, Reroll 1s/2s"
        self.assertEqual(test, correct)

    def test_constructTitle_arrays(self):
        test = PBE._construct_title(4, 6, 1, 7, 6, 3, 2, 4)
        correct = "Sum 4d6+1k3, 7k6 Attrs, 4 Arrays, Reroll 1s/2s"
        self.assertEqual(test, correct)


# These test methods actually instantiate a PBE class for various test cases.
# Unfortunately, since Monte Carlo simulation is stochastic, the same exact
# result isn't returned every time, which is awful for unit testing. This
# means that these tests have a (small) possibility of failing, even though
# I'm only checking the approximate output. These are also slow.
class TestCasesPBE(unittest.TestCase):
    def test_3d6(self):
        pbe = PBE(3, 6)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [6.8, 8.5, 9.9, 11.1, 12.5, 14.2]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 3.0
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_rolllowlimit(self):
        pbe = PBE(3, 6, roll_low_limit=7)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [8.1, 9.2, 10.4, 11.5, 12.7, 14.4]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 8.4
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_rollhighlimit(self):
        pbe = PBE(3, 6, roll_high_limit=14)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [6.6, 8.3, 9.5, 10.7, 11.8, 12.9]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = -2.4
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_pbelowlimit(self):
        pbe = PBE(3, 6, pbe_low_limit=5)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [7.8, 9.6, 10.9, 12.1, 13.5, 15.3]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 12.7
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_pbehighlimit(self):
        pbe = PBE(3, 6, pbe_high_limit=10)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [6.3, 8.1, 9.4, 10.6, 11.9, 13.7]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = -1.5
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_best3arrays(self):
        pbe = PBE(3, 6, num_arrays=3)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [7.8, 9.5, 10.85, 12.1, 13.5, 15.3]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 12.3
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_best3arrays_reroll1s(self):
        pbe = PBE(3, 6, num_arrays=3, reroll=1)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [9.6, 11.1, 12.3, 13.4, 14.5, 16.0]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 23.8
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_3d6_best6of7rolls(self):
        pbe = PBE(3, 6, num_attribute=7, keep_attribute=6)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [8.2, 9.4, 10.5, 11.6, 12.8, 14.5]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 9.1
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_4d6k3(self):
        pbe = PBE(4, 6, keep_dice=3)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [8.5, 10.4, 11.8, 13.0, 14.2, 15.7]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 18.85
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_4d6k3_best6of7rolls(self):
        pbe = PBE(4, 6, keep_dice=3, num_attribute=7, keep_attribute=6)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [10.1, 11.3, 12.4, 13.4, 14.5, 15.9]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 24.45
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_2d6p6(self):
        pbe = PBE(2, 6, add_val=6)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [10.0, 11.4, 12.5, 13.5, 14.6, 16.0]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 25.7
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

    def test_4d4p6k3_best6of7rolls(self):
        pbe = PBE(4, 4, add_val=6, keep_dice=3,
                  num_attribute=7, keep_attribute=6)
        pbe.roll_mc(int(10**6))
        ar = pbe.arr_res
        pb = pbe.pbe_res
        correct_means_raw = [13.2, 14.0, 14.7, 15.4, 16.1, 17.0]
        for ii, jj in zip(correct_means_raw, ar["means"]):
            self.assertAlmostEqual(ii, jj, places=1)
        correct_mean_pbe = 47.4
        self.assertAlmostEqual(correct_mean_pbe, pb["means"], places=1)

if __name__ == '__main__':
    unittest.main()
