#Written this module specially to fulfill my requirements of
#executing some MySQL statemtents.

import mysql.connector as mysql
from mysql.connector import errorcode

def connect(username,password,database,host='localhost'):
    config = {
        "user": username,
        "password": password,
        "host": host,
        "port": 3306 ,
        "database": database
    }
    try:
        return mysql.connect(**config)
    except:
        print('Connection error')
        exit(1)

def exec(temp_cursor,query,table_name='',ret=True):
        temp_cursor.execute(query)
        try:    
            temp_cursor.execute('select * from {}'.format(table_name))
            if ret:return temp_cursor.fetchall()
        except:
            pass

def exec_multi(temp_cursor,query,val,table_name='',ret=True):    
        temp_cursor.executemany(query,val)
        try:
            temp_cursor.execute('select * from {}'.format(table_name))
            if ret :return temp_cursor.fetchall()
        except:
            pass

def display(temp_cursor,query):
    temp_cursor.execute(query)
    return temp_cursor.fetchall()