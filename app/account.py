from pkg import openConnection
import datastore
import requests

from flask import jsonify

def login(username: str, password: str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception (f"{err}")
        
        resLogin, err = datastore.login(conn, username, password)
        if err != None:
            raise Exception(err)
        return resLogin, None
    
    except Exception as e:
        return None, e
    
def loginWithApi(username: str, password: str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        # hit api ke service login next meet
        url = "http://127.0.0.1:8000/login" 
        data = {
            "username": username,
            "password": password
        }       
        res = requests.post(url=url, json=data)
        dt = res.json()
        print(dt)
        if dt.get("status_code") != "00":
            message = dt.get("message")
            return None, f"login {message}"

        data = dt.get("data")
        return data, None
       
        
    except Exception as e:
        return None, e

def getData():
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resUser, err = datastore.getData(conn)
        if err != None:
            raise Exception(err)
        return resUser, None
    except Exception as e:
        return None, e

def getDataId(id:int):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        resUser, err = datastore.getDataId(conn, id)
        if err != None:
            raise Exception(err)
        return resUser, None
    except Exception as e:
        return None, e

def register(nama:str, email:str, username:str, password:str):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        resRegister, err = datastore.register(conn, nama, email, username, password)
        if err != None:
            raise Exception(err)
        return resRegister, None
    except Exception as e:
        return None, e
        
    
def delete(id: int):
    try:
        conn, err = openConnection()
        if err is not None or conn is None:
            raise Exception(f"{err}")
        resDelete, err = datastore.deleteData(conn, id)
        if err is not None:
            raise Exception(err)
        return resDelete, None
    except Exception as e:
        return None, e

def update(id, name, email, username, password):
    try:
        conn, err = openConnection()
        if err is not None or conn is None:
            raise Exception(f"{err}")
        
        resUpdate, err = datastore.updateData(conn, id, name, email, username, password)
        if err is not None:
            raise Exception(err)
        
        return resUpdate, None
    except Exception as e:
        return None, e

    
def getListUserAccount(keyword:str, limit: int, page: int):
    try:
        conn, err = openConnection()
        if err != None or conn == None:
            raise Exception(f"{err}")
        
        # hit api ke service login next meet
        resListUserAccount, err = datastore.getListUserAccount(conn, keyword, limit, page )
        if err != None:
            raise Exception(err)
        return resListUserAccount, None
    except Exception as e:
        return None, e