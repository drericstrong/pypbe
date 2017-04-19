==========================
 4. Online Notebook
==========================
The PBE Online Notebook allows the user to run PyPBE interactively in a Jupyter notebook on GitHub. Navigate to this link and follow the instructions in the notebook:

https://github.com/drericstrong/pypbe/pbe_notebook/PBENotebook.ipynb

Running the notebook interactively requires you to install Python 3, the latest version of which can be found here:

https://www.python.org/downloads/

Once Python 3 is installed, the following Python modules are also required:

* numpy
* matplotlib
* seaborn
* pypbe

The "install.bat" file in that base directory can be used to install these modules automatically using pip (assuming that you are on Windows). Just double-click on the batch file to run it.

Otherwise, you can install these modules by opening a command terminal and typing:

**pip install MODULE**

for each of the four MODULEs above.

After those steps are complete, run the code in the notebook by clicking the green arrow at the top, and a series of sliders and a button should appear, which allows you to investigate the results from any random character attribute rolling method you desire. 

The plots will keep generating every time you click the button (so you can compare results), but you can re-run the cell using the green arrow in order to clear the current plots.