
## 1.	Task Description

### 1.1	Objectives

The objective of this assignment is to utilize the Stream and Mlib functionalities of Apache Spark. The Stream function will be used to stream live tweets, using the tweeter API, into the EC2 instance created on Amazon Web Services. A portion of the extracted tweets are used for training a classifier and the remaining tweets are used for testing the accuracy of the Trained classifier. The tweeter data has to be cleaned to remove the noise which can be in the form of emojis, hashtags and retweets. The classifier will be given a test set of tweets all of which are labeled either as positive, negative or neutral. The classifier will be trained using the Spark Mlib library.

### 1.2	Problem Scenario

Twitter data is quite large but twitter has place some restrictions on the number of tweets that can be accessed for free per day. This project aims to collect the unstructured, incomprehensible twitter data to draw some meaning from it by performing sentiment analysis. The twitter data has to be cleaned to remove information such as URls and emojies as they cannot be analyzed for a sentiment. The tweets can be streamed into Spark and then the Mlib library of spark can be used to train the chosen Machine Learning model. The trained model can then be used to predict the sentiment of each of the streamed tweets.

### 1.3	Database

Tweeter API can be used to formulate queries. This allows us to gather the tweets on selected topic. The tweets can also be filtered based on other parameters such as location and language. It is required for this project to extract a minimum of 2000 tweets. Tweets from an airline database has been used for training the model for the machine learning part.

## 2.	Twitter Tweet Extraction

### 2.1	Prerequisites for using tweeter API

For this project we were required to extract twitter data, transform it for analysis, perform lexicon based sentiment analysis and then import it into an elastic search instance. All these operations have to be performed on an AWS EC2 instance Ubuntu virtual machine. Therefore, the prerequisites for the extraction of data is to first set up an EC2 instance and then install the required dependencies and libraries on the remote EC2 instance. The dependencies that need to be installed include: python3 for running python files, tweepy to use the twitter API for extracting tweets and a lexicon dictionary for the sentiment analysis.

The twitter API requires the user to create a developer twitter account and an app on that account to generate an API key. This API Key is unique to each user and allows users to access the twitter API

### 2.2	Setting up Spark on the EC2 instance 

This project uses Spark because Spark provides native binding for Java, Scala, Python and R. Spark also supports high speed live data streaming, machine learning, SQL and graph processing. Spark provides one platform for all the data mining and analysis needs. Spark also provides distributed processing. Spark provides the functionalities of map reduce while also allowing users to use SQL syntax for distributed programing.

Spark installation requires java and python to be installed on the Ubuntu virtual machine. The following diagram shows the commands required to connect to the EC2 instance and then to install Python, Java and Spark. The screenshot also shows the commands to submit jobs to the Spark instance.

### 2.3	Setting up tweets Listener

A Python script is written to provide the authentication required for accessing tweets from the tweeter API. The tweeter API provides a stream listener class which can be defined and extended so that an object of this class can perform functions to process the tweets as they are streamed. The filter function retrieves the tweets that match the specification provided. The tokenizer function breaks the tweets into tokens and filters them. In this python script we also set a port that listens to the incoming tweets. 

### 2.4 Cleaning and transforming twitter data

Tweets can contain a lot of special characters, emojis and URLs. These can produce a lot of problems in sentiment analysis by machine learning and hence these characters have to be removed before the sentiment analysis algorithm can be applied. In order to accomplish this the text field is stored in a data frame which uses the numpy python library. Storing the text that has been tweeted allows to perform operations on the text so that the unwanted data such as emojis, URLs, nextline and hashtags can be removed. 

## 3.	Sentiment Analysis Algorithm

For this project the sentiment analysis was done using the Mlib library provided by Spark. 
To perform sentiment analysis using the Mlib library we first have to choose the machine learning algorithm that will give us the best results for the given scenario. The Machine Learning algorithm is chosen based on the requirements of the problem statement, the type of data available and the desired results. In this scenario we have a labeled dataset. Our dataset consists of tweets that are labeled as either positive, neutral or negative. The availability of a labeled dataset allows us to perform supervised learning algorithms. Supervised Learning algorithms include: Random forests, Decision trees, Support Vector Machines, Logistic Regression and Liner Regression. All supervised learning algorithms require to be trained using a training dataset. The accuracy of the trained model can then be checked using the portion of the dataset that is set aside for testing. Once the model is trained and has a satisfactory prediction accuracy the model can be given more data to perform predictions. The predictions can be checked with the actual label of the tweet to measure the classifiers performance.

For this project the Machine Learning algorithm chosen is Logistic regression. Logistic Regression has been chosen over the Liner Regression model because unlike liner regression Logistic regression can deal with datasets that have more than two classes. This dataset has three classes: positive, negative and neutral. This scenario makes Logistic Regression the best algorithm that can be used. The training data is labeled using values that represent the sentiment expressed by the tweet. A tweet is labeled with the value 0 for a negative sentiment while a positive tweet is labeled 1 and a neutral tweet is labeled 2. The labeled dataset is split into training and testing datasets. The model is then trained on the training dataset. This allows the logistic regression model to form rules that are general to all the training data provided.            

## 4.	Labelling training data

Our dataset consists of tweets that have been labeled either positive, negative or neutral. In order to allow this data to be processes by the machine learning algorithm, transformation functions have been used to label the negative tweets with a value of 0, and the positive and negative tweets with a value of 1 and 2 respectively. The resulting data frame is then split into a training dataset and a testing dataset. Seventy percent of the original dataset was used for training the model and the remaining thirty percent was used for testing the model. Once the model has been trained it will be provide with more tweets so that the model can predict its sentiment. The model will present an output of zero if it predicts a negative sentiment. Similarly, an output of one or two are produced if a positive or a neutral sentiment are predicted respectively.    

## 5.	Feature selection

Feature extraction and selection is important to be able to train the logistic regression model. We perform feature extraction and selection on the incoming tweets befor testing and training the model as well as before the tweets are fed into the trained model to get a prediction. The function RegexTokenizer takes the tweet as input and returns the word in the tweet that can be taken as features. The StopWordsRemover function removes the words listed in the add_stopwords array from the list of features. This process removes words like “http” from the list of features. Words like “http” need to be removed because they do not contribute to the resulting sentiment.   

## 6.	Output

The accuracy of our trained model is 75 % which is quite good. The accuracy can be improved by performing a more rigorous feature extraction to remove features such as grammar words such as “is”, “a” and “the”. This would improve the accuracy of the model because the model would no longer consider the weight of a feature that does not contribute to the resulting sentiment. Another method of improving the accuracy is to fine tune the hyper parameters of the algorithm. In the case of Logistic Regression   

## 8.	References

[1] “removing newlines from messy strings in pandas dataframe cells?,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/44227748/removing-newlines-from-messy-strings-in-pandas-dataframe-cells. [Accessed: 25-Jun-2018].
 
[2]  “Remove line breaks with Python,” Remove Line Breaks with paragraph restoration. [Online]. Available: http://texthandler.com/info/remove-line-breaks-python/. [Accessed: 25-Jun-2018].
 
[3]  “how to combine two data frames in python pandas,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/12850345/how-to-combine-two-data-frames-in-python-pandas. [Accessed: 25-Jun-2018].
 
[4]  “How to iterate over rows in a DataFrame in Pandas?,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas. [Accessed: 25-Jun-2018].
 
[5]  “ML Pipelines,” Apache Spark™ - Unified Analytics Engine for Big Data. [Online]. Available: https://spark.apache.org/docs/2.2.0/ml-pipeline.html. [Accessed: 25-Jun-2018].
 
[6]  L. Cole, “How-To Use Python to Remove or Modify Empty Values in a CSV Dataset,” Code Like A Girl, 23-Aug-2017. [Online]. Available: https://code.likeagirl.io/how-to-use-python-to-remove-or-modify-empty-values-in-a-csv-dataset-34426c816347. [Accessed: 25-Jun-2018].
 
[7]  “pandas.DataFrame.to_csv¶,” pandas: powerful Python data analysis toolkit - pandas 0.22.0 documentation. [Online]. Available: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html. [Accessed: 25-Jun-2018].
 
[8]  “finding out the number of rows in a CSV file,” Bytes IT Community. [Online]. Available: https://bytes.com/topic/python/answers/833358-finding-out-number-rows-csv-file. [Accessed: 25-Jun-2018].
[9]   “What is Logistic Regression?,” Research Optimus Blog RSS. [Online]. Available: https://www.researchoptimus.com/article/what-is-logistic-regression.php. [Accessed: 25-Jun-2018].
[10]   S. Ray and Business Analytics and Intelligence, “8 Proven Ways for boosting the ‘Accuracy’ of a Machine Learning Model,” Analytics Vidhya, 02-May-2017. [Online]. Available: https://www.analyticsvidhya.com/blog/2015/12/improve-machine-learning-results/. [Accessed: 25-Jun-2018].
