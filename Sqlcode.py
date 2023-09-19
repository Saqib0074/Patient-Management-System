"""All SQL Functions"""
import mysql.connector
from mysql.connector import Error

pw = "admin"
db = 'patient_man_sys'

def create_db_connectedion(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password, database=db_name)
        print("Database connection established")
    except Error as err:
        print(f"Error: '{err}'")
    return connection
connection = create_db_connectedion('localhost','root',pw,db)
# execute sql queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error : '{err}'")
#read sql data
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error : '{err}'")

