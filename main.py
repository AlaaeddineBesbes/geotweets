import mysql.connector as MySQLdb
from mysql.connector import errorcode
import tweepy
import json
import requests
from DbConf import BD
import tweepy
class MyStreamListener(tweepy.StreamListener):


    def on_status(self, status):
        print('dada')
        print("coordinates : ",status._json["coordinates"])
        print("place: ", status._json["place"])
        if  status._json["place"]["country_code"]=="FR":
            with open('frenchTweets1.json', 'a', encoding='utf-8') as file:
                json.dump(status._json,file)
                tweet=status._json
                id_t = str(tweet['id']) # This is the tweet's id
                date_t = str(tweet['created_at']) # when the tweet posted
                text_t = str(tweet['text']) # content of the tweet
            
                id_u = str(tweet['user']['id']) # id of the user who posted the tweet
                name_u = str(tweet['user']['name']) # name of the user, e.g. "Wei Xu"
                screen_name_u = str(tweet['user']['screen_name']) # name of the user account, e.g. "cocoweixu"
                file.write("\n")

                file.close()
            with open('frenchTweets1.json', 'r', encoding='utf-8') as file:
                print(len(file.readlines()))
                file.close()

    def on_error(self, status_code):
        if status_code == 420:
            print('dada')
            #returning False in on_data disconnects the stream
            return False
        



ACCESS_TOKEN = '1099755262527893504-4FSaNTeMzGrXx2u9ABM4N3Ajxm4u1g' #put your access token
ACCESS_SECRET = 'szOhDRPHGuvbqTCr7pQrSMhJppCjia25eUQCRVvd7ie4U' #put the access secret
CONSUMER_KEY = '63BJCrhqS4b30syXuzFua1hDr' #put the consumer key
CONSUMER_SECRET = 'RDmMl20TpLfPYPqMlivQjDs1cH8miybFBCPlSPJnK0ARKlbRYR' #put the consumer secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
france=[-4.67, 42, 8, 51.1485061713]
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(languages=["fr"],locations=france)
