==========================
 4. Jupyter Notebook
==========================
The PBE Jupyter Notebook allows the user to run PyPBE interactively in a Jupyter notebook. Navigate to this link and follow the instructions in the notebook:

https://github.com/drericstrong/pypbe/blob/master/pbe_notebook/PBENotebook.ipynb

Running this notebook interactively requires you to install Python 3, the latest version of which can be found here:

https://www.python.org/downloads/

Alternatively, if you're having trouble getting these instructions to work, you may want to download the scientific Anaconda package (preferred, but larger size):

https://www.continuum.io/downloads

Once Python 3 is installed, the following Python modules are also required:

* ipywidgets
* jupyter
* numpy
* matplotlib
* seaborn
* pypbe

The "install.bat" file in this base directory can be used to install these modules automatically using pip (assuming that you are on Windows). Just double-click on the batch file to run it. If you installed Anaconda, most of these are available by default. Otherwise, you can install these modules by opening a command terminal and typing (for each of the six MODULEs above):

**pip install MODULE**

After those steps are complete, download this notebook to your computer. You can run a Jupyter notebook by typing:

**jupyter notebook**

in a command terminal, or if you installed Anaconda, open the "Anaconda Navigator" program and click on the "Jupyter" icon. Once the Jupyter notebook interface is open (it should appear in a web browser), navigate to where you downloaded this file, and click on it.

Run the following code by clicking the next "code" cell, then clicking the green arrow ("run") above, and a series of sliders and a button should appear, which allows you to investigate the results from any random character attribute rolling method you desire. 

The plots will keep generating every time you click the button (so you can compare results), but you can re-run the cell using the green arrow in order to clear the current plots.