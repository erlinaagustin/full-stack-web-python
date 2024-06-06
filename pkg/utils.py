from .connect import grant_access_connect

def openConnection():
    try:
        conn, err = grant_access_connect()
        if err != None:
            raise Exception(f"cannot connect to database: {err}")
        return conn, None
    except(Exception) as e:
        return None, e