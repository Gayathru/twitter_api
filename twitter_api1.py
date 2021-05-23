import tweepy
import sys

access_token="1395443487068233729-mPf88Fz2PT3BaDj7XG8ITvfgygmtwH"
access_token_secret="EraRSZQSEN2t1QeO2NWK94t1jarsvVxfWWeqp9EGgbC69"

api_key="X09UmwH4TO3N4lgJTBuSblYtp"
api_key_secret="5PNGEXhm5XmeqtMKxmhoUca5rrSxMm38wgLIjJ6KP6JxPhve8O"

auth=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

india_woeid=23424848

trend_result=api.trends_place(india_woeid)

val=input("Enter a hashtag : ")
#Sample input #Palestinewin

for trend in trend_result[0]["trends"][:]:
    if val==(trend["name"]):
        print("Hashtag count : ",trend["tweet_volume"])
    else:
        print("Hashtag not found or is not trending")
        
    



