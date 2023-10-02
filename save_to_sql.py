import sqlite3
from operator import itemgetter
import pandas as pd
from datetime import datetime


db_users = 'users.db'

def add_user(from_user, username):

    connect = sqlite3.connect(database=db_users)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        from_user_username TEXT,
        from_user_id TEXT,
        str_time TEXT,
        flag TEXT
)
     """)
    connect.commit()

    perem = from_user

    cursor.execute('SELECT from_user_id FROM users WHERE from_user_id = ?', [perem])
    data_test = cursor.fetchone()
   
    if data_test is None:
        reg_time = datetime.now()
        reg_time = reg_time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO users VALUES (?,?,?,?)', [username, from_user, reg_time, 'False'])

    
    connect.commit()
    cursor.close()
    


def find_user():

    connect = sqlite3.connect(database=db_users)
    cursor = connect.cursor()


    connect.commit()

    perem = 'False'

    cursor.execute('SELECT from_user_username FROM users WHERE flag = ?', [perem])
    data_test = cursor.fetchall()
    connect.commit()
    cursor.close()

    return data_test

def update_flag(from_user):

    connect = sqlite3.connect(database=db_users)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        from_user_id TEXT,
        str_time TEXT,
        flag TEXT
)
     """)
    connect.commit()

    perem = from_user


    zapros = f"""
                UPDATE users 
                SET flag = 'True'
                WHERE from_user_username = '{from_user}'
    """
    cursor.execute(zapros)
    connect.commit()
    cursor.close()


