import twitter
from keys_class import Keys
import time

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

	def post_tweet(self, tweet):
		return self.api.PostUpdate(tweet)

	def get_tweets(self):
		return self.api.GetHomeTimeline(count=20, include_entities=False)

	def get_messagesFM(self):
		return self.api.GetSentDirectMessages(include_entities=False)

	def get_messagesTM(self):
		return self.api.GetDirectMessages(include_entities=False)

	def send_message(self, text, screen_name):
		return self.api.PostDirectMessage(text, screen_name=screen_name)

	def get_favourites(self):
		return self.api.GetFavorites(include_entities=False)

	def get_my_timeline(self):
		return self.api.GetUserTimeline(screen_name = self.get_user_screen_name(), include_rts=False, trim_user=True, exclude_replies=True)

	def get_followers(self):
		return self.api.GetFollowers(screen_name = self.get_user_screen_name(), include_user_entities=False)

"""
def main():
	Tconnector = Twitter_Connector()
	Tconnector.send_message("abab", "pawe9N")
	print(Tconnector.get_messagesTM())

		

if __name__ == "__main__":
	main()
"""