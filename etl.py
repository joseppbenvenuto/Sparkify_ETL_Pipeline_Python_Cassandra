# Import Python packages
import pandas as pd
import cassandra
from cassandra.cluster import Cluster
import re
import os
import glob
import numpy as np
import json
import csv

from cassandra_queries import *


# Insert single record of song & artist data
def process_files(file_path):
    '''
    - Processes one CSV file at time from found path in driectory edning in "/event_data"
    - Creates a compiled CSV with data from all files 
    - The data is to be inserted into the sparkify keyspace
    '''
    # Checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + file_path

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):

    # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root,'*'))
        
        
    '''
    - Adds CSV file rows to list of CSV file rows 1 file at a time
    '''  
    # Initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
    file_count = 0  
    # For every filepath in the file path list 
    for f in file_path_list:

        # Reading CSV file 
        with open(f, 'r', encoding = 'utf8', newline = '') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

             # Extracting each data row one by one and append it        
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line) 
        # Show files processed
        file_count += 1
        print('{}/{} files processed'.format(file_count,len(file_path_list)))

    # Uncomment the code below if you would like to get total number of rows 
    print('Initial Number of rows: ' + str(len(full_data_rows_list)))
    
    
    '''
    - Writes a new compiled CSV with all CSV file data
    - Columns selected:
        1)  artist 
        2)  firstName
        3)  gender
        4)  itemSession
        5)  lastName
        6)  length
        7)  level
        8)  location
        9)  sessionId
        10) song
        11) userId
    '''
    # Creating an event data csv file called event_datafile_full csv that will be used to insert data into the
    # Apache Cassandra tables
    # Creates a csv reader dialect for open function
    csv.register_dialect('myDialect', quoting = csv.QUOTE_ALL, skipinitialspace = True)

    # Writes new csv with all rows from all csv files
    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline = '') as f:
        # Uses dialect object
        writer = csv.writer(f, dialect = 'myDialect')
        # Writes column headers
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        # For each row write only specific columns selected by the indicated indexes below
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            # Selects columns by index
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
        print('Rows compiled to CSV complete')
            
    # Check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print('Final number of rows: ' + str(sum(1 for line in f)))
        

def process_data(file_path, session):
    # Insert data to sparkify keyspace tables
    file = file_path

    with open(file, 'r', encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            # Data for artist, song title and song's length in the music app history that 
            # was heard during sessionId = 338, and itemInSession = 4
            session.execute(song_sessionId338_itemInSession4_insert,(line[0],line[9],float(line[5]),int(line[8]),int(line[3])))
            # Data for only the following: name of artist, song (sorted by itemInSession) and user 
            # (first and last name) for userid = 10, sessionid = 182
            session.execute(song_userId10_sessionId182_insert,(line[0],line[9],line[1],line[4],int(line[10]),int(line[8]),int(line[3])))
            # Data for every user name (first and last) in my music app history who listened to the 
            # song 'All Hands Against His Own'
            session.execute(song_user_allHandsAgainstHisOwn_insert,(line[1],line[4],line[9],int(line[10])))
    print('Inserted data for song_sessionId338_itemInSession4, song_userId10_sessionId182, song_user_allHandsAgainstHisOwn')


# Run all functions
def main():
    '''
    - The main function creates the cluster connection and set the sparkify keyspace and then uses the above 
      functions to successfully insert all data to their corresponding tables in the sparkify keyspace.
    '''
    # Establish connection
    cluster = Cluster(['127.0.0.1'])
    # Connect to keyspace
    session = cluster.connect()
    print('Cluster created')
    # Set keyspace
    session.set_keyspace('sparkify')
    print('Sparkify keyspace set')
    
    # Run fuctions to process and insert data into sparkify keyspace tables
    process_files(file_path = '/event_data')
    
    process_data(file_path = 'event_datafile_new.csv', session = session)
    
    # shutdown both seassion and cluster
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()