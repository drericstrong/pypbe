=============================
 7. PyPBE Simulator
=============================
**This executable was developed using an older version of PyPBE and may not work correctly at the current time.**

The torrent file for a compiled, Windows executable can be found in the base directory of this repository:

https://github.com/drericstrong/pypbe/blob/master/pypbe-sim/pbeSimRun.torrent

**Warning**- if you're the type of person to download and run an executable from an unknown, random website, you need to take a long, hard look at your life and the various (bad) choices that have led you to this point. I cannot emphasize strongly enough that you should **not** directly download the executable from the above link. Instead, take a look at the following instructions for compiling it from source. If you can't get them to work, try searching for the answers yourself. Python is a very enjoyable language, and it may be good for your personal development to learn. In fact, you might find it fun.  

The maintainer apologizes that only a Windows executable is available in this section. However, if you are running another OS, the instructions below should allow you to compile a version that works for your specific OS. Check pyinstaller documentation for compatability with your OS:

http://www.pyinstaller.org/

Compiling from Source
-----------------------

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