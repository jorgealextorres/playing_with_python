import psycopg2
from psycopg2 import pool

class ConnectionPool():
    postgreSQL_pool = None

    @staticmethod
    def init(host, port, databaseName, user, password):
        try:
            ConnectionPool.postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(minconn = 1, 
                                                    maxconn = 5, 
                                                    user = user,
                                                    password = password,
                                                    host = host,
                                                    port = port,
                                                    database = databaseName)
            if(ConnectionPool.postgreSQL_pool):
                print("Connection pool created successfully")

            return ConnectionPool.postgreSQL_pool

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while connecting to PostgreSQL", error)


    @staticmethod
    def finish():
        if (ConnectionPool.postgreSQL_pool):
            ConnectionPool.postgreSQL_pool.closeall
        print("PostgreSQL connection pool is closed")
