# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbeSim.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 10, 291, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spinKeepDice = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinKeepDice.setMinimum(1)
        self.spinKeepDice.setMaximum(10)
        self.spinKeepDice.setProperty("value", 3)
        self.spinKeepDice.setObjectName("spinKeepDice")
        self.gridLayout.addWidget(self.spinKeepDice, 5, 1, 1, 1)
        self.spinNumDice = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinNumDice.setMinimum(1)
        self.spinNumDice.setMaximum(10)
        self.spinNumDice.setProperty("value", 3)
        self.spinNumDice.setObjectName("spinNumDice")
        self.gridLayout.addWidget(self.spinNumDice, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.spinKeepAttrs = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinKeepAttrs.setMinimum(1)
        self.spinKeepAttrs.setMaximum(6)
        self.spinKeepAttrs.setProperty("value", 6)
        self.spinKeepAttrs.setObjectName("spinKeepAttrs")
        self.gridLayout.addWidget(self.spinKeepAttrs, 10, 1, 1, 1)
        self.comboSystem = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboSystem.setEditable(False)
        self.comboSystem.setCurrentText("")
        self.comboSystem.setMaxVisibleItems(4)
        self.comboSystem.setObjectName("comboSystem")
        self.gridLayout.addWidget(self.comboSystem, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.spinReroll = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinReroll.setMaximum(20)
        self.spinReroll.setObjectName("spinReroll")
        self.gridLayout.addWidget(self.spinReroll, 12, 1, 1, 1)
        self.spinNumArrays = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinNumArrays.setMinimum(1)
        self.spinNumArrays.setMaximum(20)
        self.spinNumArrays.setObjectName("spinNumArrays")
        self.gridLayout.addWidget(self.spinNumArrays, 13, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.spinDiceType = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinDiceType.setMinimum(2)
        self.spinDiceType.setMaximum(20)
        self.spinDiceType.setProperty("value", 6)
        self.spinDiceType.setObjectName("spinDiceType")
        self.gridLayout.addWidget(self.spinDiceType, 2, 1, 1, 1)
        self.spinAddValue = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinAddValue.setMinimum(-20)
        self.spinAddValue.setMaximum(20)
        self.spinAddValue.setObjectName("spinAddValue")
        self.gridLayout.addWidget(self.spinAddValue, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.checkKeepDice = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkKeepDice.setObjectName("checkKeepDice")
        self.gridLayout.addWidget(self.checkKeepDice, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.checkKeepAttr = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkKeepAttr.setObjectName("checkKeepAttr")
        self.gridLayout.addWidget(self.checkKeepAttr, 9, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.pushSim = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushSim.setObjectName("pushSim")
        self.gridLayout.addWidget(self.pushSim, 15, 1, 1, 1)
        self.spinNumAttr = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinNumAttr.setMinimum(1)
        self.spinNumAttr.setMaximum(6)
        self.spinNumAttr.setProperty("value", 6)
        self.spinNumAttr.setObjectName("spinNumAttr")
        self.gridLayout.addWidget(self.spinNumAttr, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 14, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(10000000)
        self.spinBox.setProperty("value", 100000)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 14, 1, 1, 1)
        self.pushAbout = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushAbout.setObjectName("pushAbout")
        self.gridLayout.addWidget(self.pushAbout, 15, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 10, 901, 651))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.plotLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.lineResults = QtWidgets.QLineEdit(self.centralwidget)
        self.lineResults.setGeometry(QtCore.QRect(310, 670, 811, 21))
        self.lineResults.setObjectName("lineResults")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPBE Simulator"))
        self.spinKeepDice.setToolTip(_translate("MainWindow", "Keep the best X dice (e.g. roll \"4d6\", keep \"3\")"))
        self.spinNumDice.setToolTip(_translate("MainWindow", "Total number of dice to roll (e.g. \"3\" in \"3d6\")"))
        self.label_3.setToolTip(_translate("MainWindow", "Add a constant value to the roll (e.g. \"2\" in \"4d4+2\")"))
        self.label_3.setText(_translate("MainWindow", "Add Value"))
        self.spinKeepAttrs.setToolTip(_translate("MainWindow", "Keep the best X attributes (e.g. \"6\" in \"roll 4d4+2 7 times, keep the best 6\")"))
        self.comboSystem.setToolTip(_translate("MainWindow", "Choose the rpg system for the point buy mapping"))
        self.label_5.setToolTip(_translate("MainWindow", "Number of dice arrays to choose from (e.g. \"3\" in \"roll 3d6 for 6 attributes, for 3 arrays\")"))
        self.label_5.setText(_translate("MainWindow", "Number of Arrays"))
        self.label_7.setToolTip(_translate("MainWindow", "Keep the best X dice (e.g. roll \"4d6\", keep \"3\")"))
        self.label_7.setText(_translate("MainWindow", "Keep Dice"))
        self.spinReroll.setToolTip(_translate("MainWindow", "Cumulatively reroll these dice values (e.g. 0 reroll nothing, 1 reroll 1s, 2 reroll 1s and 2s, etc.)"))
        self.spinNumArrays.setToolTip(_translate("MainWindow", "Number of dice arrays to choose from (e.g. \"3\" in \"roll 3d6 for 6 attributes, for 3 arrays\")"))
        self.label_2.setToolTip(_translate("MainWindow", "Number of sides on the dice (e.g. \"6\" in \"3d6\")"))
        self.label_2.setText(_translate("MainWindow", "Dice Type"))
        self.spinDiceType.setToolTip(_translate("MainWindow", "Number of sides on the dice (e.g. \"6\" in \"3d6\")"))
        self.spinAddValue.setToolTip(_translate("MainWindow", "Add a constant value to the roll (e.g. \"2\" in \"4d4+2\")"))
        self.label.setToolTip(_translate("MainWindow", "Total number of dice to roll (e.g. \"3\" in \"3d6\")"))
        self.label.setText(_translate("MainWindow", "Number of Dice"))
        self.checkKeepDice.setToolTip(_translate("MainWindow", "Must be checked if you want to keep less dice than you rolled"))
        self.checkKeepDice.setText(_translate("MainWindow", "Use Less Dice Than Rolled"))
        self.label_9.setToolTip(_translate("MainWindow", "Choose the rpg system for the point buy mapping"))
        self.label_9.setText(_translate("MainWindow", "System"))
        self.checkKeepAttr.setToolTip(_translate("MainWindow", "Must be checked if you want to keep less attributes than you rolled"))
        self.checkKeepAttr.setText(_translate("MainWindow", "Use Less Attributes Than Rolled"))
        self.label_6.setToolTip(_translate("MainWindow", "Cumulatively reroll these dice values (e.g. 0 reroll nothing, 1 reroll 1s, 2 reroll 1s and 2s, etc.)"))
        self.label_6.setText(_translate("MainWindow", "Reroll"))
        self.label_8.setToolTip(_translate("MainWindow", "Keep the best X attributes (e.g. \"6\" in \"roll 4d4+2 7 times, keep the best 6\")"))
        self.label_8.setText(_translate("MainWindow", "Keep Attributes"))
        self.label_4.setToolTip(_translate("MainWindow", "The total number of attributes to roll (e.g. STR, CON, DEX, INT, WIS, CHA)"))
        self.label_4.setText(_translate("MainWindow", "Number of Attributes"))
        self.pushSim.setText(_translate("MainWindow", "Simulate"))
        self.spinNumAttr.setToolTip(_translate("MainWindow", "The total number of attributes to roll (e.g. STR, CON, DEX, INT, WIS, CHA)"))
        self.label_10.setToolTip(_translate("MainWindow", "Monte Carlo histories to run (more is better, but slower)"))
        self.label_10.setText(_translate("MainWindow", "Number of Histories"))
        self.spinBox.setToolTip(_translate("MainWindow", "Monte Carlo histories to run (more is better, but slower)"))
        self.pushAbout.setText(_translate("MainWindow", "About"))

