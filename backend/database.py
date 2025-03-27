import mysql.connector
from mysql.connector import Error

def get_db_connection():
    config = {
        'host': 'db',  # Dockerコンテナ名を使用
        'port': 3306,
        'database': 'koilog',
        'user': 'user',
        'password': 'password'
    }
    return mysql.connector.connect(**config) 