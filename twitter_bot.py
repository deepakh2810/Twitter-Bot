import tweepy
import time
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


FILE_NAME = 'last_seen_id.txt'

# reads file
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

# writes to file
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('Retriving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended') 

    for mention in reversed(mentions):
        print(str(mention.id) + ":", mention.full_text.encode("utf-8"))
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if '#whatsgoingon' in mention.full_text.lower():
            print('Found #whatsgoingon')
            print('Responding back...')
            api.update_status('@' + mention.user.screen_name + " Nothing Much. On a Vacation. Will be back soon. #whatsgoingon !", mention.id)

# replies to tweets every x seconds
sleep_seconds = 15
while True:
    reply_to_tweets()
    time.sleep(sleep_seconds)