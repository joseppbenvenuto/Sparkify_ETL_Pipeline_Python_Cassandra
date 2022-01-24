# DROP TABLES
table_2_3_1_1_drop = "DROP TABLE IF EXISTS table_2_3_1_1"
table_2_3_2_2_drop = "DROP TABLE IF EXISTS table_2_3_2_2"
table_2_3_3_3_drop = "DROP TABLE IF EXISTS table_2_3_3_3"


# CREATE TABLES
'''
2.3.1  1.
Table for query Give me the artist, song title and song's length in the music app history that 
was heard during sessionId = 338, and itemInSession = 4
'''
table_2_3_1_1_create = ('''CREATE TABLE IF NOT EXISTS table_2_3_1_1
                           (artist text,
                            song text, 
                            length decimal,
                            sessionId int,
                            itemInSession int,
                            PRIMARY KEY ((sessionId, itemInSession)))
''')

'''
2.3.2  2. 
Table to query name of artist, song (sorted by itemInSession) 
and user (first and last name) for userid = 10, sessionid = 182
'''
table_2_3_2_2_create = ('''CREATE TABLE IF NOT EXISTS table_2_3_2_2
                           (artist text,
                            song text,
                            first_name text, 
                            last_name text,
                            itemInSession int,
                            userId int,
                            sessionId int,
                            PRIMARY KEY ((userId, sessionId), itemInSession))
''')

'''
2.3.3  3. 
Table to query every user name (first and last) in my music app history 
who listened to the song 'All Hands Against His Own'
'''
table_2_3_3_3_create = ('''CREATE TABLE IF NOT EXISTS table_2_3_3_3
                           (first_name text, 
                            last_name text,
                            song text,
                            userId int,
                            PRIMARY KEY ((song), userId))
''')


# INSERT RECORDS
table_2_3_1_1_insert = ('''INSERT INTO table_2_3_1_1 (artist,song,length,sessionId,itemInSession)
                           VALUES (%s,%s,%s,%s,%s)
''')

table_2_3_2_2_insert = ('''INSERT INTO table_2_3_2_2 (artist,song,first_name,last_name,itemInSession,userId,sessionId)
                           VALUES (%s,%s,%s,%s,%s,%s,%s)
''')

table_2_3_3_3_insert = ('''INSERT INTO table_2_3_3_3 (first_name,last_name,song,userId)
                           VALUES (%s,%s,%s,%s)
''')


# QUERY LISTS 
create_table_queries = [table_2_3_1_1_create, table_2_3_2_2_create, table_2_3_3_3_create]
drop_table_queries = [table_2_3_1_1_drop, table_2_3_2_2_drop, table_2_3_3_3_drop]