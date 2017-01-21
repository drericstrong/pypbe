[![PyPI version](https://badge.fury.io/py/pypbe.svg)](https://badge.fury.io/py/pypbe)

# PyPBE
### Python Point Buy Equivalence Calculator

**Description**: PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to fairly select which random rolling method is closest to an equivalent Point Buy value.

**Dependencies**: numpy, seaborn, bottleneck, matplotlib

Some GMs prefer to let their players choose between rolling for their ability scores and letting them use the Point Buy system. However, not all random rolling methods are created equal. Some (4d6, drop lowest) clearly give higher average results than others (3d6). PyPBE is designed to calculate and visualize the distribution of a specified ability score rolling method, which may provide useful information for decision-making.

PyPBE can be installed using pip:

> pip install pypbe

Working with PyPBE is very easy. Import the PBE class into your program, initializing it using the number and type of dice to roll, then use the "roll_mc" method to investigate the distribution. The results can be visualized using the "plot_histogram" method, and a data row summary can be generated using the "get_results" method. 

For example, running a simulation for three 6-sided dice (3d6), rolled for 6 attributes, can be accomplished using the following code:

> from pypbe import PBE

> alg = PBE(3,6)

> alg.roll_mc()

> alg.plot_histogram()

> results = alg.get_results()

The "roll_mc" and "plot_histogram" methods can be chained, like this:

> results = alg.roll_mc().plot_histogram().get_results()

More complicated scenarios can be run by adjusting the following user-specified parameters:

* **add_val**: The value to add to the dice roll. (i.e. this is the "8" in "1d10+8")
* **num_ability**: The number of ability scores to generate. Default is 6 ability scores.
* **num_arrays**: The number of ability scores arrays that can be chosen from. For instance, 2 arrays might allow the player to choose between [12,10,6,11,15,17] and [6,9,12,18,15,10]
* **reroll**: Allow dice re-rolling, cumulatively. "0" is no re-rolls, "1" is re-rolling 1s, and "2" is re-rolling 1s and 2s, and so on.
* **best_dice**: If you want to roll more dice than you need and then take the best N results. E.g. "Roll 4d6 and drop the lowest roll" would require a "3" here.
* **best_ability**: If you want to roll more abilities than you need and then take the best N results. E.g. "Roll 3d6 seven times, and take the best six times" would require a "6" here. Must be less than or equal to num_ability.
* **pbe_map**: This determines how much each ability score will "cost" in the Point Buy system. You supply a string here, and the default is Pathfinder. You can (currently) select Pathfinder: 'pf', D&D 3e: '3e', D&D 4e: '4e', or D&D 5e: '5e'

For instance, running a simulation for 2d6+6, with the best 6 out of 7 ability scores, rerolling 1s, and choosing from 3 arrays, should be initialized like this:

> alg = PBE(2, 6, add_val=6, num_ability=7, best_ability=6, reroll=1, num_arrays=3)

**Footnote**: You might also be concerned about the high variance inherent with every one of these methods and decide that you don't ever want random rolling in your game.
