import twitter
from keys_class import Keys

class Twitter_Connector():
	def __init__(self):
		self.keys = Keys()
		self.api = twitter.Api(consumer_key=self.keys.consumer_key,
				consumer_secret=self.keys.consumer_secret,
				access_token_key=self.keys.access_token,
				access_token_secret=self.keys.access_secret)
	def get_credentials(self):
		return self.api.VerifyCredentials()

	def get_user_name(self):
		return self.api.VerifyCredentials().name

	def get_user_image_url(self):
		return self.api.VerifyCredentials().profile_image_url

	def get_user_screen_name(self):
		return self.api.VerifyCredentials().screen_name

	def get_friends(self):
		return self.api.GetFriends()

	def post_status_message(self, status_message):
		return self.api.PostUpdate(status_message)
