import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import twitter
from keys_class import Keys
from twitter_connector_class import Twitter_Connector
from twitterGUI import Ui_MainWindow
from choosing_account import UI_ChoosingAccount
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
		app = QtWidgets.QApplication(sys.argv)
		self.mainWindow = QtWidgets.QMainWindow()
		self.ex = UI_ChoosingAccount()
		self.ex.setupUi(self.mainWindow)

		#setting tweets
		tweets =  self.Tconnector.get_tweets()
		myTimeLine = self.Tconnector.get_my_timeline()
		messages = self.Tconnector.get_messages()
		favourites = self.Tconnector.get_favourites()
		following = self.Tconnector.get_friends()

		#setting account
		data = urllib.request.urlopen(self.Tconnector.get_user_image_url()).read()
		self.pixmap = QtGui.QPixmap()
		self.pixmap.loadFromData(data)
		self.ex.awatarLabel.setPixmap(QtGui.QPixmap(self.pixmap))

		self.ex.profileNameLabel.setText("@"+self.Tconnector.get_user_screen_name())

		#start application
		self.ex.submitButton.clicked.connect(lambda: self.start_application(tweets, myTimeLine, messages, favourites, following))

		sys.exit(app.exec_())


	def start_application(self, tweets, myTimeLine, messages, favourites, following):
		#setting htmls
		htmlTweets, ntweets = self.htmlTweetsSetting(tweets)
		htmlMyTweets, nMyTweets = self.htmlTweetsSetting(myTimeLine)

		#closing previous window
		self.ex.MainWindow.close()
		self.ex.__del__()

		htmlPhoto, nphoto =  self.htmlPhotosSetting(myTimeLine)
		htmlMessages, nmessages = self.htmlMessagesSetting(messages)
		htmlFavourites, nfavourites = self.htmlTweetsSetting(favourites)
		htmlFollowing, nfollowing = self.htmlFollowingSetting(following)

		#setting new window
		self.ex = Ui_MainWindow()
		self.ex.setupUi(self.mainWindow)

		#setting name from twitter
		self.ex.profileNameLabel.setText(self.Tconnector.get_user_name())

		#setting screen name from twitter
		self.ex.profileHandleLabel.setText("@"+self.Tconnector.get_user_screen_name())

		#setting awatar
		self.ex.awatarLabel.setPixmap(QtGui.QPixmap(self.pixmap))

		#setting description
		self.ex.descriptionLabel.setText("Description: {}".format(self.Tconnector.get_user_description()))
		#setting location
		self.ex.locationLabel.setText("\nLocation: {}".format(self.Tconnector.get_user_location()))
		#setting website
		self.ex.websiteLabel.setText("Website: {}".format(self.Tconnector.get_user_website()))

		self.ex.dataBrowser.setHtml(htmlTweets)

		#setting tweets number
		self.ex.tweetsNumberLabel.setText(str(nMyTweets))
		#setting photos number
		self.ex.photosNumberLabel.setText(str(nphoto))
		#setting messages number
		self.ex.messagesNumberLabel.setText(str(nmessages))
		#setting favourites number
		self.ex.favouritesNumberLabel.setText(str(nfavourites))
		#setting following number
		self.ex.followingNumberLabel.setText(str(nfollowing))

		#setting buttons actions
		self.ex.nextButton.clicked.connect(lambda: self.buttonClicked(htmlTweets = htmlTweets,
															   htmlMyTweets = htmlMyTweets,
															   htmlPhoto = htmlPhoto,
															   htmlMessages = htmlMessages, 
															   htmlFavourites=htmlFavourites,
															   htmlFollowing = htmlFollowing))
		self.ex.backButton.clicked.connect(lambda: self.buttonClicked(htmlTweets = htmlTweets,
															   htmlMyTweets = htmlMyTweets,
															   htmlPhoto = htmlPhoto, 
															   htmlMessages = htmlMessages, 
															   htmlFavourites=htmlFavourites,
															   htmlFollowing = htmlFollowing))

		self.ex.postingNewTweetButton.clicked.connect(lambda: self.postTweet())

		self.ex.sendingMessageButton.clicked.connect(lambda: self.sendMessage())


	#setting html variable which containts tweets and their numbers
	#if everything is ok -> number of tweets is 20
	def htmlTweetsSetting(self,tweets):
		ntweets = 0
		html = ["<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;}</style></head><body><hr>"]
		for item in tweets:
			date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(item.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
			text = item.text
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
			if len(urls) == 1:
				text = text.replace(urls[0], "")
			if item.media is not None:
				if item.media[0].type == "photo":
					ntweets += 1
					image = item.media[0].media_url
					if not (os.path.exists("images/{}.png".format(image[27:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[27:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html.append("<center><b>{}</b><br><br><img width=400 height=400 src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date))
					else:
						html.append("<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date))
				elif item.media[0].type == "animated_gif":
					ntweets += 1
					image = item.media[0].media_url
					if not (os.path.exists("images/{}.png".format(image[39:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html.append("<center><b>{}</b><br><br><img width=400 height=400 src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date))
					else:
						html.append("<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date))
			else:
				ntweets += 1
				html.append("<center><br><b>Text: {}</b><br>Date: {} </center><hr>".format(text,date))
		return 	"".join(html), ntweets


	#setting html variable which contains an information about my photos and number of these
	def htmlPhotosSetting(self,myTimeLine):
		nphoto = 0
		html = ["<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;}</style></head><body><hr>"]
		for item in myTimeLine:
			date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(item.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
			if item.media is not None:
				image = item.media[0].media_url
				if item.media[0].type == "photo":
					nphoto += 1
					if not (os.path.exists("images/{}.png".format(image[27:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[27:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html.append("<center><b>#{}</b><br><img width=400 height=300 src='images/{}'><br>Date: {}</center><hr>".format(nphoto, image[27:],date))
					else:
						html.append("<center><b>#{}</b><br><img src='images/{}'><br>Date: {}</center><hr>".format(nphoto, image[27:],date))
				elif item.media[0].type == "animated_gif":
					nphoto += 1
					if not (os.path.exists("images/{}.png".format(image[39:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html.append("<center><b>#{}</b><br><img width=400 height=300 src='images/{}'><br>Date: {}</center><hr>".format(nphoto, image[39:],date))
					else:
						html.append("<center><b>#{}</b><br><img src='images/{}'><br>Date: {}</center><hr>".format(nphoto, image[39:],date))
		return "".join(html), nphoto


	def htmlMessagesSetting(self, messages):
		nmessages = 0
		html = ["<!DOCTYPE HTML><html><head><style>.sender{background-color:#1DA1F2;color: white;}b{font-size: 20px;}</style></head><body><hr>"]
		for message in messages:
			nmessages += 1
			sender_name = message.sender_screen_name
			text = "".join(["&nbsp;","\"",message.text,"\"","&nbsp;"])
			date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(message.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
			html.append("<center class='sender' >Message:<br><b>{}</b><br>Sender: {}<br>Date: {} </center><hr>".format(text, sender_name, date))
		return 	"".join(html), nmessages


	#setting html variable which contains an information about acounts which I am following and number of these
	def htmlFollowingSetting(self,following):
		nfollowing = 0
		html = ["<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;} b{font-size: 30px;}</style></head><body><hr>"]
		for item in following:
			nfollowing += 1
			name = item.name
			image = item.profile_image_url
			if not (os.path.exists("images/{}.png".format(image.split("/")[5]))):
				urllib.request.urlretrieve(image, "images/{}".format(image.split("/")[5]))
			html.append("<center><img src='images/{}'><br><b>{}</b></center><hr>".format(image.split("/")[5],name))
		return "".join(html), nfollowing


	#posting tweet
	def postTweet(self):
		tweetText = self.ex.tweetTextEdit.toPlainText()
		self.Tconnector.post_tweet(tweetText)

		myTimeLine = self.Tconnector.get_my_timeline()
		htmlMyTweets, nMyTweets = self.htmlTweetsSetting(myTimeLine)
		self.ex.dataBrowser.setHtml(htmlMyTweets)
		self.ex.tweetsNumberLabel.setText(str(nMyTweets))

		self.ex.dataThemeLabel.setText("My Tweets")
		self.ex.backButton.setEnabled(True)
		self.ex.backButton.setText("Tweets")
		self.ex.nextButton.setText("Photos")

		self.ex.tweetTextEdit.setPlainText("")


	#sending message
	def sendMessage(self):
		receiver = self.ex.receiverLineEdit.text()
		message = self.ex.messageTextEdit.toPlainText()
		self.Tconnector.send_message(message, receiver)

		messages = self.Tconnector.get_messages()
		htmlMessages, nMessages = self.htmlMessagesSetting(messages)
		self.ex.dataBrowser.setHtml(htmlMessages)
		self.ex.tweetsNumberLabel.setText(str(nMessages))

		self.ex.dataBrowser.setHtml(htmlMessages)
		self.ex.dataThemeLabel.setText("Messages")
		self.ex.backButton.setEnabled(True)
		self.ex.backButton.setText("Photos")
		self.ex.nextButton.setEnabled(True)
		self.ex.nextButton.setText("Following")

		self.ex.receiverLineEdit.setText("")
		self.ex.messageTextEdit.setPlainText("")


	#button clicked action
	def buttonClicked(self, htmlTweets = None, 
							htmlMyTweets = None,
                            htmlPhoto = None,
                            htmlMessages = None, 
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
			self.ex.dataBrowser.setHtml(htmlMessages)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Photos")
			self.ex.nextButton.setText("Following")
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
		elif sender.text() == "Favourites":
			self.ex.dataBrowser.setHtml(htmlFavourites)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Followers")
			self.ex.nextButton.setEnabled(False)
			self.ex.nextButton.setText("")

	#destructor 
	def __del__(self):
		del self


def main():
	TwitterGUI_APP()


if __name__ == "__main__":
	main()