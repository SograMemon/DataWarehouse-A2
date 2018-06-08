DataWarehouse
Assignment 2: Sentiment Analysis of Twitter Tweet Data using ETL Process and Elastic Search
1.	Task Description

1.1	Objectives

The objective of this assignment is to extract tweets using the tweeter API. The extracted tweets then have to be stored in a CSV file for further data transformation and analysis. Advanced management processes can be carried out on the data using NoSQL DB. The data has to be transformed and loaded into the NoSQL DB for this purpose. Sentiment analysis can be performed on this data to gain insights on certain topics and perform machine learning techniques. This report aims to document the steps followed for the process of data extraction, transformation, loading and analysis.

1.2	Problem Scenario

Twitter data is quite large but twitter has place some restrictions on the number of tweets that can be accessed for free per day. This project aims to collect the unstructured, incomprehensible twitter data to draw some meaning from it by performing sentiment analysis. The twitter data has to be cleaned to remove information such as URls and emojies as they cannot be analyses for a sentiment. 

1.3	Database

Tweeter API can be used to formulate queries. This allows us to gather the tweets on selected topic. The tweets can also be filtered based on other parameters such as location and language. It is required for this project to extract a minimum of 100 tweets. Therefor a number of queries where executed to arrive at a query that resulted in an extraction of more than 100 tweets.


Figure 1: tweets csv file
2.	Twitter Tweet Extraction

1.1	Prerequisites for using tweeter API

For this project we were required to extract twitter data, transform it for analysis, perform lexicon based sentiment analysis and then import it into an elastic search instance. All these operations have to be performed on an AWS EC2 instance Ubuntu virtual machine. Therefore, the prerequisites for the extraction of data is to first set up an EC2 instance and then install the required dependencies and libraries on the remote EC2 instance. The dependencies that need to be installed include: python3 for running python files, tweepy to use the twitter API for extracting tweets and a lexicon dictionary for the sentiment analysis.



Figure 2: EC2 Instance

Figure 3: EC2 Instance Configuration


The twitter API requires the user to create a developer twitter account and an app on that account to generate an API key. This API Key is unique to each user and allows users to access the twitter API.  


  Figure 4: Twitter App Creation


Figure 5: Twitter API Key



Figure 6: Twitter using API Key to access API

1.2	Getting trending topics from tweeter

The goal of extraction was to gather more than 100 tweets. There are certain topics that are tweeted about more than others. The more popular topics are recorded by twitter as trending and can be accessed through their API. Choosing a trending topic for our search query insures that the number of tweets extracted is more than 100.


Figure 7: Twitter function to get trending tweet topics

1.3	Search Query 

The twitter API has search functions with multiple parameters that can be used to filter the tweets returned by the API. Some of the parameter available for filtering include: city name, geo location and language. Restricting the language as English helps reduce the work put into data cleaning. The resulting tweets are than stored in a csv file with fields the fields: user_id, date_created and text. The text field of the tweet extracted has to be cleaned for sentiment analysis. 



Figure 8: Twitter search query

1.4	Cleaning the twitter data

Tweets can contain a lot of special characters, emojis and URLs. These cannot be scored by the lexicon analyzer and hence have to be removed before the sentiment analysis algorithm can be applied. In order to accomplish this the text field is stored in a data frame which uses the numpy python library. Storing the text that has been tweeted allows to perform operations on the text so that the unwanted data such as emojis, URLs and hashtags. The lexicon dictionary being used is a .txt file that contains the positive, negative and neutral scores for each word. The lexicon dictionary only has values for the words and not other special characters.  



Figure 9: Remove noise from tweets




3.	Sentiment Analysis Algorithm

Sentiment Analysis was done by first extracting and cleaning twitter data which is then stored in a csv file. The type of method chosen for this project is the lexicon based classifier. In this method of sentiment analysis, the tweets collected are broken down into tokens. Each token consists of a single word. Each token is then given a score of how positive neutral and negative the word is. The score is derived from a dictionary which consists of a list of words each having a score of how negative, positive or neutral it is. The tokens from the tweet are used to retrieve their corresponding score from the dictionary. The score for all three sentiments are added for each of the tokens giving a score for the entire tweet. Therefore, each tweet will have a score for each of the sentiments. The sentiment with the highest score is the final sentiment that is linked to the tweek.  The tweet and its corresponding sentiment are stored in a csv file.  



From the sentiment analysis carried out in this project it has been concluded that the accuracy of this algorithm is neutral. 
Figure 10: Sentiment Analysis Algorithm






Figure 11: Sentiment Analysis csv output
	
4.	Loading Data into Elastic Search DB

An EC2 instance was created on AWS with a Ubuntu virtual machine. Elastic search was then installed on this virtual machine along with all its dependencies. There are several ways to import the data into Elasticsearch. In this project the high level method has been used. [1]–[7]


Figure 12: Loading results into elastic search using the high level approach


Figure 13: Command to run the script for importing



Figure 14: Output data loaded into elasticsearch



5.	ETL as Batch Process



6.	Code submission

The code has been submitted on github. The link is given below:
https://github.com/SograMemon/DataWarehouse-A2.git



7.	References


[1]	“Python Sentiment Analysis – Python Tutorial.” [Online]. Available: https://pythonspot.com/python-sentiment-analysis/. [Accessed: 07-Jun-2018].
[2]	“python pandas add column in dataframe from list - Stack Overflow.” [Online]. Available: https://stackoverflow.com/questions/26666919/python-pandas-add-column-in-dataframe-from-list. [Accessed: 07-Jun-2018].
[3]	“Create A pandas Column With A For Loop.” [Online]. Available: https://chrisalbon.com/python/data_wrangling/pandas_create_column_with_loop/. [Accessed: 07-Jun-2018].
[4]	“Python for Beginners: Reading &amp; Manipulating CSV Files.” [Online]. Available: https://www.protechtraining.com/blog/post/737. [Accessed: 07-Jun-2018].
[5]	“Tutorial - Modeling Relationships in a MySQL ERD - YouTube.” [Online]. Available: https://www.youtube.com/watch?v=HusL582R2TY. [Accessed: 24-May-2018].
[6]	“MySQL :: MySQL Workbench Manual :: 6.5 Data Export and Import.” [Online]. Available: https://dev.mysql.com/doc/workbench/en/wb-admin-export-import.html. [Accessed: 24-May-2018].
[7]	“CSCI5408_TutorialNotes01 - CSCI5408 - Data Mgmt, Warhsng Analytics (Sec 1) - 2018 Summer.” [Online]. Available: https://dal.brightspace.com/d2l/le/content/73925/viewContent/988013/View. [Accessed: 24-May-2018].

[8]	 https://github.com/harshitkgupta
[9]	 https://github.com/ayushoriginal/Sentiment-Analysis-Twitter
[10]	 https://github.com/mayank93/Twitter-Sentiment-Analysis
[11]	 https://github.com/abdulfatir/twitter-sentiment-analysis
[12]	 https://stackoverflow.com/questions/18960689/ubuntu-says-bash-program-permission-denied
[13]       https://stackoverflow.com/questions/16828035/linux-command-to-check-if-a-shell-script-is-running-or-not
