import twitter
from keys_class import Keys
import urllib
import requests
import time
import os.path
import re
import pprint


class Twitter_Connector():
	def __init__(self):
		self.keys = Keys()
		self.api = twitter.Api(consumer_key=self.keys.consumer_key,
				consumer_secret=self.keys.consumer_secret,
				access_token_key=self.keys.access_token,
				access_token_secret=self.keys.access_secret)

		self.credentials = self.api.VerifyCredentials()

	def get_user_name(self):
		return self.credentials.name

	def get_user_image_url(self):
		return self.credentials.profile_image_url

	def get_user_screen_name(self):
		return self.credentials.screen_name

	def get_user_description(self):
		return self.credentials.description

	def get_user_location(self):
		return self.credentials.location

	def get_user_website(self):
		return self.credentials.url

	def get_friends(self):
		return self.api.GetFriends(screen_name = self.get_user_screen_name())

	def post_status_message(self, status_message):
		return self.api.PostUpdate(status_message)

	def get_tweets(self):
		return self.api.GetHomeTimeline()

	def get_favourites(self):
		return self.api.GetFavorites()

	def get_my_timeline(self):
		return self.api.GetUserTimeline(screen_name = self.get_user_screen_name())
"""
def main():
	Tconnector = Twitter_Connector()
	statuses = Tconnector.get_friends()
	for item in statuses:
		print(item.profile_image_url.split("/")[5])
if __name__ == "__main__":
	main()
"""
