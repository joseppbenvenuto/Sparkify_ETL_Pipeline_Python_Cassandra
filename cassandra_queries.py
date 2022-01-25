# DROP TABLES
song_sessionId338_itemInSession4_drop = "DROP TABLE IF EXISTS song_sessionId338_itemInSession4"
song_userId10_sessionId182_drop = "DROP TABLE IF EXISTS song_userId10_sessionId182"
song_user_allHandsAgainstHisOwn_drop = "DROP TABLE IF EXISTS song_user_allHandsAgainstHisOwn"


# CREATE TABLES
'''
2.3.1  1.
Table for query Give me the artist, song title and song's length in the music app history that 
was heard during sessionId = 338, and itemInSession = 4
'''
song_sessionId338_itemInSession4_create = ('''CREATE TABLE IF NOT EXISTS song_sessionId338_itemInSession4
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
song_userId10_sessionId182_create = ('''CREATE TABLE IF NOT EXISTS song_userId10_sessionId182
                                       (artist text,
                                        song text,
                                        first_name text, 
                                        last_name text,
                                        userId int,
                                        sessionId int,
                                        itemInSession int,
                                        PRIMARY KEY ((userId, sessionId), itemInSession))
''')

'''
2.3.3  3. 
Table to query every user name (first and last) in my music app history 
who listened to the song 'All Hands Against His Own'
'''
song_user_allHandsAgainstHisOwn_create = ('''CREATE TABLE IF NOT EXISTS song_user_allHandsAgainstHisOwn
                                             (first_name text, 
                                              last_name text,
                                              song text,
                                              userId int,
                                              PRIMARY KEY ((song), userId))
''')


# INSERT RECORDS
song_sessionId338_itemInSession4_insert = ('''INSERT INTO song_sessionId338_itemInSession4 
                                              (artist,song,length,sessionId,itemInSession)
                                              VALUES (%s,%s,%s,%s,%s)
''')

song_userId10_sessionId182_insert = ('''INSERT INTO song_userId10_sessionId182
                                        (artist,song,first_name,last_name,userId,sessionId,itemInSession)
                                        VALUES (%s,%s,%s,%s,%s,%s,%s)
''')

song_user_allHandsAgainstHisOwn_insert = ('''INSERT INTO song_user_allHandsAgainstHisOwn
                                             (first_name,last_name,song,userId)
                                             VALUES (%s,%s,%s,%s)
''')


# QUERY LISTS 
create_table_queries = [song_sessionId338_itemInSession4_create, song_userId10_sessionId182_create, song_user_allHandsAgainstHisOwn_create]
drop_table_queries = [song_sessionId338_itemInSession4_drop, song_userId10_sessionId182_drop, song_user_allHandsAgainstHisOwn_drop]