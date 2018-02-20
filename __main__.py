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


class TwitterGUI_APP():

	def __init__(self):
		#setting twitter connection
		self.Tconnector = Twitter_Connector()

		#setting window
		self.app = QtWidgets.QApplication(sys.argv)
		self.ex = Ui_MainWindow()
		self.mainWindow = QtWidgets.QMainWindow()
		self.ex.setupUi(self.mainWindow)

		#setting name from twitter
		self.ex.profileNameLabel.setText(self.Tconnector.get_user_name())

		#setting screen name from twitter
		self.ex.profileHandleLabel.setText("@"+self.Tconnector.get_user_screen_name())

		#setting awatar
		awatar_url = self.Tconnector.get_user_image_url()
		data = urllib.request.urlopen(awatar_url).read()
		pixmap = QtGui.QPixmap()
		pixmap.loadFromData(data)
		self.ex.awatarLabel.setPixmap(QtGui.QPixmap(pixmap))

		#setting description
		description = self.Tconnector.get_user_description()
		self.ex.descriptionLabel.setText("Description: {}".format(description))

		#setting location
		self.ex.locationLabel.setText("\nLocation: {}".format(self.Tconnector.get_user_location()))
		#setting website
		self.ex.websiteLabel.setText("Website: {}".format(self.Tconnector.get_user_website()))

		#setting tweets
		tweets = self.Tconnector.get_tweets()
		myTimeLine = self.Tconnector.get_my_timeline()
		favourites = self.Tconnector.get_favourites()
		following = self.Tconnector.get_friends()
		
		#setting htmls
		settingBool = True
		htmlTweets, ntweets = self.htmlTweetsSetting(tweets)
		htmlMyTweets, nMyTweets = self.htmlTweetsSetting(myTimeLine)
		htmlPhoto, nphoto =  self.htmlPhotosSetting(myTimeLine)
		htmlFavourites, nfavourites = self.htmlTweetsSetting(favourites)
		htmlFollowing, nfollowing = self.htmlFollowingSetting(following)

		self.ex.dataBrowser.setHtml(htmlTweets)

		#setting buttons properties
		self.ex.backButton.setText("")
		self.ex.backButton.setEnabled(False)
		self.ex.nextButton.setText("My Tweets")

		self.ex.nextButton.clicked.connect(lambda: self.buttonClicked(htmlTweets = htmlTweets,
															   htmlMyTweets = htmlMyTweets,
															   htmlPhoto = htmlPhoto, 
															   htmlFavourites=htmlFavourites,
															   htmlFollowing = htmlFollowing))
		self.ex.backButton.clicked.connect(lambda: self.buttonClicked(htmlTweets = htmlTweets,
															   htmlMyTweets = htmlMyTweets,
															   htmlPhoto = htmlPhoto, 
															   htmlFavourites=htmlFavourites,
															   htmlFollowing = htmlFollowing))


		#setting tweets number
		self.ex.tweetsNumberLabel.setText(str(nMyTweets))
		#setting photos number
		self.ex.photosNumberLabel.setText(str(nphoto))
		#setting favourites number
		self.ex.favouritesNumberLabel.setText(str(nfavourites))
		#setting following number
		self.ex.followingNumberLabel.setText(str(nfollowing))

		sys.exit(self.app.exec_())

	#setting html variable which containts tweets and their numbers
	#if everything is ok -> number of tweets is 20
	def htmlTweetsSetting(self,tweets):
		nphoto = 0
		ntweets = 0
		html = "<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;}</style></head><body><hr>"
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
						html += "<center><b>{}</b><br><br><img width=400 height=400 src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date)
					else:
						html += "<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date)
				elif item.media[0].type == "animated_gif":
					nphoto += 1
					ntweets += 1
					image = item.media[0].media_url
					if not (os.path.exists("images/{}.png".format(image[39:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html += "<center><b>{}</b><br><br><img width=400 height=400 src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date)
					else:
						html += "<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date)
				else:
					np
			else:
				ntweets += 1
				html += "<center><br><b>Text: {}</b><br>Date: {} </center><hr>".format(text,date)
		html += "</body></html>"
		return html, ntweets

	#setting html variable which contains an information about my photos and number of these
	def htmlPhotosSetting(self,myTimeLine):
		nphoto = 0
		html = "<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;}</style></head><body><hr><br>"
		for item in myTimeLine:
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


	#setting html variable which contains an information about acounts which I am following and number of these
	def htmlFollowingSetting(self,following):
		nfollowing = 0
		html = "<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;} b{font-size: 30px;}</style></head><body><hr>"
		for item in following:
			nfollowing += 1
			name = item.name
			image = item.profile_image_url
			if not (os.path.exists("images/{}.png".format(image.split("/")[5]))):
				urllib.request.urlretrieve(image, "images/{}".format(image.split("/")[5]))
			html += "<center><img src='images/{}'><br><b>{}</b></center><hr>".format(image.split("/")[5],name)
		html += "</body></html>"
		return html, nfollowing


	#button clicked action
	def buttonClicked(self, htmlTweets = None, 
							htmlMyTweets = None,
                            htmlPhoto = None, 
                            htmlFavourites = None,
                            htmlFollowing = None):
		sender = self.ex.MainWindow.sender()
		if sender.text() == "Tweets":
			self.ex.dataBrowser.setHtml(htmlTweets)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setEnabled(False)
			self.ex.backButton.setText("")
			self.ex.nextButton.setText("My Tweets")
		elif sender.text() == "My Tweets":
			self.ex.dataBrowser.setHtml(htmlMyTweets)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setEnabled(True)
			self.ex.backButton.setText("Tweets")
			self.ex.nextButton.setText("Photos")
		elif sender.text() == "Photos":
			self.ex.dataBrowser.setHtml(htmlPhoto)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("My Tweets")
			self.ex.nextButton.setText("Messages")
		elif sender.text() == "Messages":
			self.ex.dataBrowser.setHtml("<body>Lorem ipsum</body>")
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Photos")
			self.ex.nextButton.setText("Following")
			pass
		elif sender.text() == "Following":
			self.ex.dataBrowser.setHtml(htmlFollowing)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Messages")
			self.ex.nextButton.setText("Followers")
		elif sender.text() == "Followers":
			self.ex.dataBrowser.setHtml("<body>Lorem ipsum</body>")
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Following")
			self.ex.nextButton.setEnabled(True)
			self.ex.nextButton.setText("Favourites")
			pass
		elif sender.text() == "Favourites":
			self.ex.dataBrowser.setHtml(htmlFavourites)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Followers")
			self.ex.nextButton.setEnabled(False)
			self.ex.nextButton.setText("")

def main():
	TwitterGUI_APP()

if __name__ == "__main__":
	main()