# -*- coding: utf-8 -*-
"""
    pypbe
    Python Point Buy Equivalent
    ~~~~~~~~~~~~~~~
    Intended for tabletop rpgs such as Pathfinder or D&D, this module contains
    code to run a Monte Carlo simulation to determine the Point Buy Equivalent
    (PBE) for a given type of ability score rolling method, such as "Roll 4d6
    and drop the lowest".

    :copyright: (c) 2017 Eric Strong.
    :license: Refer to LICENSE.txt for more information.
"""

import numpy as np
import seaborn as sns
import bottleneck as bn
import matplotlib.pyplot as plt
from numpy.random import randint


class PBE:
    """
    pypbe.PBE
    Point Buy Equivalent
    ~~~~~~~~~~~~~~~~~~~~
    Initializes a Monte Carlo simulation to determine the equivalent
    Point Buy of an ability score rolling method.
    """
    def __init__(self, num_dice, dice_type, add_val=0, num_ability=6,
                 num_arrays=1, reroll=0, best_dice=None, best_ability=6,
                 pbe_map='pf', custom_pbe_map=None):
        """
        pypbe.PBE
        Point Buy Equivalent
        ~~~~~~~~~~~~~~~~~~~~
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
        self.num_dice = num_dice
        self.dice_type = dice_type
        self.add_val = add_val
        self.num_ability = num_ability
        self.num_arrays = num_arrays
        self.reroll = reroll
        self.best_ability = best_ability
        if custom_pbe_map:
            self.pbe_map = custom_pbe_map
        else:
            self.pbe_map = self._find_pb_mapping(pbe_map)
        if best_dice:
            self.best_dice = best_dice
        else:
            self.best_dice = num_dice

    @staticmethod
    def _find_pb_mapping(map_string):
        # This function will find the point buy mapping for each roll
        # The following line is the default, for 3e, 4e, and Pathfinder
        vmap = {3: -16, 4: -12, 5: -9, 6: -6, 7: -4, 8: -2, 9: -1, 10: 0,
                11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
        # Now, go through and match the user string with all selections
        if map_string is "5e":
            vmap = {3: -7, 4: -5, 5: -3, 6: -2, 7: -1, 8: 0, 9: 1, 10: 2,
                    11: 3, 12: 4, 13: 5, 14: 6, 15: 8, 16: 10, 17: 13, 18: 16}
        return vmap

    @staticmethod
    def _roll_array(num_hist, num_dice, dice_type, add_val, num_ability,
                    best_dice, reroll):
        # This function will roll a single stat array, with a number of
        # rows equal to [num_hist] and columns equal to [num_ability]
        abilities = []
        # Rolls the full array containing [num_ability] Ability Scores
        for _ in range(num_ability):
            # Generate a matrix of random integers [num_hist] by [num_dice]
            attr = randint(reroll + 1, dice_type + 1,
                           size=(num_hist, num_dice))
            # Sorts and takes the top [best_dice] values. Partition sort is
            # quicker, but it only works for sorting the best N values
            if best_dice < num_dice:
                attr = bn.partsort(attr, best_dice, axis=1)[:, -best_dice:]
            # Sum the rolls together, and add the [add_val]
            result = np.add(attr.sum(axis=1), add_val)
            abilities.append(result)
            # Return the stacked ability array
        ability_array = np.column_stack(abilities)
        return ability_array

    @staticmethod
    def _roll_arrays(num_hist, num_dice, dice_type, add_val, num_ability,
                     best_dice, reroll, num_arrays, best_ability, vmap):
        # This function will roll multiple stat arrays, with dimensions:
        # raw_array = (num_arrays,num_hist,best_dice)
        # pbe_array = (num_hist,num_arrays)
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

    @staticmethod
    def _find_best_pbe(num_hist, num_dice, dice_type, add_val, num_ability,
                       best_dice, reroll, num_arrays, best_ability, vmap):
        # This function will roll multiple stat arrays and choose the one
        # with the highest PBE
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
        # Find the bin count of each value
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
        # The results are bundled together into results arrays
        arr_res = [bin_arr, mean_arr, std_arr, a5_arr, a95_arr]
        pbe_res = [bin_pbe, mean_pbe, std_pbe, a5_pbe, a95_pbe]
        return arr_res, pbe_res

    @staticmethod
    def _construct_title(num_dice, dice_type, add_val, num_ability,
                         best_ability, best_dice, reroll, num_arrays):
        # This function will construct an appropriate title for the
        # histogram using all the user-configured settings
        first = "Sum "
        high = ""
        if best_dice < num_dice:
            high = "the Best {} ".format(best_dice)
        dice = "of {}d{}".format(num_dice, dice_type)
        plus = ""
        if add_val > 0:
            plus = "+" + str(add_val)
        rerolls = ""
        if reroll > 0:
            rerolls = ", Reroll "
            for ii in range(0, reroll):
                rerolls += str(ii + 1) + "s/"
            rerolls = rerolls[:-1]
        best = ", "
        if best_ability < num_ability:
            best = ", Best {} of ".format(best_ability)
        repeat = "{} Rolls".format(num_ability)
        array_ = ""
        if num_arrays > 1:
            array_ = ", Best of {} Arrays".format(num_arrays)
        return "".join(
            [first, high, dice, plus, rerolls, best, repeat, array_])

    @staticmethod
    def _build_text(mean_arr, a5_arr, a95_arr):
        # This function will build the text box for the raw array, since we
        # need a new line for each roll
        ret_str = ""
        for ii in range(len(mean_arr)):
            app = 'Roll {}: {:.2f} [{:.0f},{:.0f}]\n'.format(
                str(ii + 1), mean_arr[ii], a5_arr[ii], a95_arr[ii])
            ret_str += app
        ret_str = ret_str[:-1]
        return ret_str

    @staticmethod
    def _plot_hist(arr_res, pbe_res, title, figsize):
        # This function will plot a histogram using the bins found
        # from the roll_mc() function. roll_mc() must be called first

        # Unpack the results for readability
        bin_arr, mean_arr, std_arr, a5_arr, a95_arr = arr_res
        bin_pbe, mean_pbe, std_pbe, a5_pbe, a95_pbe = pbe_res
        # Props is a dictionary for the text box with summary stats
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        # Divide into two subplots, stacked horizontally
        f, ((ax1), (ax2)) = plt.subplots(2, 1, figsize=figsize)

        # Plot each raw array, which is ordered from smallest to largest
        # The max val is global and needed to scale the legend appropriately
        maxval = 0
        for ii, roll in enumerate(bin_arr):
            ax1.plot(roll, label="Roll {}".format(ii + 1))
            maxval = max(maxval, max(roll))
        ax1.axis([1, 18, 0, 1.25 * maxval])
        # Plot the text box for the raw arrays, which contains the
        # mean and 90% values
        str1 = PBE._build_text(mean_arr, a5_arr, a95_arr)
        ax1.text(0.05, 0.75, str1, transform=ax1.transAxes, bbox=props,
                 fontsize=12, verticalalignment='top',
                 horizontalalignment='left')

        # Plot the Point Buy Equivalent distribution
        ax2.plot(bin_pbe[:, 0], bin_pbe[:, 1], label="PBE")
        maxval_pbe = 1.05 * max(bin_pbe[:, 1])
        ax2.fill_between(bin_pbe[:, 0], bin_pbe[:, 1])
        ax2.plot([mean_pbe, mean_pbe], [0, maxval_pbe], color='k',
                 ls='--', label="Mean")
        ax2.set_ylim([0, maxval_pbe])
        # Plot the 90% line
        five_ind = np.where(bin_pbe[:, 0] == a5_pbe)[0]
        five_prob = bin_pbe[five_ind, 1]
        ax2.plot([a5_pbe, a95_pbe], [five_prob, five_prob],
                 color='darkslategray',
                 ls=':', label="90%")
        # Plot the text box for the PBE, which contains the mean, std,
        # and 90% values
        str2 = '$\mu$= {:.1f}\n$\sigma$= {:.2f}\n5%= {:.0f}\n95%= {:.0f}'.format(
            mean_pbe, std_pbe, a5_pbe, a95_pbe)
        ax2.text(0.85, 0.90, str2, transform=ax2.transAxes, fontsize=12,
                 verticalalignment='top', bbox=props)

        # Labeling
        plt.suptitle(title, fontsize=14)
        ax1.legend(loc='upper center', ncol=len(bin_arr))
        ax1.set_ylabel('Raw Values Probability')
        ax2.legend(loc='upper left')
        ax2.set_ylabel('Point Buy Equivalent Probability')

    def roll_mc(self, num_hist=10**6):
        """
        Runs the initialized Monte Carlo simulation to determine the equivalent
        Point Buy of an ability score rolling method. NOTE- This method must
        be called BEFORE "plot_histogram".

        This method returns self, so you can stack the "plot_histogram" and
        "get_results" methods, like pbe1.roll_mc().plot_histogram()

        :param num_hist: Number of Monte Carlo histories to run. Suggest 10**6
        """
        # This is hard to read- just look at _find_best_pbe
        self.arr_res, self.pbe_res = self._find_best_pbe(num_hist,
            self.num_dice, self.dice_type, self.add_val, self.num_ability,
            self.best_dice, self.reroll, self.num_arrays, self.best_ability,
            self.pbe_map)
        return self

    def plot_histogram(self, title_prefix="", title_override="",
                       figsize=(10, 8)):
        """
        Plots a histogram of the results after the Monte Carlo simulation is
        run. NOTE- This method must be called AFTER "roll_mc".

        This method returns self, so you can stack the "get_results" method,
        like pbe1.roll_mc().plot_histogram().get_results()

        :param title_prefix: If desired, prefix the title (such as "Alg 1")
        :param title_override: Override the title string entirely
        :param figsize: The size of the histogram plot
        """
        # Find a title using either the override or _construct_title method
        if title_override:
            title = title_override
        else:
            title = title_prefix + PBE._construct_title(self.num_dice,
                self.dice_type, self.add_val, self.num_ability,
                self.best_ability, self.best_dice, self.reroll,
                self.num_arrays)
        # Construct the histogram
        self._plot_hist(self.arr_res, self.pbe_res, title, figsize)
        return self

    def get_results(self, title_prefix="", title_override="",
                    round_digits=2):
        """
        Constructs a summary of the results as an array, which might be
        useful for writing the results of multiple algorithms to a table.
        NOTE- This method must be called AFTER "roll_mc".

        :param title_prefix: If desired, prefix the title (such as "Alg 1")
        :param title_override: Override the title string entirely
        :param round_digits: the number of digits to round to
        :return: A tuple of the raw array results and PBE results, as:
                 [Description, Typical Array, Mean, Std, 5%, 95%]
        """
        # Find a title using either the override or _construct_title method
        if title_override:
            title = title_override
        else:
            title = title_prefix + PBE._construct_title(self.num_dice,
                self.dice_type, self.add_val, self.num_ability,
                self.best_ability, self.best_dice, self.reroll,
                self.num_arrays)
        # Unpack the results for readability
        bin_arr, mean_arr, std_arr, a5_arr, a95_arr = self.arr_res
        bin_pbe, mean_pbe, std_pbe, a5_pbe, a95_pbe = self.pbe_res
        # Find the typical array
        typ_arr = "; ".join([str(round(x, round_digits)) for x in mean_arr])
        res_row = [title, typ_arr, round(mean_pbe, round_digits),
                   round(std_pbe, round_digits), a5_pbe, a95_pbe]
        return res_row
