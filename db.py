from mysql.connector import Error
import mysql.connector
pw='root'
user_name='root'
host_name= 'webserver-mysql-1'
db_name='web_db'

def connecting_to_server():
    try:
        connection= mysql.connector.connect(
    host="webserver-mysql-1",
    user="root",
    password="root")

    except Error as err:
        print(f"Error: '{err}'")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="webserver-mysql-1",
            user="root",
            password="root",
            database="web_db"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
