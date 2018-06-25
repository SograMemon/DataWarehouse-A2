import pandas as pd
import csv

df=pd.read_csv('Tweets.csv', names=['tweet_id','airline_sentiment','airline_sentiment_confidence','negativereason','negativereason_confidence','airline','airline_sentiment_gold','name','negativereason_gold','retweet_count','text','tweet_coord','tweet_created','tweet_location','user_timezone'])
#print(df.values)
for index, row in df.iterrows():
   # print(row)
   data1=df['text'].replace(['@',r'\\n','"','\\r\\n','\r\n','\\r','\n',r'\\r'],['','','','','','','',''],regex = True)
   data2=df['airline_sentiment'].replace(['positive'],['positive'],regex = True)

  # print(data)
data=pd.concat([data1,data2],axis=1)
   #df['text'].replace([r'\n','@'],'
data.fillna(0)

data.to_csv('Tweets2.csv')
