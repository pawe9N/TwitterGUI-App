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
import re


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
	photos = Tconnector.get_my_timeline()
	favourites = Tconnector.get_favourites()
	following = Tconnector.get_friends()
	
	#setting htmls
	settingBool = True
	htmlTweets, ntweets = htmlTweetsSetting(tweets)
	htmlPhoto, nphoto =  htmlPhotosSetting(photos)
	htmlFavourites, nfavourites = htmlTweetsSetting(favourites)
	htmlFollowing, nfollowing = htmlFollowingSetting(following)

	ex.dataBrowser.setHtml(htmlTweets)

	#setting buttons
	ex.backButton.setText("")
	ex.backButton.setEnabled(False)
	ex.nextButton.setText("Photos")

	ex.nextButton.clicked.connect(lambda: ex.buttonClicked(htmlTweets = htmlTweets,
														   htmlPhoto = htmlPhoto, 
														   htmlFavourites=htmlFavourites,
														   htmlFollowing = htmlFollowing))
	ex.backButton.clicked.connect(lambda: ex.buttonClicked(htmlTweets = htmlTweets,
														   htmlPhoto = htmlPhoto, 
														   htmlFavourites=htmlFavourites,
														   htmlFollowing = htmlFollowing))
	#setting tweets number
	ex.tweetsNumberLabel.setText(str(ntweets))
	#setting photos number
	ex.photosNumberLabel.setText(str(nphoto))
	#setting favourites number
	ex.favouritesNumberLabel.setText(str(nfavourites))
	#setting following number
	ex.followingNumberLabel.setText(str(nfollowing))

	sys.exit(app.exec_())

def htmlTweetsSetting(tweets):
	nphoto = 0
	ntweets = 0
	html = "<!DOCTYPE HTML><html><head><style></style></head><body>"
	for item in tweets:
		date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(item.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
		text = item.text
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
		if len(urls) == 1:
			text = text.replace(urls[0], "")

		if item.media is not None:
			if item.media[0].type == "photo":
				ntweets += 1
				nphoto += 1
				image = item.media[0].media_url
				if not (os.path.exists("images/{}.png".format(image[27:]))):
					urllib.request.urlretrieve(image, "images/{}".format(image[27:]))
				if item.media[0].sizes["medium"]["w"] > 400:
					html += "<center><b>Text: {}</b><br><img width=400 height=400 src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date)
				else:
					html += "<center><b>Text: {}</b><br><img src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date)
			elif item.media[0].type == "animated_gif":
				nphoto += 1
				ntweets += 1
				image = item.media[0].media_url
				if not (os.path.exists("images/{}.png".format(image[39:]))):
					urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
				if item.media[0].sizes["medium"]["w"] > 400:
					html += "<center><b>Text: {}</b><br><img width=400 height=400 src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date)
				else:
					html += "<center><b>Text: {}</b><br><img src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date)
			else:
				np
		else:
			ntweets += 1
			html += "<center><br><b>Text: {}</b><br>Date: {} </center><hr>".format(text,date)
	html += "</body></html>"
	return html, ntweets

def htmlPhotosSetting(photos):
	nphoto = 0
	html = "<!DOCTYPE HTML><html><head><style></style></head><body>"
	for item in photos:
		date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(item.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
		if item.media is not None:
			image = item.media[0].media_url
			if item.media[0].type == "photo":
				nphoto += 1
				if not (os.path.exists("images/{}.png".format(image[27:]))):
					urllib.request.urlretrieve(image, "images/{}".format(image[27:]))
				if item.media[0].sizes["medium"]["w"] > 400:
					html += "<center><img width=400 height=300 src='images/{}'><br>Date: {}</center><hr>".format(image[27:],date)
				else:
					html += "<center><img src='images/{}'><br>Date: {}</center><hr>".format(image[27:],date)
			elif item.media[0].type == "animated_gif":
				nphoto += 1
				if not (os.path.exists("images/{}.png".format(image[39:]))):
					urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
				if item.media[0].sizes["medium"]["w"] > 400:
					html += "<center><img width=400 height=300 src='images/{}'><br>Date: {}</center><hr>".format(image[39:],date)
				else:
					html += "<center><img src='images/{}'><br>Date: {}</center><hr>".format(image[39:],date)
	html += "</body></html>"
	return html, nphoto

def htmlFollowingSetting(following):
	nfollowing = 0
	html = "<!DOCTYPE HTML><html><head><style>b{font-size: 30px;}</style></head><body>"
	for item in following:
		nfollowing += 1
		name = item.name
		image = item.profile_image_url
		if not (os.path.exists("images/{}.png".format(image.split("/")[5]))):
			urllib.request.urlretrieve(image, "images/{}".format(image.split("/")[5]))
		html += "<center><img src='images/{}'><br><b>{}</b></center><hr>".format(image.split("/")[5],name)
	html += "</body></html>"
	return html, nfollowing

if __name__ == "__main__":
	main()