# DROP TABLES
songs_by_session_and_item_drop = "DROP TABLE IF EXISTS songs_by_session_and_item"
songs_by_user_and_session_drop = "DROP TABLE IF EXISTS songs_by_user_and_session"
songs_by_user_drop = "DROP TABLE IF EXISTS songs_by_user"


# CREATE TABLES
'''
2.3.1  1.
Table for query Give me the artist, song title and song's length in the music app history that 
was heard during sessionId = 338, and itemInSession = 4
'''
songs_by_session_and_item_create = ('''CREATE TABLE IF NOT EXISTS songs_by_session_and_item
                                       (sessionId int,
                                        itemInSession int,
                                        artist text,
                                        song text, 
                                        length decimal,
                                        PRIMARY KEY ((sessionId, itemInSession)))
''')

'''
2.3.2  2. 
Table to query name of artist, song (sorted by itemInSession) 
and user (first and last name) for userid = 10, sessionid = 182
'''
songs_by_user_and_session_create = ('''CREATE TABLE IF NOT EXISTS songs_by_user_and_session
                                       (userId int,
                                        sessionId int,
                                        itemInSession int,
                                        artist text,
                                        song text,
                                        first_name text, 
                                        last_name text,
                                        PRIMARY KEY ((userId, sessionId), itemInSession))
''')

'''
2.3.3  3. 
Table to query every user name (first and last) in my music app history 
who listened to the song 'All Hands Against His Own'
'''
songs_by_user_create = ('''CREATE TABLE IF NOT EXISTS songs_by_user
                           (song text,
                            userId int,
                            first_name text, 
                            last_name text,
                            PRIMARY KEY ((song), userId))
''')


# INSERT RECORDS
songs_by_session_and_item_insert = ('''INSERT INTO songs_by_session_and_item 
                                       (sessionId,itemInSession,artist,song,length)
                                       VALUES (%s,%s,%s,%s,%s)
''')

songs_by_user_and_session_insert = ('''INSERT INTO songs_by_user_and_session
                                       (userId,sessionId,itemInSession,artist,song,first_name,last_name)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s)
''')

songs_by_user_insert = ('''INSERT INTO songs_by_user
                           (song,userId,first_name,last_name)
                           VALUES (%s,%s,%s,%s)
''')


# QUERY LISTS 
create_table_queries = [songs_by_session_and_item_create, songs_by_user_and_session_create, songs_by_user_create]
drop_table_queries = [songs_by_session_and_item_drop, songs_by_user_and_session_drop,songs_by_user_drop]