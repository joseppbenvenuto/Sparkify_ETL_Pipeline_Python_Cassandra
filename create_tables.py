import cassandra
from cassandra.cluster import Cluster
from cassandra_queries import create_table_queries, drop_table_queries


def create_keysapce():
    """
    - Establish connection to cluster and creates session
    - Returns the session and cluster
    """

    # Establish connection to cluster and creates session
    cluster = Cluster(['127.0.0.1'])
    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    print('Cluster created')

    # Create and set sparkify keyspace with 1 node
    session.execute('''CREATE KEYSPACE IF NOT EXISTS sparkify 
                       WITH REPLICATION =
                       {'class':'SimpleStrategy', 
                       'replication_factor':1}''')
    print('Keyspace sparkify created')

    # Connect to keyspace
    session.set_keyspace('sparkify')
    print('Keysapce sparkify set')

    return session, cluster


def drop_tables(session):
    """
    - Drops each table using the queries in `drop_table_queries` list
    """
    for query in drop_table_queries:
        session.execute(query)
    print('Tables in sparkify keyspace have been dropped')


def create_tables(session):
    """
    - Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        session.execute(query)
    print('Tables song_sessionId338_itemInSession4, song_userId10_sessionId182, song_user_allHandsAgainstHisOwn have been created')


def main():
    """
    - Drops (if exists) and Creates the sparkify keysapce
    - Establishes connection with the sparkify keyspace and starts session
    - Drops all the tables
    - Creates all tables needed
    - Finally, closes the connection
    """
    session, cluster = create_keysapce()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()