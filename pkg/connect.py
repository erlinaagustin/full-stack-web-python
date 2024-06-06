import psycopg2

def connection():
    try:
        conn = psycopg2.connect(database="crud",
                                host="localhost",
                                user="postgres",
                                password="root",
                                port="5432")
        
        return conn, None
    except (psycopg2.DatabaseError, Exception) as error:
        return None, error
    
def grant_access_connect():
    connect, err = connection()
    return connect, err

grant_access_connect()