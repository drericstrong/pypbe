====================
 2. Getting Started
====================

Installation
--------------
If Python is already installed on your computer, PyPBE can be installed using 
PyPI by opening a command window and typing:

**pip install pypbe**

Upgrading to a new version of pyedna can be accomplished by:

**pip install pypbe --upgrade**

The source code of pyedna is hosted on GitHub at:

https://github.com/drericstrong/pypbe

Python Requirements
--------------------
**Required libraries**: numpy, seaborn, matplotlib

A requirements.txt document is located in the GitHub repository, and all 
package requirements can be installed using the following line in a
command window:

**pip install -r requirements.txt**

Numpy is required for the random arrays, and seaborn/matplotlib are required
to visualize the histograms. It is very unlikely that these requirements will 
change in the future.

Python Version Support
------------------------
Currently, PyPBE only supports Python 3.2+ and is not fully compatible with
Python 2. If this is important to you, please make a pull request at:

https://github.com/drericstrong/pypbe

The package maintainer welcomes collaboration.

Importing PyPBE
-----------------
The main class in PyPBE is usually imported into a script using the following line:

**from pypbe import PBE**