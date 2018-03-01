import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import requests
import time
import re
import os.path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

    	################################## Main Window ######################################################
        self.MainWindow = MainWindow
        self.MainWindow .setObjectName("MainWindow")
        self.MainWindow .setFixedSize(1140, 870)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\twitter icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow .setWindowIcon(icon)

        self.mainWIdget = QtWidgets.QWidget(self.MainWindow )
        self.mainWIdget.setStyleSheet("background: #243447;")
        ## ("background: qlineargradient(spread:pad, x1:1, y1:1, x2:0.988636, y2:0.08, stop:0 rgba(0, 199, 255, 137), stop:1 rgba(255, 255, 255, 255));

        #################################  Profile Info   #####################################################

        self.profileInfoWidget = QtWidgets.QWidget(self.mainWIdget)
        self.profileInfoWidget.setGeometry(QtCore.QRect(40, 190, 500, 500))
        self.profileInfoWidget.setStyleSheet("background: #141d26; border-radius: 30px; padding: 2px 5px;color: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.profileInfoWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        self.awatarLabel = QtWidgets.QLabel(self.profileInfoWidget)
        self.awatarLabel.setMinimumSize(QtCore.QSize(150, 150))
        self.awatarLabel.setMaximumSize(QtCore.QSize(150, 150))
        #self.awatarLabel.setStyleSheet("background-color: white;")
        self.awatarLabel.setPixmap(QtGui.QPixmap("images\\twitter icon.png"))
        self.awatarLabel.setScaledContents(True)
        self.verticalLayout.addWidget(self.awatarLabel, 0, QtCore.Qt.AlignHCenter)

        self.profileNameLabel = QtWidgets.QLabel(self.profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.profileNameLabel.setFont(font)
        self.profileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.profileNameLabel, 0, QtCore.Qt.AlignHCenter)

        self.profileHandleLabel = QtWidgets.QLabel(self.profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.profileHandleLabel.setFont(font)
        self.verticalLayout.addWidget(self.profileHandleLabel)

        self.descriptionLabel = QtWidgets.QLabel(self.profileInfoWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.descriptionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setTextFormat(QtCore.Qt.RichText)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setMinimumWidth(250)
        self.verticalLayout.addWidget(self.descriptionLabel)

        self.locationLabel = QtWidgets.QLabel(self.profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locationLabel.setFont(font)
        self.verticalLayout.addWidget(self.locationLabel)

        self.websiteLabel = QtWidgets.QLabel(self.profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.websiteLabel.setFont(font)
        self.websiteLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.verticalLayout.addWidget(self.websiteLabel)

        ############################ posting tweet widget #####################################################################

        self.tweetingWidget = QtWidgets.QWidget(self.mainWIdget)
        self.tweetingWidget.setGeometry(QtCore.QRect(820, 200, 280, 222))
        self.tweetingWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px; border-top-right-radius:30px; ")

        self.mainTweetingVBoxLayout = QtWidgets.QVBoxLayout(self.tweetingWidget)

        self.tweetingVBoxLayout = QtWidgets.QVBoxLayout()

        self.postingNewTweetLabel = QtWidgets.QLabel(self.tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.postingNewTweetLabel.setFont(font)
        self.tweetingVBoxLayout.addWidget(self.postingNewTweetLabel, 0, QtCore.Qt.AlignHCenter)

        self.tweetTextEdit = QtWidgets.QTextEdit(self.tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tweetTextEdit.setFont(font)
        self.tweetTextEdit.setStyleSheet("border: 1px solid #8899a6; padding:10px 5px; margin: 0px 5px; background: #243447; color: white;")
        self.tweetingVBoxLayout.addWidget(self.tweetTextEdit)

        self.postingNewTweetButton = QtWidgets.QPushButton(self.tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.postingNewTweetButton.setFont(font)
        self.postingNewTweetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.postingNewTweetButton.setStyleSheet("QPushButton {font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px; border: 1px solid white;} QPushButton:hover {background-color: white;color:#1dcaff;}")
        
        self.tweetingVBoxLayout.addWidget(self.postingNewTweetButton)
        self.mainTweetingVBoxLayout.addLayout(self.tweetingVBoxLayout)

        ################################### logo widget #########################################################

        self.logoWidget = QtWidgets.QWidget(self.mainWIdget)
        self.logoWidget.setGeometry(QtCore.QRect(5, 30, 1150, 100))

        self.logoVBoxLayout = QtWidgets.QVBoxLayout(self.logoWidget)
        self.logoVBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.logoLabel = QtWidgets.QLabel(self.logoWidget)
        self.logoLabel.setPixmap(QtGui.QPixmap("images\\banner.png"))
        self.logoLabel.setScaledContents(False)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.logoVBoxLayout.addWidget(self.logoLabel)

        ############################### infotable widget ########################################################

        self.infoTableWidget = QtWidgets.QWidget(self.mainWIdget)
        self.infoTableWidget.setGeometry(QtCore.QRect(330, 200, 470, 50))
        self.infoTableWidget.setStyleSheet("background: #141d26;color: white; border-radius: 10px;")

        self.infoTableGridLayout = QtWidgets.QGridLayout(self.infoTableWidget)
        self.infoTableGridLayout.setContentsMargins(0, 0, 0, 0)
        self.infoTableGridLayout.setObjectName("gridLayout_2")

        self.followingNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followingNumberLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.followingNumberLabel, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.tweetsNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tweetsNumberLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.tweetsNumberLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.messagesLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.messagesLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.messagesLabel, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)

        self.followingLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followingLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.followingLabel, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.photosNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.photosNumberLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.photosNumberLabel, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.tweetsLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tweetsLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.tweetsLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.favouritesLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.favouritesLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.favouritesLabel, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)

        self.followersLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followersLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.followersLabel, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)

        self.favouritesNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.favouritesNumberLabel.setFont(font)
        self.favouritesNumberLabel.setObjectName("favouritesNumberLabel")
        self.infoTableGridLayout.addWidget(self.favouritesNumberLabel, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)

        self.followersNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followersNumberLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.followersNumberLabel, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)

        self.photosLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.photosLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.photosLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.messagesNumberLabel = QtWidgets.QLabel(self.infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.messagesNumberLabel.setFont(font)
        self.infoTableGridLayout.addWidget(self.messagesNumberLabel, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)

        ############################## showing data widget #################################################

        self.showingDataWidget = QtWidgets.QWidget(self.mainWIdget)
        self.showingDataWidget.setGeometry(QtCore.QRect(330, 270, 470, 580))
        self.showingDataWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px;border-top-right-radius: 30px;")

        self.dataVBoxLayout = QtWidgets.QVBoxLayout(self.showingDataWidget)
        self.dataVBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.navigationWidget = QtWidgets.QWidget(self.showingDataWidget)

        self.navigationVBoxLayout = QtWidgets.QVBoxLayout(self.navigationWidget)

        self.dataThemeLabel = QtWidgets.QLabel(self.navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dataThemeLabel.setFont(font)

        self.navigationVBoxLayout.addWidget(self.dataThemeLabel, 0, QtCore.Qt.AlignHCenter)
        self.navigationHBoxLayout = QtWidgets.QHBoxLayout()

        self.backButton = QtWidgets.QPushButton(self.navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("QPushButton {border: 1px solid white; font-weight: bold;border-top-right-radius: 10px; border-top-left-radius: 10px;} :hover {background-color: white;color:#1dcaff;} :disabled {border: 1px solid #141d26}")
        self.backButton.setEnabled(False)
        self.navigationHBoxLayout.addWidget(self.backButton)

        self.nextButton = QtWidgets.QPushButton(self.navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nextButton.setFont(font)
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setStyleSheet("QPushButton {border: 1px solid white; font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px;} :hover {background-color: white;color:#1dcaff;} :disabled {border: 1px solid #141d26}")
        self.navigationHBoxLayout.addWidget(self.nextButton)

        self.navigationVBoxLayout.addLayout(self.navigationHBoxLayout)
        self.dataVBoxLayout.addWidget(self.navigationWidget)

        self.dataBrowser = QtWidgets.QTextBrowser(self.showingDataWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dataBrowser.setFont(font)
        self.dataBrowser.setStyleSheet("color: #1dcaff;")
        self.dataVBoxLayout.addWidget(self.dataBrowser)

        ######################################## messaging widget ######################################################################

        self.messagingWidget = QtWidgets.QWidget(self.mainWIdget)
        self.messagingWidget.setGeometry(QtCore.QRect(820, 450, 280, 290))
        self.messagingWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px; border-top-right-radius:30px;")

        self.messagingVerticalBoxLayout = QtWidgets.QVBoxLayout(self.messagingWidget)

        self.messagingVBoxLayout = QtWidgets.QVBoxLayout()

        self.sendAMessageLabel = QtWidgets.QLabel(self.messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendAMessageLabel.setFont(font)
        self.messagingVBoxLayout.addWidget(self.sendAMessageLabel)

        self.receiverLineEdit = QtWidgets.QLineEdit(self.messagingWidget)
        self.receiverLineEdit.setStyleSheet("border: 1px solid white; margin: 1px; padding: 1px; background: #243447; font-size: 14px;")
        self.messagingVBoxLayout.addWidget(self.receiverLineEdit)

        self.messageLabel = QtWidgets.QLabel(self.messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        self.messagingVBoxLayout.addWidget(self.messageLabel)

        self.messageTextEdit = QtWidgets.QTextEdit(self.messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.messageTextEdit.setFont(font)
        self.messageTextEdit.setStyleSheet("border: 1px solid white; padding: 10px 5px; background: #243447;")
        self.messagingVBoxLayout.addWidget(self.messageTextEdit)

        self.sendingMessageButton = QtWidgets.QPushButton(self.messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendingMessageButton.setFont(font)
        self.sendingMessageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendingMessageButton.setStyleSheet("QPushButton {font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px; border: 1px solid white;} QPushButton:hover {background-color: white;color:#1dcaff;}")
        self.messagingVBoxLayout.addWidget(self.sendingMessageButton)

        self.messagingVerticalBoxLayout.addLayout(self.messagingVBoxLayout)

        ############################ MainWindow and data ###################################################################################

        self.MainWindow .setCentralWidget(self.mainWIdget)
        self.retranslateUi(self.MainWindow )
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow )
        self.MainWindow .show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TwitterGUI-App"))
        self.profileNameLabel.setText(_translate("MainWindow", "Your Name"))
        self.profileHandleLabel.setText(_translate("MainWindow", "@YoutHandle"))
        self.descriptionLabel.setText(_translate("MainWindow", "Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque interdum rutrum sodales. Nullam mattis fermentum libero, non volutpat.\n"))
        self.locationLabel.setText(_translate("MainWindow", "Location:"))
        self.websiteLabel.setText(_translate("MainWindow", "Website:"))
        self.postingNewTweetLabel.setText(_translate("MainWindow", "Post a new tweet!"))
        self.postingNewTweetButton.setText(_translate("MainWindow", "Post"))
        self.followingNumberLabel.setText(_translate("MainWindow", "0"))
        self.tweetsNumberLabel.setText(_translate("MainWindow", "0"))
        self.messagesLabel.setText(_translate("MainWindow", "Messages"))
        self.followingLabel.setText(_translate("MainWindow", "Folowing"))
        self.photosNumberLabel.setText(_translate("MainWindow", "0"))
        self.tweetsLabel.setText(_translate("MainWindow", "Tweets"))
        self.favouritesLabel.setText(_translate("MainWindow", "Favourites"))
        self.followersLabel.setText(_translate("MainWindow", "Followers"))
        self.favouritesNumberLabel.setText(_translate("MainWindow", "0"))
        self.followersNumberLabel.setText(_translate("MainWindow", "0"))
        self.photosLabel.setText(_translate("MainWindow", "Photos"))
        self.messagesNumberLabel.setText(_translate("MainWindow", "0"))
        self.dataThemeLabel.setText(_translate("MainWindow", "Tweets"))
        self.backButton.setText(_translate("MainWindow", ""))
        self.nextButton.setText(_translate("MainWindow", "My Tweets"))
        self.dataBrowser.setHtml(_translate("MainWindow", "Test"))
        self.sendAMessageLabel.setText(_translate("MainWindow", "Send a message to:"))
        self.messageLabel.setText(_translate("MainWindow", "Message:"))
        self.sendingMessageButton.setText(_translate("MainWindow", "Send"))


"""
app = QtWidgets.QApplication(sys.argv)
ex = Ui_MainWindow()
mainWindow = QtWidgets.QMainWindow()
ex.setupUi(mainWindow)
sys.exit(app.exec_())
"""
