import sys
import numpy as np
from PySide2 import QtCore, QtGui, QtWidgets
from plxscripting.easy import * 


class Ui_MainWindow(object):
    """ graphical user interface """    

    def setupUi(self, MainWindow):
        self.g_i = g_i
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 520)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Select_Line_QText_Edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Select_Line_QText_Edit.setEnabled(True)
        self.Select_Line_QText_Edit.setGeometry(QtCore.QRect(30, 30, 141, 21))
        self.Select_Line_QText_Edit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Select_Line_QText_Edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Select_Line_QText_Edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Select_Line_QText_Edit.setReadOnly(True)
        self.Select_Line_QText_Edit.setOverwriteMode(False)
        self.Select_Line_QText_Edit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Select_Line_QText_Edit.setObjectName("Select_Line_QText_Edit")

        self.Min_Line_Length_QLine_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Min_Line_Length_QLine_Edit.setGeometry(QtCore.QRect(190, 60, 101, 20))
        self.Min_Line_Length_QLine_Edit.setText("")
        self.Min_Line_Length_QLine_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Min_Line_Length_QLine_Edit.setObjectName("Min_Line_Length_QLine_Edit")
        self.Min_Line_Length_QText_Edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Min_Line_Length_QText_Edit.setGeometry(QtCore.QRect(190, 30, 101, 21))
        self.Min_Line_Length_QText_Edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Min_Line_Length_QText_Edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Min_Line_Length_QText_Edit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Min_Line_Length_QText_Edit.setObjectName("Min_Line_Length_QText_Edit")

        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setGeometry(QtCore.QRect(230, 100, 111, 31))
        self.Run.setObjectName("Run")
        self.Run.clicked.connect(self.run)

        self.g_i.gotostructures() 
        self.Lines_QComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Lines_QComboBox.setGeometry(QtCore.QRect(30, 60, 141, 20))
        self.Lines_QComboBox.setAccessibleName("")
        self.Lines_QComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Lines_QComboBox.setEditable(False)
        self.Lines_QComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.Lines_QComboBox.setMinimumContentsLength(0)
        self.Lines_QComboBox.setObjectName("Lines_QComboBox")
        self.Lines_QComboBox.addItems([i.Name.value for i in self.g_i.Lines[:]])

        self.Max_Line_Length_QText_Edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Max_Line_Length_QText_Edit.setGeometry(QtCore.QRect(310, 30, 101, 21))
        self.Max_Line_Length_QText_Edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Max_Line_Length_QText_Edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Max_Line_Length_QText_Edit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Max_Line_Length_QText_Edit.setObjectName("Max_Line_Length_QText_Edit")

        self.Max_Line_Length_QLine_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Max_Line_Length_QLine_Edit.setGeometry(QtCore.QRect(310, 60, 101, 20))
        self.Max_Line_Length_QLine_Edit.setText("")
        self.Max_Line_Length_QLine_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Max_Line_Length_QLine_Edit.setObjectName("Max_Line_Length_QLine_Edit")

        self.Increment_QText_Edit = QtWidgets.QTextEdit(self.centralwidget)
        self.Increment_QText_Edit.setGeometry(QtCore.QRect(430, 30, 101, 21))
        self.Increment_QText_Edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Increment_QText_Edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Increment_QText_Edit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Increment_QText_Edit.setObjectName("Increment_QText_Edit")

        self.Increment_QLine_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Increment_QLine_Edit.setGeometry(QtCore.QRect(430, 60, 101, 20))
        self.Increment_QLine_Edit.setText("")
        self.Increment_QLine_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.Increment_QLine_Edit.setObjectName("Increment_QLine_Edit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.listwidget.setGeometry(QtCore.QRect(30, 150, 500, 300))
        self.listwidget.setObjectName("listView")
        self.listwidget.addItems(["Factor of Safety"])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Lines_QComboBox, self.Min_Line_Length_QLine_Edit)
        MainWindow.setTabOrder(self.Min_Line_Length_QLine_Edit, self.Max_Line_Length_QLine_Edit)
        MainWindow.setTabOrder(self.Max_Line_Length_QLine_Edit, self.Increment_QLine_Edit)
        MainWindow.setTabOrder(self.Increment_QLine_Edit, self.Run)
        MainWindow.setTabOrder(self.Run, self.Select_Line_QText_Edit)
        MainWindow.setTabOrder(self.Select_Line_QText_Edit, self.Min_Line_Length_QText_Edit)
        MainWindow.setTabOrder(self.Min_Line_Length_QText_Edit, self.Max_Line_Length_QText_Edit)
        MainWindow.setTabOrder(self.Max_Line_Length_QText_Edit, self.Increment_QText_Edit)

    def run(self):
        """
        changes the length of the selected line, calculates the Msf value and prints it
        the Msf analysis phase must be the last phase  
        """
        self.Lines_List = {i.Name.value: i  for i in self.g_i.Lines[:]}
        self.Selected_Line = self.Lines_QComboBox.currentText()
        self.Min_Line_Length = float(self.Min_Line_Length_QLine_Edit.text())
        self.Max_Line_Length = float(self.Max_Line_Length_QLine_Edit.text())
        self.Incrementation = float(self.Increment_QLine_Edit.text())
        for i in np.arange(self.Min_Line_Length,self.Max_Line_Length+self.Incrementation/2,self.Incrementation):
            QtCore.QCoreApplication.processEvents()
            self.g_i.gotostructures()
            self.Lines_List[self.Selected_Line].Second.y.set((self.Lines_List[self.Selected_Line].First.y - i))
            self.g_i.gotomesh()
            self.g_i.mesh()
            self.g_i.gotostages()
            self.g_i.calculate()
            if self.g_i.Phases[-1].CalculationResult == 1:
                self.Factor_of_safety = f"Msf for {i} meters length = {g_i.Phases[-1].Reached.SumMsf.value:.3f}"
                self.listwidget.addItems([self.Factor_of_safety])
            else:
                self.listwidget.addItems(["The calculation is failed "])
                break


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Msf_Sensivity"))
        self.Select_Line_QText_Edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Line</p></body></html>"))
        self.Min_Line_Length_QLine_Edit.setPlaceholderText(_translate("MainWindow", "Length (m)"))
        self.Min_Line_Length_QText_Edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Min. Length</p></body></html>"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Max_Line_Length_QText_Edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Max. Length</p></body></html>"))
        self.Max_Line_Length_QLine_Edit.setPlaceholderText(_translate("MainWindow", "Length (m)"))
        self.Increment_QText_Edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Incrementation</p></body></html>"))
        self.Increment_QLine_Edit.setPlaceholderText(_translate("MainWindow", "Length (m)"))


if __name__ == "__main__":
    s_i, g_i = new_server()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
