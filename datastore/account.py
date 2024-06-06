def login(conn, username: str, password: str):
    try:
        cur = conn.cursor()
        query = '''
        SELECT username, password
        FROM public.users
        WHERE username = %s AND password = %s
        '''
        cur.execute(query, (username, password))
        resdata = cur.fetchone()
        if resdata:
            return resdata, None
        else:
            raise Exception("username or password incorrect")
    except Exception as e:
        return None, e
    
def register(conn, nama:str, email:str, username: str, password: str):
    try:
        cur = conn.cursor()
        query = "INSERT INTO users (name, email, username, password) values (%s, %s, %s, %s)"
        cur.execute(query, (nama, email, username, password))
        conn.commit()  
        return True, None  
    
    except Exception as e:
        conn.rollback()  
        return None, e  

    
def getData(conn):
    try:
        cur = conn.cursor()
        query = "select * from users"
        cur.execute(query)
        resdata = cur.fetchall()
        if resdata:
            return resdata, None
        else:
            raise Exception("data gagal diload")
    except Exception as e:
        return None, e
    
def deleteData(conn, id: int):
    try:
        cur = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cur.execute(query, (id,))
        conn.commit()
        return True, None
    except Exception as e:
        return None, e

def getDataId(conn, id:int):
    try:
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cur.execute(query, (id, ))
        resdata = cur.fetchone()
        cur.close()
        if resdata:
            return resdata, None
        else:
            raise Exception("Data gagal diload")
    except Exception as e:
        return None, e


def updateData(conn, id, name, email, username, password):
    try:
        cur = conn.cursor()
        query = """
        UPDATE users
        SET name = %s, email = %s, username = %s, password = %s
        WHERE id = %s
        """
        cur.execute(query, (name, email, username, password, id))
        conn.commit()
        cur.close()
        return True, None
    except Exception as e:
        return None, e



