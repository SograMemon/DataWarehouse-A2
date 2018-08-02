## 1.	Task Description

In the objective of this project was to implement different machine learning algorithms on a single data set so that the performance of each algorithm can be compared to that of the other. This project uses the language dataset from DSL 2014 workshop to train machine learning models to predict the language a sentence has been written in based on the occurrences or absence of certain words. The data set consists of two .txt files one for the testing data and the other for the training data.[1] 

The process of achieving the predictions from these machine learning algorithms involves a number of steps. The data set has to downloaded and imported into the Anaconda Jupiter notebook. Followed by the process of feature extraction, feature selection and model training. These processes are encapsulated in a pipeline so that the training dataset can be rationalized and passed through the already trained model. The resulting prediction is then compared to the actual results to calculate the accuracy of the model.[2], [3] 

The accuracy of a model varies based on multiple parameters such as the algorithm used and how well it is suited to the data as well as the features selected.[4] The variation of model accuracy has been shown based on the change in these parameters. A number of visualization techniques have been used to represent this data. In order to perform these predictions, visualizations and analysis a number of resources have been used. These resources include Python libraries like the sklearn, numpy, pandas and matplotlib.[5][6]–[8][9] The Anaconda Jupiter notebook provides a user friendly development environment for easy execution and debugging.[10]      

## 2.	Procedures Followed

# 2.1	Parsing dataset into a Dataframe

The dataset consists of sentences and the language this sentence belongs to. This data is not in a suitable format for training a classifier

# 2.2	Feature Extraction

The CountVectorizer() function has to be used to extract the features from the dataset.[11] Features are parameters that vary from one record to another effecting the resulting classification of the record. In this case the frequency of occurrence of each word in a given sentence are the features extracted and the language a sentence belongs to is the label used for classification. 

# 2.3	Sampling
 
This dataset is quite large consisting of 2000 records per language. Since this dataset has thirteen languages this means there are 26,0000 records in total.[1] In order to generate plots that show a clear separation of points, based on the language class the point belongs to, a smaller sample of points has been taken for plotting the graphs. The sample function from the pandas library has been used to select an equal number of points from each of the thirteen language classes.[5] These points from each of the thirteen languages have been chosen in random order. We wanted to select 200 points from each language this is achieved by setting the n parameter of the sample function to the total number of records to be returned and leaving all the other parameters at the default setting. When all parameters except the n value are given the default setting the function chooses an equal weightage of points for each of the classes.[5] In our case we need 200 records for each of the 13 values giving a total of 2600 returned records. Therefor the value of the n parameter must be set to 2600 to select 200 points from each language.

# 2.4 Feature Selection
We have used chi square to select the features since the desired number of features can be selected with best scores using the chi square statistics. The training dataset is divided to data and target. Using SelectKBest function, we select best features. The best features are displayed using fit_transform function.

The whole dataset is divided into training and testing data. Training data is fitted into df_x and df_y. The testing data is fitted into dft. The number of columns, 2600 is randomly selected from the dataset as training and testing. The training dataset is utilized to train the pipeline model and testing data is used to predict accuracy and confusion matrix of the model. Detailed process is described below. The test data is splitted into two dataframes, one dataframe consisting Sentence column, other column consisting Language dataset. 

## Conclusion:
Based on the classifiers’ accuracy, we can say that Decision Tree classifier gives the best accurate result(1.0) compared to other classifiers. The Linear SVC(0.57) and Logistic Regression(0.56) give almost close accurate results after Decision Tree Classifier. Benoulli NB is positioned at 4th giving 0.47 and Multionmial NB gives 0.26.

