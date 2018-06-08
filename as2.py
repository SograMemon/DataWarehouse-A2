import tweepy
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import time
import json 

consumer_key = 'Kzwyx3xCPd4FjNdPa5d7NapVJ'
consumer_secret = '5KUlCi22kXVTuKMLxmeCPEiooKQurcDoymVkGwvTS043Gs9Xqd'
access_key = '1004034353020702721-SCt8yqZg01qewOFIraU5DA4rgfM48Q'
access_secret= '2MvKkWlTM0BvZAiJcihtMPwfabFLgsRnFKgy18m00L4r4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_tweets(query):
    api = tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweeps.error.TweepError as e:
        tweets = [json.loads(e.response.text)]
    return tweets

queries = ["#Politics -filter:retweets lang:en"," \"India\"","@Windows filter:retweets lang:en", "#Trump filter:retweets lang:en"]
analyzer = SentimentIntensityAnalyzer()
Text=[]
Sentiment=[]
Score=[]
df=pd.DataFrame()
with open ('tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id','user','created_at','text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            text=""
            res=""
            score=0
            writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])
            vs= analyzer.polarity_scores(tweet.text)
            txt=tweet.text
            p = vs['pos']
            n = vs['neg']
            o = vs['neu']
            if(p>n and p>o):
                    res="Positive"
                    score=p
                    Text.append(txt)
                    Sentiment.append(res)
                    Score.append(score)
            elif(n>p and n>o):
                    res="Negative"
                    score=n
                    Text.append(txt)
                    Sentiment.append(res)
                    Score.append(score)
            else:
                    res="Neutral"
                    score=o
                    Text.append(txt)
                    Sentiment.append(res)
                    Score.append(score)
df['Text']=Text
df['Sentiment']=Sentiment
df['Score']=Score
df.to_csv('tweets1.csv')                   
