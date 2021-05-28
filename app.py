import os
from flask import Flask, render_template, request
import tweepy
from decouple import config

access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

api_key = config('API_KEY')
api_key_secret = config('API_KEY_SECRET')

auth=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

india_woeid=23424848

trend_result=api.trends_place(india_woeid)

template_dir=os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/count', methods = ['POST', 'GET'])
def hello_name():
	tweet_name = request.form['tweet_name']
	#model.get_tweet_count
	tweet_count = get_tweet_count(tweet_name)
	return render_template('count.html', tweet_count = tweet_count)

def get_tweet_count(tweet_name):

    count=0
    for trend in trend_result[0]["trends"][:]:
        if tweet_name==(trend["name"]):
        #print(trend["name"])
            count+=1
            #print("Hashtag count : ",trend["tweet_volume"])
            return trend["tweet_volume"];
    
    #if count==0:
        #print("No hashtag found or hashtag not trending anymore")
	    #Processing....
	#return 2;

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8000, debug = True)
