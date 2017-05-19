# -*- coding: utf-8 -*-
"""
    pypbe.core
    --------------
    Intended for tabletop rpgs such as Pathfinder or D&D, this module contains
    code to run a Monte Carlo simulation to determine the Point Buy Equivalent
    (PBE) for a given type of ability score rolling method, such as "Roll 4d6
    and drop the lowest".

    :copyright: (c) 2017 Eric Strong.
    :license: Refer to LICENSE.txt for more information.
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.random import randint


class PBE:
    """
    Initializes a Monte Carlo simulation to determine the equivalent
    Point Buy of an ability score rolling method.
    """
    def __init__(self, num_dice, dice_type, add_val=0, num_attribute=6,
                 num_arrays=1, reroll=0, keep_dice=None, keep_attribute=6,
                 pbe_map='pf', custom_pbe_map=None):
        """
        Initializes a Monte Carlo simulation to determine the equivalent
        Point Buy of an ability score rolling method.

        :param num_dice: num_dice- The number of dice to roll (i.e. this is
            the "3" in "3d6")
        :param dice_type: The type of dice to roll (i.e. six-sided,
            eight-sided, etc. This is the "6" in "3d6")
        :param add_val: The value to add to the dice roll. (i.e.
            this is the "8" in "1d10+8")
        :param num_ability: The number of ability scores to generate (e.g. 6)
        :param num_arrays: The number of ability scores arrays that can be
            chosen from. For instance, 2 arrays might allow the player to
            choose between [12,10,6,11,15,17] and [6,9,12,18,15,10]
        :param reroll: Allow dice re-rolling, cumulatively. "0" is no re-rolls,
            "1" is re-rolling 1s, and "2" is re-rolling 1s and 2s, and so on.
        :param best_dice: If you want to roll more dice than you need
            and then take the best N results. E.g. "Roll 4d6 and drop the
            lowest roll" would require a "3" here.
        :param best_ability: If you want to roll more abilities than you need
            and then take the best N results. E.g. "Roll 3d6 seven times,
            and take the best six times" would require a "6" here.
        :param pbe_map: This determines how much each ability score will
            "cost" in the Point Buy system. You supply a string here, and
            the default is Pathfinder. You can (currently) select Pathfinder:
            'pf', D&D 3e: '3e', D&D 4e: '4e', or D&D 5e: '5e'
        :param custom_pbe_map: If you want, you can supply a custom Point Buy
        """
        # Save the user-supplied properties
        self.num_dice = int(num_dice)
        self.dice_type = int(dice_type)
        self.add_val = int(add_val)
        self.num_attribute = int(num_attribute)
        self.num_arrays = int(num_arrays)
        self.reroll = int(reroll)
        self.keep_attribute = int(keep_attribute)
        # If a custom PBE map is supplied, use it; otherwise, find the
        # PBE mapping based on the user-supplied string
        pbe_map = str(pbe_map).lower()
        if custom_pbe_map:
            if type(custom_pbe_map) == dict:
                self.pbe_map = custom_pbe_map
            else:
                raise TypeError("Custom PBE map must be a dictionary.")
        else:
            if pbe_map == 'pf' or pbe_map == '3e' or pbe_map == '3.5e' or \
                            pbe_map == '4e' or pbe_map == '5e':
                self.pbe_map = self._find_pb_mapping(pbe_map)
            else:
                raise ValueError("PBE map string unrecognized.")
        # If keep dice wasn't supplied, it's equal to the number of dice
        # (i.e. we're keeping "all" the dice)
        if keep_dice:
            self.keep_dice = keep_dice
        else:
            self.keep_dice = num_dice
        # Check supplied user input for errors
        self._error_check()

    # This function will perform some basic error-checking on the user
    # input. For instance, the amount of dice to keep can't be greater
    # than the amount of dice we are actually rolling.
    def _error_check(self):
        if self.keep_dice > self.num_dice:
            raise ValueError("Number of dice to keep cannot be greater " +
                             "than the number of dice.")
        if self.keep_attribute > self.num_attribute:
            raise ValueError("Number of attributes to keep cannot be greater" +
                             " than the number of attributes.")
        if self.reroll >= self.dice_type:
            raise ValueError("Number to re-roll must be less than dice type.")
        # If the lowest possible value is below the lowest defined point buy,
        # PyPBE can't calculate it. Same for the highest value being above the
        # highest defined point buy.
        low_pos_val = self.keep_dice * 1 + self.add_val
        high_pos_val = (self.dice_type * self.keep_dice) + self.add_val
        low_def_val = min(self.pbe_map.keys())
        high_def_val = max(self.pbe_map.keys())
        if low_pos_val < low_def_val:
            raise ValueError("The lowest possible value is " +
                             str(low_pos_val) + ". PBE is not defined for " +
                             "values less than " + str(low_def_val) +
                             ". Please increase the number of dice (or " +
                             "dice to keep) or the add value.")
        elif high_pos_val > high_def_val:
            raise ValueError("The highest possible value is " +
                             str(high_pos_val) + ". PBE is not defined for " +
                             "values greater than " + str(high_def_val) +
                             ". Please decrease the number of dice (or " +
                             "dice to keep) or the add value.")

    # This function will find a point buy mapping (dictionary) based on the
    # user-supplied string
    @staticmethod
    def _find_pb_mapping(map_s):
        if map_s == "pf":  # default
            vmap = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                    11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        elif (map_s == "3e") | (map_s == "3.5e") | (map_s == "5e"):
            vmap = {3: -7, 4: -5, 5: -3, 6: -2, 7: -1, 8: 0, 9: 1, 10: 2,
                    11: 3, 12: 4, 13: 5, 14: 6, 15: 8, 16: 10, 17: 13, 18: 16}
        elif map_s == "4e":
            vmap = {3: -12, 4: -9, 5: -7, 6: -5, 7: -3, 8: -2, 9: -1, 10: 0,
                    11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 9, 17: 12, 18: 16}
        # I would rather this function fail noisily, even though this input
        # is checked during object initialization
        else:
            raise ValueError("PBE map string unrecognized. (2)")
        return vmap

    # This function will roll a single stat array, with a number of
    # rows equal to [num_hist] and columns equal to [num_ability]
    @staticmethod
    def _roll_array(num_hist, num_dice, dice_type, add_val, num_ability,
                    best_dice, reroll):
        abilities = []
        # Rolls the full array containing [num_ability] Ability Scores
        for _ in range(num_ability):
            # Generate a matrix of random integers [num_hist] by [num_dice]
            attr = randint(reroll + 1, dice_type + 1,
                           size=(num_hist, num_dice))
            # Sorts and takes the top [best_dice] values.
            if best_dice < num_dice:
                attr = np.sort(attr, axis=1)[:, -best_dice:]
            # Sum the rolls together, and add the [add_val]
            result = np.add(attr.sum(axis=1), add_val)
            abilities.append(result)
            # Return the stacked ability array
        ability_array = np.column_stack(abilities)
        return ability_array

    # This function will roll multiple stat arrays, with dimensions:
    # raw_array = (num_arrays,num_hist,best_dice)
    # pbe_array = (num_hist,num_arrays)
    @staticmethod
    def _roll_arrays(num_hist, num_dice, dice_type, add_val, num_ability,
                     best_dice, reroll, num_arrays, best_ability, vmap):
        arrays = []
        arrays_pbe = []
        # Iterates over the number of arrays
        for _ in range(num_arrays):
            array_ = PBE._roll_array(num_hist, num_dice, dice_type, add_val,
                                     num_ability, best_dice, reroll)
            # Sorts the array- we will need this to determine the distributions
            # of the top ability score, second ability score, and so on
            array_ = np.sort(array_)
            # Takes the top [best_ability] values
            if best_ability < num_ability:
                array_ = array_[:, -best_ability:]
            # Finds the total PBE of the array
            array_pbe = np.sum(np.vectorize(vmap.__getitem__)(array_), axis=1)
            # Add to the list of arrays
            arrays.append(array_)
            arrays_pbe.append(array_pbe)
        # Return the stacked arrays
        raw_arrays = np.array(arrays)
        pbe_arrays = np.column_stack(arrays_pbe)
        return raw_arrays, pbe_arrays

    # This function will roll multiple stat arrays and choose the one
    # with the highest PBE
    @staticmethod
    def _find_best_pbe(num_hist, num_dice, dice_type, add_val, num_ability,
                       best_dice, reroll, num_arrays, best_ability, vmap):
        raw_arrays, pbe_arrays = PBE._roll_arrays(num_hist, num_dice,
            dice_type, add_val, num_ability, best_dice, reroll, num_arrays,
            best_ability, vmap)
        # Find the index of the array with the best PBE
        shp = raw_arrays.shape
        y, x = np.ogrid[0:shp[1], 0:shp[2]]
        z = np.argmax(pbe_arrays, axis=1)
        zr = np.reshape(z, (-1, 1))
        # Select the array and PBE with the largest PBE, using the index above
        best_array = raw_arrays[zr, y, x]
        best_pbe = np.choose(z, pbe_arrays.T)
        # Find the bin count of each value.
        bin_arr = [np.bincount(best_array[:, i]) for i in range(best_ability)]
        bin_arr = [bin_arr[i] / sum(bin_arr[i]) for i in range(best_ability)]
        vals, counts = np.unique(best_pbe, return_counts=True)
        counts = counts / sum(counts)
        bin_pbe = np.array([[val, count] for val, count in zip(vals, counts)])
        # Summary statistics
        mean_arr = [np.mean(best_array[:, i])
                    for i in range(best_ability)]
        mean_pbe = np.mean(best_pbe)
        a5_arr = [int(np.percentile(best_array[:, i], 5))
                  for i in range(best_ability)]
        a5_pbe = int(np.percentile(best_pbe, 5))
        a95_arr = [int(np.percentile(best_array[:, i], 95))
                   for i in range(best_ability)]
        a95_pbe = int(np.percentile(best_pbe, 95))
        std_arr = [np.std(best_array[:, i])
                   for i in range(best_ability)]
        std_pbe = np.std(best_pbe)
        # The results are bundled together
        arr_res = {"raw_bins": bin_arr, "means": mean_arr, "stds": std_arr,
                   "5percentile": a5_arr, "95percentile": a95_arr}
        pbe_res = {"raw_bins": bin_pbe, "means": mean_pbe, "stds": std_pbe,
                   "5percentile": a5_pbe, "95percentile": a95_pbe}
        return arr_res, pbe_res

    # This function will construct a title for the plots, based on the
    # user-supplied input
    @staticmethod
    def _construct_title(num_dice, dice_type, add_val, num_ability,
                         best_ability, best_dice, reroll, num_arrays):
        # Construct part 1: "Sum AdB+CkD"
        dice_str = "Sum {}d{}".format(num_dice, dice_type)
        if add_val > 0:
            dice_str += "+{}".format(str(add_val))
        if best_dice < num_dice:
            dice_str += "k{}".format(str(best_dice))
        # Construct part 2: ", EkF Attrs"
        ability_str = ", {}".format(str(num_ability))
        if best_ability < num_ability:
            ability_str += "k{}".format(str(best_ability))
        ability_str += " Attrs"
        # Construct part 3: ", G Arrays"
        array_str = ""
        if num_arrays > 1:
            array_str += ", {} Arrays".format(str(num_arrays))
        # Construct part 4: ", Reroll Hs"
        rerolls_str = ""
        if reroll > 0:
            rerolls_str = ", Reroll "
            for ii in range(0, reroll):
                rerolls_str += str(ii + 1) + "s/"
            rerolls_str = rerolls_str[:-1]
        # Concatenate all four parts, and return the results
        ret = "".join([dice_str, ability_str, array_str, rerolls_str])
        return ret

    # This function will build the text box for the raw array plot, since we
    # need a new line for each roll
    @staticmethod
    def _build_text(mean_arr, a5_arr, a95_arr):
        ret_str = ""
        for ii in range(len(mean_arr)):
            app = 'Roll {}: {:.2f} [{:.0f},{:.0f}]\n'.format(
                str(ii + 1), mean_arr[ii], a5_arr[ii], a95_arr[ii])
            ret_str += app
        ret_str = ret_str[:-1]
        return ret_str

    # This function will plot a histogram using the bins found
    # from the roll_mc() function. roll_mc() must be called first
    @staticmethod
    def _plot_hist(arr_res, pbe_res, title, figsize):
        # Divide into two subplots, stacked horizontally
        # Props is a dictionary for the text box with summary stats
        f, ((ax1), (ax2)) = plt.subplots(2, 1, figsize=figsize)
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        # Plot each raw array, which is ordered from smallest to largest
        # The max val is global and needed to scale the legend appropriately
        maxval = 0
        for ii, roll in enumerate(arr_res["raw_bins"]):
            ax1.plot(roll, label="Roll {}".format(ii + 1))
            maxval = max(maxval, max(roll))
        ax1.axis([1, 18, 0, 1.25 * maxval])

        # Plot the text box for the raw arrays, which contains the
        # means, 5th percentile, and 95th percentile values
        str1 = PBE._build_text(arr_res["means"], arr_res["5percentile"],
                               arr_res["95percentile"])
        ax1.text(0.05, 0.75, str1, transform=ax1.transAxes, bbox=props,
                 fontsize=12, verticalalignment='top',
                 horizontalalignment='left')

        # Plot the Point Buy Equivalent distribution
        ax2.plot(pbe_res["raw_bins"][:, 0], pbe_res["raw_bins"][:, 1],
                 label="PBE")
        maxval_pbe = 1.05 * max(pbe_res["raw_bins"][:, 1])
        ax2.fill_between(pbe_res["raw_bins"][:, 0],
                         pbe_res["raw_bins"][:, 1])
        meanval = pbe_res["means"]
        ax2.plot([meanval, meanval], [0, maxval_pbe], color='k',
                 ls='--', label="Mean")
        ax2.set_ylim([0, maxval_pbe])
        # Plot the 90% line
        five_ind = np.where(pbe_res["raw_bins"][:, 0] == pbe_res["5percentile"])[0]
        five_prob = pbe_res["raw_bins"][five_ind, 1]
        ax2.plot([pbe_res["5percentile"], pbe_res["95percentile"]],
                 [five_prob, five_prob], color='darkslategray',
                 ls=':', label="90%")
        # Plot the text box for the PBE, which contains the mean, std,
        # and 90% values
        str2 = '$\mu$= {:.1f}\n$\sigma$= {:.2f}\n5%= {:.0f}\n95%= {:.0f}'.format(
            pbe_res["means"], pbe_res["stds"], pbe_res["5percentile"],
            pbe_res["95percentile"])
        ax2.text(0.85, 0.90, str2, transform=ax2.transAxes, fontsize=12,
                 verticalalignment='top', bbox=props)

        # Labeling
        plt.suptitle(title, fontsize=14)
        ax1.legend(loc='upper center', ncol=len(arr_res["raw_bins"]))
        ax1.set_ylabel('Raw Values Probability')
        ax2.legend(loc='upper left')
        ax2.set_ylabel('Point Buy Equivalent Probability')
        return f

    def roll_mc(self, num_hist=10**5):
        """
        Runs the initialized Monte Carlo simulation to determine the equivalent
        Point Buy of an ability score rolling method. NOTE- This method must
        be called BEFORE "plot_histogram".

        This method returns self, so you can stack the "plot_histogram" and
        "get_results" methods, like pbe1.roll_mc().plot_histogram()

        :param num_hist: Number of Monte Carlo histories to run. Suggest 10**5
        """
        # This is hard to read. I wanted to keep the underlying functions
        # static, so this is essentially just a wrapper around _find_best_pbe.
        self.arr_res, self.pbe_res = self._find_best_pbe(num_hist,
            self.num_dice, self.dice_type, self.add_val, self.num_attribute,
            self.keep_dice, self.reroll, self.num_arrays, self.keep_attribute,
            self.pbe_map)
        return self

    def plot_histogram(self, title_prefix="", title_override="",
                       figsize=(8, 6)):
        """
        Plots a histogram of the results after the Monte Carlo simulation is
        run. NOTE- This method must be called AFTER "roll_mc".

        :param title_prefix: If desired, prefix the title (such as "Alg 1")
        :param title_override: Override the title string entirely
        :param figsize: The size of the histogram plot
        :return: a seaborn figure of the histogram
        """
        # Check that roll_mc has been called
        if not self.arr_res:
            raise ValueError("Call roll_mc before plotting the histogram.")
        # Find a title using either the override or _construct_title method
        if title_override:
            title = title_override
        else:
            title = title_prefix + PBE._construct_title(self.num_dice,
                self.dice_type, self.add_val, self.num_attribute,
                self.keep_attribute, self.keep_dice, self.reroll,
                self.num_arrays)
        # Construct the histogram
        f = self._plot_hist(self.arr_res, self.pbe_res, title, figsize)
        return f

    def get_results(self, title_prefix="", title_override="", rnd_dig=2):
        """
        Constructs a summary of the results as an array, which might be
        useful for writing the results of multiple algorithms to a table.
        NOTE- This method must be called AFTER "roll_mc".

        :param title_prefix: If desired, prefix the title (such as "Alg 1 ")
        :param title_override: Override the title string entirely
        :param rnd_dig: the number of digits to round to
        :return: A tuple of the raw array results and PBE results, as:
                 [Description, Typical Array, Mean, Std, 5%, 95%]
        """
        # Check that roll_mc has been called
        if not self.arr_res:
            raise ValueError("Call roll_mc before getting results.")
        # Find a title using either the override or _construct_title method
        if title_override:
            title = title_override
        else:
            ctitle = PBE._construct_title(self.num_dice, self.dice_type,
                        self.add_val, self.num_attribute, self.keep_attribute,
                        self.keep_dice, self.reroll, self.num_arrays)
            title = title_prefix + ctitle
        # Find the typical array
        typ_arr = "; ".join([str(round(x, rnd_dig))
                             for x in self.arr_res["means"]])
        res_row = [title, typ_arr,
                   round(self.pbe_res["means"], rnd_dig),
                   round(self.pbe_res["stds"], rnd_dig),
                   round(self.pbe_res["5percentile"], rnd_dig),
                   round(self.pbe_res["95percentile"], rnd_dig)]
        return res_row
