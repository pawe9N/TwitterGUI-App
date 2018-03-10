import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_ChoosingAccount(object):

    def setupUi(self, MainWindow):
    	################################## Main Window ######################################################
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

        welcomeLabel = QtWidgets.QLabel(mainWidget)
        welcomeLabel.setText("Choose your account:")
        welcomeLabel.setGeometry(QtCore.QRect(225, 275, 800, 100))
        welcomeLabel.setStyleSheet("font: 50pt Monospace;font-weight:bold;")

        self.awatarLabel = QtWidgets.QLabel(mainWidget)
        self.awatarLabel.setMinimumSize(QtCore.QSize(150, 150))
        self.awatarLabel.setMaximumSize(QtCore.QSize(150, 150))
        self.awatarLabel.setPixmap(QtGui.QPixmap("images\\twitter icon.png"))
        self.awatarLabel.setScaledContents(True)
        self.awatarLabel.setGeometry(QtCore.QRect(350, 400, 160, 160))

        self.profileNameLabel = QtWidgets.QLabel(mainWidget)
        self.profileNameLabel.setText("Account login")
        self.profileNameLabel.setGeometry(QtCore.QRect(535, 425, 200, 100))
        self.profileNameLabel.setStyleSheet("font-size: 25px;")

        self.submitButton = QtWidgets.QPushButton(mainWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setText("✔")
        self.submitButton.setGeometry(QtCore.QRect(700, 425, 100, 100))
        self.submitButton.setStyleSheet("QPushButton {border: 1px solid white; border-top-right-radius: 10px; border-top-left-radius: 10px; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;}QPushButton:hover {background-color: white;color:#1dcaff;}")

        self.MainWindow.setCentralWidget(mainWidget)
        self.MainWindow.show()


    def __del__(self):
    	del self 

"""
app = QtWidgets.QApplication(sys.argv)
ex = UI_ChoosingAccount()
mainWindow = QtWidgets.QMainWindow()
ex.setupUi(mainWindow)
sys.exit(app.exec_())
"""