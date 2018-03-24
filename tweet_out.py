# Dependencies
import time
import tweepy 

# Twitter API Keys
consumer_key = "BADfHZM86ux3BGq6OzQFAzeSz"
consumer_secret = "9KMYSluWvDYFlqRwW8cAM15yGwjqdmjrCNUu0PSXjWz65bDVPg"
access_token = "3142538747-HSx7wYLXiuny6WiYTJTuOE8ZgNii20AaVVZMjFa"
access_token_secret = "v2qTZ7noTAREKruem3PwxemxKtCOGd6GsYZovRSQOZOVi"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Loop through all tweets
tweet_num =1
while tweet_num <6 :
	api.update_status("tweet num " + str(time.ctime()) + "counter " + str(tweet_num))
	tweet_num  = tweet_num + 1
	time.sleep(60)
