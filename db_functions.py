import mysql.connector
from decouple import config
DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_PORT = config('DB_PORT')
DB_DATABASE = config('DB_DATABASE')
def get_database_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        database=DB_DATABASE
        )
