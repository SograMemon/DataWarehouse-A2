# Project Name: Choosing a location for establishing a Business

## 1.	Summary

In this project we have focused on generating visualizations, based on current demographics that could be helpful to new comers who are aspiring entrepreneurs. For simplicity we have taken a possible business use case and accordingly modeled visualizations to show which city from Nova Scotia has the highest growth potential for this venture. These visualizations of the current population along with the income, age and language distribution gives aspiring business owners an idea of his/her potential customers, their product of interest and their spending budget.  We have chosen the idea of starting a senior citizen café and have visualized the current demographics to find the city where this venture has the highest growth potential. 


## 2.	Business Idea, Problem statement, Value Proposition 

Halifax is growing as a city and with this growth there are many people from other countries who want to migrate to Halifax. With the migration process comes a number of challenges such as visa application, renting a home, finding a school to setting up a business. While google is a great tool for all these searches it does not provide a visualization of all the data available in order for users to take immediate decisions. Users have to rely on their memory and constant google searches to make the right decisions for each of these situations. Our project aims to help newcomers set up a business with ease so that they can focus on other aspects of settling down into a new place. Our project will be working with CENSUS data to give potential business owners all the information they need about their surrounding neighborhood to come to a conclusion about which products will sell in that particular area. The CENSUS data is a record of the number of people living in each location in Canada. Demographic information such as age, gender, marital status and languages spoken are also available for people living in each location. This makes the CENSUS data the perfect dataset for potential business owners to look through before they take a plunge at their new business idea. 

We aim to make the CENSUS data available to anyone who is looking to validate the feasibility of setting up their venture at a specific location. Our project will also help users find the best possible location for his or her venture based on the requirements for business success provided by the user. The user will be provided with data visualizations that will provide clear indications on which locations are better for the business as compared to others based on the parameters selected by the user. These visualizations can also be used by the user to develop business proposals and strategies that are not based on intuition but on actual data that can be presented to investors as evidence that the product or service will work.  

Starting a business in Halifax is a goal of many Halifax citizens. Many times the users get stuck in locating a place to set up their business. There is no uncomplicated way to make the users’ search successful. Our project aides the users to locate the suitable location by using data analytics concepts and tools. The data is and has been available for a long time. This project aims to make it available to public in a way that it is easy to use and meets the demands of providing some certainty to a startup that is in an uncertain risky environment. Many startups fail every year not necessarily because the venture idea was bad but because it was executed at the wrong location. The location and timing are key to any business. With this solution, users will be able to make better choices based on data and quantitative comparison between locations


## 3.	Implementation

The implementation of this project has been achieved through a series of sprint. The sprints have been discussing in detail in section 5. In this section we discuss the data set used and the procedures followed to clean, process, visualize and analyze the data. 

### 3.1.	Data Source 

The Dataset being used in this project has been taken from CENSUS Canada. This dataset consists of all the information gathered by CENSUS in 2016. CENSUS is a survey that takes place every five years. The dataset taken contains information on population, income and language distribution for the entire Canada. These records have been taken for each of the counties in each of the provinces which caused it to occupy 84mb of memory. The data was highly unstructured and required the extraction and transformation of relevant 
features. The data occupies 84 Mb of memory space.

Since the file size is to big to upload. The below instructions must be followed to download the file:
1. Goto link: http://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/details/page_Download-Telecharger.cfm?Lang=E&Tab=1&Geo1=CD&Code1=1209&Geo2=PR&Code2=12&Data=Count&SearchText=Halifax&SearchType=Begins&SearchPR=01&B1=All&TABID=1
2. Click on Option2: Comprehensive download files
3. Download CSV that is corresponding to population centres

### 3.2.	Tools used

In this project we have used a variety of tools to store, clean, process, transform and perform visualization on the dataset chosen. Some of the tools and languages used include: Python, AWS EC2 instance, Spark, MySQL and Tablue. The details of how each of the tools that were used has been described in section 3.3.                                                                                                                      
### 3.3.	Planned Procedures
In this project we planned to collect, clean and manipulate the CENSUS the following way. 

Data Extraction
The CENSUS data seemed to be well structured in the form of tables, rows and columns. However, it is not available in the form of a csv file

Data Cleaning
Once the CSV file is ready the data can be cleaned to remove any null values as well as any unnecessary columns. Depending on the quality of the data it may also have to be normalized. 

Setting up an EC2 instance and loading the data
This project will run on an EC2 instance which will be setup and configured with an Ubuntu virtual machine and the required software packages such as Python and apache spark will be installed. The CSV files prepared can then be loaded into the EC2 instance. 

After ETL processes
Further ETL processes will be carried out on the csv file so that the data can be loaded in apache spark. This will further remove any noise in the data

Querying the data
Queries will be generated based on user’s requirements. These queries will be executed by Spark SQL to retrieve the required data. If there is no data available that matches the search query an error message will be displayed. on the other hand, if the query is executed successfully the data is fetched and saved.

Connect to tableau 
The dataset resulting from the query is connected to tableau and the user is given options to choose the type of visualization he/she would like. Once the type of graph is selected tableau generates and presents the visualization generated. 

### 3.4.	Execution of the planned procedures

This project required us to collect, clean and manipulate the CENSUS data to be able to achieve the desired insights. 
Data Extraction

The CENSUS data turned out to be more unstructured then we expected. The schema made it very hard to query especially join functions. We had to extract the required data into separate data frames. Where each data frame will have a similar set of data. In the example below we show the complete dataset being split into the population, income and language data frames. We also realized that the data set was too large and decided to only take the records that belonged to Nova Scotia instead of for the entire Canada.

A.	Data Extraction with Spark
As mentioned in the proposal we planned to use spark for the ETL processes and Spark SQL for querying. However, we ran into memory errors while trying to process our entire dataset. As a result, a python scripts were run on the deployed EC2 instance to clean and extract the required data

B.	Data Extraction with Python
When Spark started to give memory errors we switched to using python scripts to extract the features we needed and remove any columns and rows with null values. The features we choose to extract where based on the visualizations we wanted to perform to determine the best city to launch our business idea “The Senior Café”. We decided to extract features such as the percentage of the senior citizen population in each city.    

Data Cleaning
Once the CSV files were ready the data was cleaned to remove any null values as well as any unnecessary columns. This dataset had a lot of null values that were removed.

Setting up an EC2 instance and loading the data
The EC2 instance was setup opting for the highest memory possible with the free student account. The required programing languages and libraries where installed. Some of the packages installed include Python, pandas library, pip library and MySQL. The dataset was then loaded into the EC2 instance. Python scripts were then written and applied to the loaded dataset to generate extracted csv files.  

ETL processes
After Extracting the required data each of the CSV files were transformed using python scripts to change the features recorded in rows to columns. The change in schema is shown below.

Querying the data
The dataset has been transformed from an unstructured dataset to a structured schema. This schema was then loaded into MySQL workbench to allow the data to be queried. The queries were chosen based on our business idea. For the future of this application the queries would be generated dynamically to generate current market visualization for any type of business desired. The query takes a CSV as an input and gives a much smaller more clean csv as a result that is then exported to tableau for visualization. The database schema after ETL processes and loading into MySQL workbench

Connect to tableau 
The dataset resulting from the query is connected to tableau and visualizations are generated by specifying the parameters used for the visualization.

Visualizations
1. Query3.sql provides visualization in which Shelburne has the highest percentage of senior citizens. This information would be helpful to someone looking to start a business as they could decide to start in Shelburne based on the given information about the current market scenario. This visualization could be used in a business pitch to support the business owner’s decision while presenting to a potential investor.
However, this visualization below shows that even though Shelburne has a higher percentage of the elderly population, the total population of Halifax is higher and hence Halifax has a larger population of senior citizens as compared to Shelburne.  

2. Lowincome.sql provides visulaization of the low income of the seniors helps us to decide on where to start a business for the seniors since they should not feel the business is expensive from their perspective. Below, the graph depicts the low income of the seniors versus the location. We can say that Halifax has the highest number of low income seniors who are 65 years and above.

3. Query3.sql provides visualization to understand which city has the highest growth potential for the senior café. This shows that Halifax has the highest population of both seniors and high income population.

4. Languages play an important role in our lives. Though English and French are the most spoken by the population all over Canada. There are people who still converse in mother tongue. Conversing in mother tongue makes one feel comfortable. Starting a business for seniors and letting them talk in the language they want to improves the business. They might find more people who speaks their language on daily basis. The business may also run on a specific theme where a specific ethnicity has been followed by more people in a location compared to other locations.

The graphs that are visualized from query4.sql conveys most number of languages being spoken by Halifax population. The first graph shows the non-aboriginal languages being spoken in the Halifax where the value is represented by its size. Indo-European is spoken by most and Afro-asiatic languages come in second. If the business is targeted towards these specific languages, the number of customers who speak the same language may like the idea of meeting more people in the same location. The second graph depicts the aboriginal languages such as Algonquian languages, Easter Algonquian languages and Mi'kmaq languages
Halifax is the most optimal location for a business in the whole of Nova Scotia. We decided to analyze the location within Halifax in more detail. We extracted another dataset specific to regions within Halifax. The map shows the area division and the associated regional codes.

## 4.	Role based work and distribution

The data was extracted, transformed and loaded to the My SQL Workbench by the Data Scientist. The Data Scientist then queried the results of the resulted dataset. The Data Engineer then took the project forward by analyzing the queries and building graphs to help the customers to look into their searches in a creative view. The Data Engineer also tested the whole process of the project for the user to provide a good user experience.

## 6.	Limitations of Current work

The limitation of current work includes the fact that the data source is static. Furthermore, the CENSUS data is collected and made available every 5 years this makes it hard to make the dataset dynamic. Another limitation is the memory space. This issue arises because the dataset records have been recorded for the entire Canada. 

## 7.	Future Work

For the future work of this project we would like to build a front end where users can select the columns they would like to visualize based on the requirement of their business and the user interface would generate the resulting query and a visualization automatically. In this way a normal user can have access to visualizations that can be shown as part of business pitches and decisions being made without having to know the details about ETL processes or about Data Science.

## 9.	Critical Review

The project was designed to help newcomers to find a location to start up their business. The project is quite straightforward as the data is in the same manner. We couldn’t experiment with the data. If only there were more required data in the census file, the data generated could have been more creative. We made lots of trials and errors on how to process the data, in the end we were convenient to visualize our results as it made us to improvise for each visualization onwards. We wanted to display the geolocations on the map for the final result as the Geolocations data weren’t available in the census file, we stuck to what we have.

## 10.	References 

[1]	“Tableau Spark SQL Connector Demo - YouTube.” [Online]. Available: https://www.youtube.com/watch?v=OKcIf6UdK7c. [Accessed: 03-Jul-2018].
[2]	“Spark SQL &amp; DataFrames | Apache Spark.” [Online]. Available: https://spark.apache.org/sql/. [Accessed: 03-Jul-2018].
[3]	“90% Of Startups Fail: Here’s What You Need To Know About The 10%.” [Online]. Available: https://www.forbes.com/sites/neilpatel/2015/01/16/90-of-startups-will-fail-heres-what-you-need-to-know-about-the-10/#5b657bfa6679. [Accessed: 03-Jul-2018].
[4]	“Tableau Help | Tableau Software.” [Online]. Available: https://www.tableau.com/support/help. [Accessed: 03-Jul-2018].
[5]	“Answer questions as fast as you can think of them with Tableau | Tableau Software.” [Online]. Available: https://www.tableau.com/trial/tableau-software?utm_campaign_id=2017049&utm_campaign=Prospecting-CORE-ALL-ALL-ALL-ALL&utm_medium=Paid+Search&utm_source=Google+Search&utm_language=EN&utm_country=USCA&kw=tableau&adgroup=CTX-Brand-Core-E&adused=221441171506&m. [Accessed: 03-Jul-2018].
[6]	“Date Functions.” [Online]. Available: https://onlinehelp.tableau.com/current/pro/desktop/en-us/functions_functions_date.html. [Accessed: 03-Jul-2018].
[7]	“Descriptive Analytics with Tableau - Creating Correlation Matrix and Boxplot Chart - YouTube.” [Online]. Available: https://www.youtube.com/watch?v=eQnH_IqUfEA. [Accessed: 03-Jul-2018].
 [8] Shanelynn, “The Pandas DataFrame – loading, editing, and viewing data in Python,” Shane Lynn, 18-Dec-2017. [Online]. Available: https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/. [Accessed: 06-Aug-2018].

[9] “Fixing Column Names in pandas,” The New, Interactive Singles Map.[Online]. Available: http://jonathansoma.com/lede/foundations/classes/pandas columns and functions/fixing-column-names-in-pandas/. [Accessed: 06-Aug-2018].

[10]“Multiple Criteria Filtering,” ritchieng.github.io. [Online]. Available: https://www.ritchieng.com/pandas-multi-criteria-filtering/. [Accessed: 06-Aug-2018].

[11] “Pandas read_csv: AttributeError: 'NoneType' object has no attribute 'dtype',” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/30383478/pandas-read-csv-attributeerror-nonetype-object-has-no-attribute-dtype. [Accessed: 06-Aug-2018].

[12] “Frequently Asked Questions (FAQ)” pandas: powerful Python data analysis toolkit - pandas 0.22.0 documentation. [Online]. Available: http://pandas.pydata.org/pandas-docs/stable/gotchas.html#support-for-integer-na. [Accessed: 06-Aug-2018].

[13] “Convert Pandas column containing NaNs to dtype `int`,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/21287624/convert-pandas-column-containing-nans-to-dtype-int. [Accessed: 06-Aug-2018].

[14] “Select rows from a DataFrame based on values in a column in pandas,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas. [Accessed: 06-Aug-2018].

[15] “pandas dataframe - select by partial string,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/11350770/pandas-dataframe-select-by-partial-string. [Accessed: 06-Aug-2018].

[16]“Combine two columns of text in dataframe in pandas/python,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python. [Accessed: 06-Aug-2018].

[17] “pivot_table No numeric types to aggregate,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/39229005/pivot-table-no-numeric-types-to-aggregate. [Accessed: 06-Aug-2018].

[18] http://www12.statcan.gc.ca/census-recensement/2016/geo/map-carte/ref/ct/files-fichiers/2016-92146-205-01.pdf

[19] http://dc1.chass.utoronto.ca.ezproxy.library.dal.ca/census/ 
