import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import twitter
from keys_class import Keys
from twitter_connector_class import Twitter_Connector
from twitterGUI import Ui_MainWindow



def main():
	Tconnector = Twitter_Connector()

	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_MainWindow()
	mainWindow = QtWidgets.QMainWindow()
	ex.setupUi(mainWindow)

	print(Tconnector.get_credentials())

	#setting name from twitter
	ex.profileNameLabel.setText(Tconnector.get_user_name())
	#setting screen name from twitter
	ex.profileHandleLabel.setText("@"+Tconnector.get_user_screen_name())


	

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()