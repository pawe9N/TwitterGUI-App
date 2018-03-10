import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_ConnectionError(object):

    def setupUi(self, MainWindow):
    	################################## ConnectionError Window ######################################################
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle("TwitterGUI-App")
        self.MainWindow.setFixedSize(1140, 870)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\twitter icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)

        mainWidget = QtWidgets.QWidget(self.MainWindow )
        mainWidget.setStyleSheet("background: #243447; color:white;")
        verticalLayout = QtWidgets.QVBoxLayout(mainWidget)

        errormessage = QtWidgets.QLabel(mainWidget)
        errormessage.setText("Connection error!")
        errormessage.setGeometry(QtCore.QRect(275, 325, 800, 100))
        errormessage.setStyleSheet("font: 50pt Monospace;font-weight:bold;")

        errormessage2 = QtWidgets.QLabel(mainWidget)
        errormessage2.setText("You should check your internet connection!")
        errormessage2.setGeometry(QtCore.QRect(125, 425, 1000, 100))
        errormessage2.setStyleSheet("font: 30pt Monospace;font-weight:bold;")

        self.MainWindow.setCentralWidget(mainWidget)
        self.MainWindow.show()

    def __del__(self):
        del self
"""
app = QtWidgets.QApplication(sys.argv)
ex = UI_ConnectionError()
mainWindow = QtWidgets.QMainWindow()
ex.setupUi(mainWindow)
sys.exit(app.exec_())
"""