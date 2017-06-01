.. PyPBE documentation master file, created by
   sphinx-quickstart on Tue Apr 18 13:16:55 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyePBE
==================================

.. image:: https://github.com/drericstrong/pypbe/blob/master/images/pypbe_small.jpg?raw=true

*Sarah, John, and Kara sit down to play the first session of a new Pathfinder campaign with their GM, Lee. Sarah is excited about playing her favorite class, a Ranger. It doesn't matter what stats she rolls- she'll make it work. John is a bit of a min-maxer and wants to roll up a Wizard, so he's keen on getting the highest intelligence possible. Kara wants to play a Monk, which requires decent stats in a few different attributes.* 

*Lee decides that he wants the players to randomly roll for their character's stats. Sarah is excited about the chance for high stats. She's feeling especially lucky today. John, however, is angry. What if he doesn't roll any 18s for his intelligence? Kara is worried. She really wants to play a Monk, but she wants the character to be effective, and bad rolls could significantly reduce the fun she'll have playing the character.*

*What should Lee do?*

PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to fairly select which random rolling method is closest to an equivalent Point Buy value. Ideally, all players will determine their character's stats exactly the same way. However, in some cases (as in the story above), players may ask for several different options for generating their character's stats. But not all random rolling methods are created equal. Some (4d6, drop lowest) clearly give higher average results than others (3d6). PyPBE is designed to allow GMs to make this decision in a fair way.

The stats that PyPBE calculates aren't the "raw" values of the roll (e.g. typically 3 through 18), they're the "Point Buy Equivalent" of multiple rolls using that stat-rolling method. For instance, if you roll 3d6 six times, you might get 10, 12, 8, 13, 7, 9, which has a Point Buy Equivalent of -2 (0+2-2+3-4-1) using the Pathfinder point buy scheme. PyPBE uses Monte Carlo simulation to obtain its results. If you perform the above process thousands/millions of times, you will get a distribution. The mean of that distribution is the fair Point Buy you should select for that rolling method. 90% of the time, the random roll PBE will fall between the 5%/95% values, which gives you an idea of the potential spread of the results. The "Typical Array" gives the most likely stat array using that random rolling method.

PyPBE is designed for Pathfinder, 3e, 3.5e, 4e, and 5e characters. However, the Python API allows the option to supply a custom Point Buy mapping, which means that it is applicable for any system in which the "Point Buy" concept applies. PyPBE also supports any number of attributes, although it was designed for the common 6-attribute system (strength, constitution, dexterity, intelligence, wisdom, charisma).

.. toctree::
   :maxdepth: 2

   introduction
   gettingstarted
   pythonapi   
   notebook  
   bokehserver
   gui
   changelog
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
