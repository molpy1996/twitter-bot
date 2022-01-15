import tweepy

api_keys = open("D:\\Loisirs\\python\\twitter-bot\\src\\api_keys.txt", "r")

CONSUMER_KEY=api_keys.readline().rstrip()
CONSUMER_SECRET=api_keys.readline().rstrip()
ACCESS_TOKEN=api_keys.readline().rstrip()
ACCESS_TOKEN_SECRET=api_keys.readline().rstrip()

print(CONSUMER_KEY+CONSUMER_SECRET+ACCESS_TOKEN+ACCESS_TOKEN_SECRET)
api_keys.close()


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

#api.update_status("Hello Twitter!")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
