import io
import sys
import pypbe
import pbeSimDesign
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets

class PBEApp(QtWidgets.QMainWindow, pbeSimDesign.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) 
        # Build the rpg system options that are currently available
        self.comboSystem.addItem('pf')
        self.comboSystem.addItem('3e')
        self.comboSystem.addItem('4e')
        self.comboSystem.addItem('5e')
        # Build the button connections
        self.pushSim.clicked.connect(self.simulate_pbe)  
        self.pushAbout.clicked.connect(self.about) 
        # Set up the label to display the image
        self.image = QtWidgets.QLabel()
        self.plotLayout.addWidget(self.image)
        
    def simulate_pbe(self):
        # Obtain values from the spinners and inputs
        numDice = self.spinNumDice.value()
        diceType = self.spinDiceType.value()
        addVal = self.spinAddValue.value()
        numArr = self.spinNumArrays.value()
        numAtt = self.spinNumAttr.value()
        reRoll = self.spinReroll.value()
        numHist = self.spinBox.value()
        system = self.comboSystem.currentText()
        if self.checkKeepDice.isChecked():
            keepDice = self.spinKeepDice.value()
        else:
            keepDice = numDice
        if self.checkKeepAttr.isChecked():
            keepAtt = self.spinKeepAttrs.value()
        else:
            keepAtt = numAtt
        # Error Checking
        lowest_val = keepDice + addVal
        highest_val = (diceType * numDice) + addVal
        if keepDice > numDice:
            self.print_error("Number of dice to keep cannot be greater " + 
                             "than the number of dice.")
        elif keepAtt > numAtt:
            self.print_error("Number of attributes to keep cannot be greater" + 
                             " than the number of attributes.")      
        elif reRoll >= diceType:
            self.print_error("Number to re-roll must be less than the dice type.")
        elif lowest_val < 3:
            er_str = "The lowest possible value is " + str(lowest_val) + \
                     ". PBE is not defined for values less than 3. Please " + \
                     "increase the number of dice (or dice to keep) or the " + \
                     "add value."
            self.print_error(er_str)    
        elif highest_val > 18:
            er_str = "The highest possible value is " + str(highest_val) + \
                     ". PBE is not defined for values greater than 18. Please " + \
                     "decrease the number of dice (or dice to keep) or the " + \
                     "add value."
            self.print_error(er_str)        
        # If no errors found
        else:
            # Build a Point Buy Estimate
            pbe = pypbe.PBE(numDice, diceType, addVal, numAtt, numArr, reRoll, 
                            keepDice, keepAtt, system)
            f = pbe.roll_mc(numHist).plot_histogram(figsize=(9,7))
            # Display the figure using the QLabel
            buf = io.BytesIO()
            f.savefig(buf, format='png')
            buf.seek(0)
            im = Image.open(buf)
            imQt = ImageQt(im)
            pixmap = QtGui.QPixmap.fromImage(imQt)
            self.image.setPixmap(pixmap)
            self.image.show()
            # Display the raw results on a text line
            results = str(pbe.get_results())
            self.lineResults.setText(results)
    
    def print_error(self, err_string):
        QtWidgets.QMessageBox.about(self, "Error", err_string)
    
    def about(self):
        QtWidgets.QMessageBox.about(self, "About", """
Copyright 2017 Eric Strong. Refer to LICENSE for more information.

Project homepage: github.com/drericstrong/pypbe

PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to 
fairly select which random rolling method is closest to an equivalent Point Buy 
value. Ideally, all players will determine their character's stats exactly the 
same way. However, in some cases, players may ask for several different options 
for generating their character's stats. PyPBE is designed to allow GMs to make 
this decision in a fair way.""")

def main():
    app = QtWidgets.QApplication(sys.argv)  
    form = PBEApp()
    form.show()
    app.exec_()

if __name__ == '__main__':              
    main()