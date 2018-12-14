import tweepy
print("my twitter bot")

CONSUMER_KEY='LBXBM3lVaSdeFUZjfhZSOB35B'
CONSUMER_SECRET='oXoxvCKIQNJ5AoeUP3AqnRfcaViJuFz53uYbV7PLlZYfSqM6WW'
ACCESS_KEY='2165183149-4Fwog3Jtm6I3NQrYdIdjEheJU5uQkFBrdCBhyqn'
ACCESS_SECRET='UVytQmSRAjqyoxCPoCX6LvcZvQxX8FMIVfvHjJacQLOgM'

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
#api-> provides access to entire twitter RESTful API methods. So to create API you will need your keys from the develoepr account
#Twitter requires Oauth for authentication.
#in mentions API, it is nothing but a list. Storing the things it returns in a variable we can access it.
api=tweepy.API(auth)
mentions= api.mentions_timeline()

for mentiontext in mentions:
    print(mentiontext.text)

