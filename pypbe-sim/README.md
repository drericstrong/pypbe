# PyPBE Simulator

![PyePBE](https://github.com/drericstrong/pypbe/blob/master/images/pypbe_small.jpg)

### Core Library

The core code repository of PyPBE is located [here](https://github.com/drericstrong/pypbe). Current documentation can be found [here](https://pypbe.readthedocs.io/en/latest/).

### Build Version

The torrent file for a compiled, Windows executable can be found in the base directory of this repository:

https://github.com/drericstrong/pypbe-sim/blob/master/pbeSimRun.torrent

**Warning**- if you're the type of person to download and run an executable from an unknown, random website, you need to take a long, hard look at your life and the various (bad) choices that have led you to this point. I cannot emphasize strongly enough that you should **not** directly download the executable from the above link. Instead, take a look at the following instructions for compiling it from source. If you can't get them to work, try searching for the answers yourself. Python is a very enjoyable language, and it may be good for your personal development to learn. In fact, you might find it fun.  

The maintainer apologizes that only a Windows executable is available in this section. However, if you are running another OS, the instructions below should allow you to compile a version that works for your specific OS. Check pyinstaller documentation for compatability with your OS:

http://www.pyinstaller.org/

### Compiling from Source

Unfortunately, this section does assume some knowledge of Python and programming in general. Also, I (obviously) do not personally support any of the software required for these steps, and so any major changes in the modules/libraries in this section may invalidate these instructions. These instructions were last updated May 2017.

First, install Python. Since PyPBE is written in Python, this is an absolutely necessary first step. I suggest version 3.5.3, since pyinstaller does not (currently) support 3.6. Instructions and binaries for Python 3.5.3 can be found here:

https://www.python.org/downloads/release/python-353/

Next, install the Qt framework. Qt is used for the PyPBE simulator graphical user interface. You should select the free, open-source version from this link:

https://info.qt.io/download-qt-for-application-development

Then, install the required Python modules. There's a requirements.txt file in the main directory of this repository. Download the pypbe-sim repository to your computer, navigate to the base directory (the one that "requirements.txt" is in) and then run the following command:

**pip install -r requirements.txt**

Finally, navigate to the "src" directory of the repository, and then run 3create.bat, which should contain the following line of code:

**pyinstaller pbeSimRun.py --onefile**

Once this is complete, your executable will appear in the "dist" folder of the repository!

### Python Point Buy Equivalence Calculator

*Sarah, John, and Kara sit down to play the first session of a new Pathfinder campaign with their GM, Lee. Sarah is excited about playing her favorite class, a Ranger. It doesn't matter what stats she rolls- she'll make it work. John is a bit of a min-maxer and wants to roll up a Wizard, so he's keen on getting the highest intelligence possible. Kara wants to play a Monk, which requires decent stats in a few different attributes.* 

*Lee decides that he wants the players to randomly roll for their character's stats. Sarah is excited about the chance for high stats. She's feeling especially lucky today. John, however, is angry. What if he doesn't roll any 18s for his intelligence? Kara is worried. She really wants to play a Monk, but she wants the character to be effective, and bad rolls could significantly reduce the fun she'll have playing the character.*

*What should Lee do?*

PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to fairly select which random rolling method is closest to an equivalent Point Buy value. Ideally, all players will determine their character's stats exactly the same way. However, in some cases (as in the story above), players may ask for several different options for generating their character's stats. PyPBE is designed to allow GMs to make this decision in a fair way.

As you work with PyPBE, you might also become concerned about the high variance inherent with every one of these methods and decide that you don't ever want random rolling in your game.

## Overview
Some GMs prefer to let their players choose between rolling for their ability scores and letting them use the Point Buy system. However, not all random rolling methods are created equal. Some (4d6, drop lowest) clearly give higher average results than others (3d6). PyPBE is designed to calculate and visualize the distribution of a specified ability score rolling method, which may provide useful information for decision-making.

The stats that PyPBE calculates aren't the "raw" values of the roll (e.g. typically 3 through 18), they're the "Point Buy Equivalent" of multiple rolls using that rolling method. For instance, if you roll 3d6 six times, you might get 10, 12, 8, 13, 7, 9, which has a Point Buy Equivalent of -2 (0+2-2+3-4-1) using the Pathfinder point buy scheme. 

PyPBE uses Monte Carlo simulation to obtain its results. If you perform the above process thousands/millions of times, you will get a distribution. The mean of that distribution is the fair Point Buy you should select for that rolling method, and 90% of the time, the random roll PBE will fall between the 5%/95% values. The "Typical Array" gives the most likely stat array using that random rolling method.

## Systems
PyPBE is designed for Pathfinder, 3e, 3.5e, 4e, and 5e characters. However, it allows the option to supply a custom Point Buy mapping, which means that it is applicable for any system in which the "Point Buy" concept applies. PyPBE also supports any number of attributes, although it was designed for the common 6-attribute system (strength, constitution, dexterity, intelligence, wisdom, charisma). As the number of attributes increase, note that the plots may become cluttered.