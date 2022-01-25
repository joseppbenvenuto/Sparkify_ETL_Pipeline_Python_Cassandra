# Sparkify ETL Pipeline Python & Cassandra

## Project Description

Skarkify is a startup that wants to analyze song and user activity data that they've been collecting on their streaming app. With this initiative in mind, a Cassandra keyspace was developed in addition to an ETL pipeline in Python. 

## How to Run ETL Pipeline

1) Run create_tables.py to create keyspace if it doesn't exist and drop all existing tables in the Sparkify keyspace followed by creating new tables. This will be the first step to get the ETL pipeline up and running and will only need to be used afterwards if the project needs to start from scratch while in development.
2) Run the test.ipynb Jupyter Notebook to test any ETL pipeline work completed by running the queries coded and observing the results.  
3) With the initial batch of data in the event_data folder run the pipeline to extract, transform, and load the data into the Sparkify keysapce and their predefined tables.

## Files & Description

* **test.ipynb -**  Using Python, a script is developed to allow for keyspace testing by viewing created tables and queries.
* **create_tables.py -**  Python script is developed to drop and create tables allowing for flexibility during the ETL pipeline development phase.
* **etl.ipynb -** A Jupyter notebook containing the first phase of development for Sparkify's ETL pipeline.
* **etl.py -** Final ETL pipeline script that extracts data from CSV files, transforms the data appropriately to allow for future analysis, and loads the data into Sparkify's keyspace via pre-defined tables.
* **cassandra_queries.py -** Contains all cassandra queries used in the ETL pipeline.

## Tables

1) **songs_by_session_and_item -** sessionId (int - partition), itemInSession (int - partition), artist (text), song (text), length (decimal)
    * **query -** Table to query the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

2) **songs_by_user_and_session -** userId (int - partition), sessionId (int - partition), itemInSession (int - Cluster), artist (text), song (text), first_name (text), last_name (text) 
    * **query -** Table to query name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
    
3) **songs_by_user -** song (text - partition), userId (int - Cluster), first_name (text), last_name (text)
    * **query -** Table to query every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
