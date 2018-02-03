import twitter
from keys_object import Keys_object
keys = Keys_object()
api = twitter.Api(consumer_key=keys.consumer_key,
				consumer_secret=keys.consumer_secret,
				access_token_key=keys.access_token,
				access_token_secret=keys.access_secret)

print(api.VerifyCredentials())
"""
api.PostUpdates(status)
api.PostDirectMessage(user, text)
api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()
"""