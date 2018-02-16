import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import twitter
from keys_class import Keys
from twitter_connector_class import Twitter_Connector
from twitterGUI import Ui_MainWindow
import urllib
import requests
import time
import os.path


def main():
	Tconnector = Twitter_Connector()
	#print(Tconnector.credentials)

	app = QtWidgets.QApplication(sys.argv)
	ex = Ui_MainWindow()
	mainWindow = QtWidgets.QMainWindow()
	ex.setupUi(mainWindow)

	#setting name from twitter
	ex.profileNameLabel.setText(Tconnector.get_user_name())
	#setting screen name from twitter
	ex.profileHandleLabel.setText("@"+Tconnector.get_user_screen_name())
	#setting awatar
	awatar_url = Tconnector.get_user_image_url()
	data = urllib.request.urlopen(awatar_url).read()
	pixmap = QtGui.QPixmap()
	pixmap.loadFromData(data)
	ex.awatarLabel.setPixmap(QtGui.QPixmap(pixmap))
	#setting description
	description = Tconnector.get_user_description()
	ex.descriptionLabel.setText("Description: {}".format(description))
	#setting location
	ex.locationLabel.setText("Location: {}".format(Tconnector.get_user_location()))
	#setting website
	ex.websiteLabel.setText("Website: {}".format(Tconnector.get_user_website()))
	#setting tweets
	tweets = Tconnector.get_tweets()
	html = "<!DOCTYPE HTML><html><head><style>span{text-align: center; width:30px;}</style></head><body><hr>"
	for item in tweets:
		date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(item.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
		text = item.text
		if item.media is not None:
			image = item.media[0].media_url
			print(item.media[0].media_url[27:])
			if not (os.path.exists("images/{}.png".format(image[27:]))):
				urllib.request.urlretrieve(image, "images/{}.png".format(image[27:]))
			html += "<span>Date: {} <span><br><b>Text: {}</b></span> <img src='images/{}.png'><hr>".format(date,text,image[27:])
		else:
			html += "<span>Date: {} </span><br><b>Text: {}</b><hr>".format(date,text)
	html += "</body></html>"
	ex.dataBrowser.setHtml(html)
	#setting buttons
	ex.backButton.setEnabled(False)
	ex.nextButton.setText("Photos")
	#setting tweets number
	ex.tweetsNumberLabel.setText(str(len(tweets)))

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()