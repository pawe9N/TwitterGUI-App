import sys
sys.path.insert(0, sys.path[0]+'\\classes')

from PyQt5 import QtCore, QtGui, QtWidgets
import twitter
from classes.keys_class import Keys
from classes.twitter_connector import Twitter_Connector
from classes.twitterGUI import Ui_MainWindow
from classes.choosing_account import UI_ChoosingAccount
from classes.connection_error import UI_ConnectionError
import urllib
import requests
import time
import os.path
import re

class TwitterGUI_APP():

	def __init__(self):
		try:
			#setting twitter connection
			Tconnector = Twitter_Connector()

			#setting window
			app = QtWidgets.QApplication(sys.argv)
			mainWindow = QtWidgets.QMainWindow()
			self.ex = UI_ChoosingAccount()
			self.ex.setupUi(mainWindow)

			#setting tweets
			tweets =  Tconnector.get_tweets()
			myTimeLine = Tconnector.get_my_timeline()
			messagesTM = Tconnector.get_messagesTM()
			messagesFM = Tconnector.get_messagesFM()
			favourites = Tconnector.get_favourites()
			following = Tconnector.get_friends()
			followers = Tconnector.get_followers()

			#setting account
			data = urllib.request.urlopen(Tconnector.get_user_image_url()).read()
			self.pixmap = QtGui.QPixmap()
			self.pixmap.loadFromData(data)
			self.ex.awatarLabel.setPixmap(QtGui.QPixmap(self.pixmap))

			self.ex.profileNameLabel.setText("@"+Tconnector.get_user_screen_name())

			#start application
			self.ex.submitButton.clicked.connect(lambda: self.start_application(tweets, myTimeLine, messagesTM, messagesFM, favourites, followers, following, mainWindow, Tconnector))

			app.aboutToQuit.connect(self.closeEvent)

			sys.exit(app.exec_())

		except:
			#making error window
			app = QtWidgets.QApplication(sys.argv)
			ex = UI_ConnectionError()
			mainWindow = QtWidgets.QMainWindow()
			ex.setupUi(mainWindow)
			sys.exit(app.exec_())


	def start_application(self, tweets, myTimeLine, messagesTM, messagesFM, favourites, followers, following, mainWindow, Tconnector):
		#setting static htmls
		self.htmlMyTweets, self.nMyTweets = self.htmlTweetsSetting(myTimeLine)
		self.htmlMessagesFM, self.nmessagesFM = self.htmlMessagesSetting(messagesFM)
		self.htmlMessagesTM, nmessagesTM = self.htmlMessagesSetting(messagesTM)

		#setting htmls
		htmlTweets, ntweets = self.htmlTweetsSetting(tweets)
		htmlPhoto, nphoto =  self.htmlPhotosSetting(myTimeLine)
		htmlFavourites, nfavourites = self.htmlTweetsSetting(favourites)
		htmlFollowing, nfollowing = self.htmlFollowingSetting(following)
		htmlFollowers, nfollowers = self.htmlFollowingSetting(followers)
		
		#closing previous window
		self.ex.MainWindow.close()
		self.ex.__del__()

		#setting new window
		self.ex = Ui_MainWindow()
		self.ex.setupUi(mainWindow)

		#setting name from twitter
		self.ex.profileNameLabel.setText(Tconnector.get_user_name())

		#setting screen name from twitter
		self.ex.profileHandleLabel.setText("@"+Tconnector.get_user_screen_name())

		#setting awatar
		self.ex.awatarLabel.setPixmap(QtGui.QPixmap(self.pixmap))

		#setting description
		self.ex.descriptionLabel.setText("Description: {}".format(Tconnector.get_user_description()))
		#setting location
		self.ex.locationLabel.setText("\nLocation: {}".format(Tconnector.get_user_location()))
		#setting website
		self.ex.websiteLabel.setText("Website: {}".format(Tconnector.get_user_website()))

		self.ex.dataBrowser.setHtml(htmlTweets)

		#setting tweets number
		self.ex.tweetsNumberLabel.setText(str(self.nMyTweets))
		#setting photos number
		self.ex.photosNumberLabel.setText(str(nphoto))
		#setting messages from me number
		self.ex.messagesNumberLabel.setText(str(self.nmessagesFM))
		#setting favourites number
		self.ex.favouritesNumberLabel.setText(str(nfavourites))
		#setting following number
		self.ex.followingNumberLabel.setText(str(nfollowing))
		#setting followers number
		self.ex.followersNumberLabel.setText(str(nfollowers))

		#setting buttons actions
		self.ex.nextButton.clicked.connect(lambda: self.buttonClicked(mainWindow,
															   htmlTweets = htmlTweets,
															   htmlPhoto = htmlPhoto,
															   htmlFavourites = htmlFavourites,
															   htmlFollowers = htmlFollowers,
															   htmlFollowing = htmlFollowing))
		self.ex.backButton.clicked.connect(lambda: self.buttonClicked(mainWindow,
															   htmlTweets = htmlTweets,
															   htmlPhoto = htmlPhoto, 
															   htmlFavourites=htmlFavourites,
															   htmlFollowers = htmlFollowers,
															   htmlFollowing = htmlFollowing))

		self.ex.postingNewTweetButton.clicked.connect(lambda: self.postTweet(Tconnector))

		self.ex.sendingMessageButton.clicked.connect(lambda: self.sendMessage(Tconnector))


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
						html.append("<center><b>{}</b><br><br><img width=400 height=300 src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date))
					else:
						html.append("<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center><hr>".format(text,image[27:],date))
				elif item.media[0].type == "animated_gif":
					ntweets += 1
					image = item.media[0].media_url
					if not (os.path.exists("images/{}.png".format(image[39:]))):
						urllib.request.urlretrieve(image, "images/{}".format(image[39:]))
					if item.media[0].sizes["medium"]["w"] > 400:
						html.append("<center><b>{}</b><br><br><img width=400 height=300 src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date))
					else:
						html.append("<center><b>{}</b><br><br><img src='images/{}'><br>Date: {}</center> <hr>".format(text,image[39:],date))
			else:
				ntweets += 1
				html.append("<center><b>{}</b><br>Date: {} </center><hr>".format(text,date))
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

	#setting html messages
	def htmlMessagesSetting(self, messages):
		nmessages = 0
		html = ["<!DOCTYPE HTML><html><head>body{background-color:#141d26;color: white;} b{font-size: 30px;}</style></head><body></head><body><hr>"]
		for message in messages:
			nmessages += 1
			sender_name = message.sender_screen_name
			recipient_name = message.recipient_screen_name
			text = "".join(["&nbsp;","\"",message.text,"\"","&nbsp;"])
			date =  time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(message.created_at,'%a %b %d %H:%M:%S +0000 %Y'))
			html.append("To:{}<br>From: {}<br><center style='color:white;'><b>{}</b></center><br>Date: {} </center><hr>".format( recipient_name, sender_name, text, date))
		return 	"".join(html), nmessages


	#setting html variable which contains an information about acounts which I am following and number of these
	def htmlFollowingSetting(self,following):
		nfollowing = 0
		html = ["<!DOCTYPE HTML><html><head><style>body{background-color:#141d26;color: white;} b{font-size: 30px;} .description{font-size: 18px;} </style></head><body><hr>"]
		for item in following:
			nfollowing += 1
			name = item.name
			image = item.profile_image_url
			description = item.description
			if not (os.path.exists("images/{}.png".format(image.split("/")[5]))):
				urllib.request.urlretrieve(image, "images/{}".format(image.split("/")[5]))
			html.append("<center><img src='images/{}'><br><b>{}</b><div class='description'>{}</div></center><hr>".format(image.split("/")[5],name, description))
		return "".join(html), nfollowing


	#posting tweet and updating interface
	def postTweet(self, Tconnector):
		try:
			tweetText = self.ex.tweetTextEdit.toPlainText()
			Tconnector.post_tweet(tweetText)

			myTimeLine = Tconnector.get_my_timeline()
			self.htmlMyTweets, self.nMyTweets = self.htmlTweetsSetting(myTimeLine)
			self.ex.dataBrowser.setHtml(self.htmlMyTweets)
			self.ex.tweetsNumberLabel.setText(str(self.nMyTweets))

			self.ex.dataThemeLabel.setText("My Tweets")
			self.ex.nextButton.setEnabled(True)
			self.ex.backButton.setEnabled(True)
			self.ex.backButton.setText("Tweets")
			self.ex.nextButton.setText("Photos")

			self.ex.tweetTextEdit.setPlainText("")

		except:
			print("Posting tweet failed!")
			self.ex.tweetTextEdit.setPlainText("")


	#sending message and updating interface
	def sendMessage(self, Tconnector):
		try:
			receiver = self.ex.receiverLineEdit.text()
			message = self.ex.messageTextEdit.toPlainText()
			Tconnector.send_message(message, receiver)

			messagesFM = Tconnector.get_messagesFM()
			messagesTM = Tconnector.get_messagesTM()
			self.htmlMessagesFM, self.nmessagesFM = self.htmlMessagesSetting(messagesFM)
			self.htmlMessagesTM, nmessagesTM = self.htmlMessagesSetting(messagesTM)

			self.ex.dataBrowser.setHtml(self.htmlMessagesFM)
			self.ex.messagesNumberLabel.setText(str(self.nmessagesFM))

			self.ex.dataThemeLabel.setText("Messages from Me")
			self.ex.backButton.setEnabled(True)
			self.ex.backButton.setText("Messages to Me")
			self.ex.nextButton.setEnabled(True)
			self.ex.nextButton.setText("Following")

			self.ex.receiverLineEdit.setText("")
			self.ex.messageTextEdit.setPlainText("")

		except:
			print("Message sending failed!")
			self.ex.receiverLineEdit.setText("")
			self.ex.messageTextEdit.setPlainText("")


	#button clicked action
	def buttonClicked(self, mainWindow,
						    htmlTweets = None, 
                            htmlPhoto = None,
                            htmlMessagesTM = None,
                            htmlFavourites = None,
                            htmlFollowers = None,
                            htmlFollowing = None):
		sender = mainWindow.sender()
		if sender.text() == "Tweets":
			self.ex.dataBrowser.setHtml(htmlTweets)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setEnabled(False)
			self.ex.backButton.setText("")
			self.ex.nextButton.setText("My Tweets")
		elif sender.text() == "My Tweets":
			self.ex.dataBrowser.setHtml(self.htmlMyTweets)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setEnabled(True)
			self.ex.nextButton.setEnabled(True)
			self.ex.backButton.setText("Tweets")
			self.ex.nextButton.setText("Photos")
		elif sender.text() == "Photos":
			self.ex.dataBrowser.setHtml(htmlPhoto)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("My Tweets")
			self.ex.nextButton.setText("Messages to Me")
		elif sender.text() == "Messages to Me":
			self.ex.dataBrowser.setHtml(self.htmlMessagesTM)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Photos")
			self.ex.nextButton.setText("Messages from Me")
		elif sender.text() == "Messages from Me":
			self.ex.dataBrowser.setHtml(self.htmlMessagesFM)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setEnabled(True)
			self.ex.nextButton.setEnabled(True)
			self.ex.backButton.setText("Messages to Me")
			self.ex.nextButton.setText("Following")
		elif sender.text() == "Following":
			self.ex.dataBrowser.setHtml(htmlFollowing)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Messages from Me")
			self.ex.nextButton.setText("Followers")
		elif sender.text() == "Followers":
			self.ex.dataBrowser.setHtml(htmlFollowers)
			self.ex.dataThemeLabel.setText(sender.text())
			self.ex.backButton.setText("Following")
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

	#event for closing window without error
	def closeEvent(self):
		sys.exit(0)


def main():
	TwitterGUI_APP()


if __name__ == "__main__":
	main()