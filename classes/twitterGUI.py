import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

    	################################## Main Window ######################################################
        MainWindow.setFixedSize(1140, 870)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images\\twitter icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        mainWidget = QtWidgets.QWidget(MainWindow )
        mainWidget.setStyleSheet("background: #243447;")
        ## ("background: qlineargradient(spread:pad, x1:1, y1:1, x2:0.988636, y2:0.08, stop:0 rgba(0, 199, 255, 137), stop:1 rgba(255, 255, 255, 255));

        #################################  Profile Info   #####################################################

        profileInfoWidget = QtWidgets.QWidget(mainWidget)
        profileInfoWidget.setGeometry(QtCore.QRect(40, 190, 500, 500))
        profileInfoWidget.setStyleSheet("background: #141d26; border-radius: 30px; padding: 2px 5px;color: white;")
        verticalLayout = QtWidgets.QVBoxLayout(profileInfoWidget)
        verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        self.awatarLabel = QtWidgets.QLabel(profileInfoWidget)
        self.awatarLabel.setMinimumSize(QtCore.QSize(150, 150))
        self.awatarLabel.setMaximumSize(QtCore.QSize(150, 150))
        #self.awatarLabel.setStyleSheet("background-color: white;")
        self.awatarLabel.setPixmap(QtGui.QPixmap("images\\twitter icon.png"))
        self.awatarLabel.setScaledContents(True)
        verticalLayout.addWidget(self.awatarLabel, 0, QtCore.Qt.AlignHCenter)

        self.profileNameLabel = QtWidgets.QLabel(profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.profileNameLabel.setFont(font)
        self.profileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        verticalLayout.addWidget(self.profileNameLabel, 0, QtCore.Qt.AlignHCenter)

        self.profileHandleLabel = QtWidgets.QLabel(profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.profileHandleLabel.setFont(font)
        verticalLayout.addWidget(self.profileHandleLabel)

        self.descriptionLabel = QtWidgets.QLabel(profileInfoWidget)
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
        verticalLayout.addWidget(self.descriptionLabel)

        self.locationLabel = QtWidgets.QLabel(profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.locationLabel.setFont(font)
        verticalLayout.addWidget(self.locationLabel)

        self.websiteLabel = QtWidgets.QLabel(profileInfoWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.websiteLabel.setFont(font)
        self.websiteLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        verticalLayout.addWidget(self.websiteLabel)

        ############################ posting tweet widget #####################################################################

        tweetingWidget = QtWidgets.QWidget(mainWidget)
        tweetingWidget.setGeometry(QtCore.QRect(820, 200, 280, 222))
        tweetingWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px; border-top-right-radius:30px; ")

        mainTweetingVBoxLayout = QtWidgets.QVBoxLayout(tweetingWidget)

        tweetingVBoxLayout = QtWidgets.QVBoxLayout()

        self.postingNewTweetLabel = QtWidgets.QLabel(tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.postingNewTweetLabel.setFont(font)
        tweetingVBoxLayout.addWidget(self.postingNewTweetLabel, 0, QtCore.Qt.AlignHCenter)

        self.tweetTextEdit = QtWidgets.QTextEdit(tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tweetTextEdit.setFont(font)
        self.tweetTextEdit.setStyleSheet("border: 1px solid #8899a6; padding:10px 5px; margin: 0px 5px; background: #243447; color: white;")
        tweetingVBoxLayout.addWidget(self.tweetTextEdit)

        self.postingNewTweetButton = QtWidgets.QPushButton(tweetingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.postingNewTweetButton.setFont(font)
        self.postingNewTweetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.postingNewTweetButton.setStyleSheet("QPushButton {font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px; border: 1px solid white;} QPushButton:hover {background-color: white;color:#1dcaff;}")
        
        tweetingVBoxLayout.addWidget(self.postingNewTweetButton)
        mainTweetingVBoxLayout.addLayout(tweetingVBoxLayout)

        ################################### logo widget #########################################################

        logoWidget = QtWidgets.QWidget(mainWidget)
        logoWidget.setGeometry(QtCore.QRect(5, 30, 1150, 100))

        logoVBoxLayout = QtWidgets.QVBoxLayout(logoWidget)
        logoVBoxLayout.setContentsMargins(0, 0, 0, 0)

        logoLabel = QtWidgets.QLabel(logoWidget)
        logoLabel.setPixmap(QtGui.QPixmap("images\\banner.png"))
        logoLabel.setScaledContents(False)
        logoLabel.setAlignment(QtCore.Qt.AlignCenter)

        logoVBoxLayout.addWidget(logoLabel)

        ############################### infotable widget ########################################################

        infoTableWidget = QtWidgets.QWidget(mainWidget)
        infoTableWidget.setGeometry(QtCore.QRect(330, 200, 470, 50))
        infoTableWidget.setStyleSheet("background: #141d26;color: white; border-radius: 10px;")

        infoTableGridLayout = QtWidgets.QGridLayout(infoTableWidget)
        infoTableGridLayout.setContentsMargins(0, 0, 0, 0)
        infoTableGridLayout.setObjectName("gridLayout_2")

        self.followingNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followingNumberLabel.setFont(font)
        infoTableGridLayout.addWidget(self.followingNumberLabel, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.tweetsNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tweetsNumberLabel.setFont(font)
        infoTableGridLayout.addWidget(self.tweetsNumberLabel, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.messagesLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.messagesLabel.setFont(font)
        infoTableGridLayout.addWidget(self.messagesLabel, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)

        self.followingLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followingLabel.setFont(font)
        infoTableGridLayout.addWidget(self.followingLabel, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)

        self.photosNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.photosNumberLabel.setFont(font)
        infoTableGridLayout.addWidget(self.photosNumberLabel, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.tweetsLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tweetsLabel.setFont(font)
        infoTableGridLayout.addWidget(self.tweetsLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.favouritesLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.favouritesLabel.setFont(font)
        infoTableGridLayout.addWidget(self.favouritesLabel, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)

        self.followersLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followersLabel.setFont(font)
        infoTableGridLayout.addWidget(self.followersLabel, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)

        self.favouritesNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.favouritesNumberLabel.setFont(font)
        self.favouritesNumberLabel.setObjectName("favouritesNumberLabel")
        infoTableGridLayout.addWidget(self.favouritesNumberLabel, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)

        self.followersNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.followersNumberLabel.setFont(font)
        infoTableGridLayout.addWidget(self.followersNumberLabel, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)

        self.photosLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.photosLabel.setFont(font)
        infoTableGridLayout.addWidget(self.photosLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.messagesNumberLabel = QtWidgets.QLabel(infoTableWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.messagesNumberLabel.setFont(font)
        infoTableGridLayout.addWidget(self.messagesNumberLabel, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)

        ############################## showing data widget #################################################

        showingDataWidget = QtWidgets.QWidget(mainWidget)
        showingDataWidget.setGeometry(QtCore.QRect(330, 270, 470, 580))
        showingDataWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px;border-top-right-radius: 30px;")

        dataVBoxLayout = QtWidgets.QVBoxLayout(showingDataWidget)
        dataVBoxLayout.setContentsMargins(0, 0, 0, 0)

        navigationWidget = QtWidgets.QWidget(showingDataWidget)

        navigationVBoxLayout = QtWidgets.QVBoxLayout(navigationWidget)

        self.dataThemeLabel = QtWidgets.QLabel(navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dataThemeLabel.setFont(font)

        navigationVBoxLayout.addWidget(self.dataThemeLabel, 0, QtCore.Qt.AlignHCenter)
        navigationHBoxLayout = QtWidgets.QHBoxLayout()

        self.backButton = QtWidgets.QPushButton(navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("QPushButton {border: 1px solid white; font-weight: bold;border-top-right-radius: 10px; border-top-left-radius: 10px;} :hover {background-color: white;color:#1dcaff;} :disabled {border: 1px solid #141d26}")
        self.backButton.setEnabled(False)
        navigationHBoxLayout.addWidget(self.backButton)

        self.nextButton = QtWidgets.QPushButton(navigationWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nextButton.setFont(font)
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setStyleSheet("QPushButton {border: 1px solid white; font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px;} :hover {background-color: white;color:#1dcaff;} :disabled {border: 1px solid #141d26}")
        navigationHBoxLayout.addWidget(self.nextButton)

        navigationVBoxLayout.addLayout(navigationHBoxLayout)
        dataVBoxLayout.addWidget(navigationWidget)

        self.dataBrowser = QtWidgets.QTextBrowser(showingDataWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dataBrowser.setFont(font)
        self.dataBrowser.setStyleSheet("color: #1dcaff;")
        dataVBoxLayout.addWidget(self.dataBrowser)

        ######################################## messaging widget ######################################################################

        messagingWidget = QtWidgets.QWidget(mainWidget)
        messagingWidget.setGeometry(QtCore.QRect(820, 450, 280, 290))
        messagingWidget.setStyleSheet("background: #141d26; color: white; border-top-left-radius: 30px; border-top-right-radius:30px;")

        messagingVerticalBoxLayout = QtWidgets.QVBoxLayout(messagingWidget)

        messagingVBoxLayout = QtWidgets.QVBoxLayout()

        self.sendAMessageLabel = QtWidgets.QLabel(messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendAMessageLabel.setFont(font)
        messagingVBoxLayout.addWidget(self.sendAMessageLabel)

        self.receiverLineEdit = QtWidgets.QLineEdit(messagingWidget)
        self.receiverLineEdit.setStyleSheet("border: 1px solid white; margin: 1px; padding: 1px; background: #243447; font-size: 14px;")
        messagingVBoxLayout.addWidget(self.receiverLineEdit)

        self.messageLabel = QtWidgets.QLabel(messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        messagingVBoxLayout.addWidget(self.messageLabel)

        self.messageTextEdit = QtWidgets.QTextEdit(messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.messageTextEdit.setFont(font)
        self.messageTextEdit.setStyleSheet("border: 1px solid white; padding: 10px 5px; background: #243447;")
        messagingVBoxLayout.addWidget(self.messageTextEdit)

        self.sendingMessageButton = QtWidgets.QPushButton(messagingWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendingMessageButton.setFont(font)
        self.sendingMessageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendingMessageButton.setStyleSheet("QPushButton {font-weight: bold; border-top-right-radius: 10px; border-top-left-radius: 10px; border: 1px solid white;} QPushButton:hover {background-color: white;color:#1dcaff;}")
        messagingVBoxLayout.addWidget(self.sendingMessageButton)

        messagingVerticalBoxLayout.addLayout(messagingVBoxLayout)

        ############################ MainWindow and data ###################################################################################

        MainWindow.setCentralWidget(mainWidget)
        self.retranslateUi(MainWindow )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TwitterGUI-App"))
        self.postingNewTweetLabel.setText(_translate("MainWindow", "Post a new tweet!"))
        self.postingNewTweetButton.setText(_translate("MainWindow", "Post"))
        self.messagesLabel.setText(_translate("MainWindow", "Messages"))
        self.followingLabel.setText(_translate("MainWindow", "Folowing"))
        self.tweetsLabel.setText(_translate("MainWindow", "Tweets"))
        self.favouritesLabel.setText(_translate("MainWindow", "Favourites"))
        self.followersLabel.setText(_translate("MainWindow", "Followers"))
        self.photosLabel.setText(_translate("MainWindow", "Photos"))
        self.dataThemeLabel.setText(_translate("MainWindow", "Tweets"))
        self.backButton.setText(_translate("MainWindow", ""))
        self.nextButton.setText(_translate("MainWindow", "My Tweets"))
        self.sendAMessageLabel.setText(_translate("MainWindow", "Send a message to:"))
        self.messageLabel.setText(_translate("MainWindow", "Message:"))
        self.sendingMessageButton.setText(_translate("MainWindow", "Send"))


    def __del__(self):
        del self


"""
app = QtWidgets.QApplication(sys.argv)
ex = Ui_MainWindow()
mainWindow = QtWidgets.QMainWindow()
ex.setupUi(mainWindow)
sys.exit(app.exec_())
"""
