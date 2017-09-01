====================
 1. Introduction
====================
PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to fairly select which random rolling method is closest to an equivalent Point Buy value.

Overview
---------
Some GMs prefer to let their players choose between rolling for their ability scores and letting them use the Point Buy system. However, not all random rolling methods are created equal. Some (4d6, drop lowest) clearly give higher average results than others (3d6). PyPBE is designed to calculate and visualize the distribution of a specified ability score rolling method, which may provide useful information for decision-making.

The stats that PyPBE calculates aren't the "raw" values of the roll (e.g. typically 3 through 18), they're the "Point Buy Equivalent" of 6 rolls using that rolling method. For instance, if you roll 3d6 six times, you might get 10, 12, 8, 13, 7, 9, which has a Point Buy Equivalent of -2 (0+2-2+3-4-1) using the Pathfinder point buy scheme. 

PyPBE uses Monte Carlo simulation to obtain its results. If you perform the above process thousands/millions of times, you will get a distribution. The mean of that distribution is the fair Point Buy you should select for that rolling method, and 90% of the time, the random roll PBE will fall between the 5%/95% values. The "Typical Array" gives the most likely stat array using that random rolling method.

Package Organization
----------------------
PyPBE is organized into a single namespace, called "core". The "PBE" class inside the core namespace is used to simulate a single rolling method (such as the sum of 3d6 for 6 attributes), plot a histogram of the results, and save the results to an array.

For those who wish to contribute or dig deeper into the code, the following folders in the GitHub repository may be of interest:

* pypbe: contains the core functionality of PyPBE
* pypbe-bk: a Bokeh server for visualizing the results from running PyPBE, with a Procfile for running on Heroku
* pypbe-nb: an (older) Jupyter notebook with a basic GUI that shows off some of the functionality of PyPBE
* pypbe-rec: a Bokeh server for recommending a dice rolling method based on a selected point buy (think of this as the inverse of pypbe-bk)
* pypbe-sim: an (older) Windows executable for running PyPBE locally without Python
* tests: a set of unit tests for the core functionality (needs some work)

Systems
--------
PyPBE is designed for Pathfinder, 3.5e, and 5e characters. However, it allows the option to supply a custom Point Buy mapping, which means that it is applicable for any system in which the "Point Buy" concept applies. PyPBE also supports any number of attributes, although it was designed for the common 6-attribute system (strength, constitution, dexterity, intelligence, wisdom, charisma).

