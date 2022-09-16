import mysql.connector
from mysql.connector import Error
import pandas as pd
import random
import json

#connecting to DB with user password database name and hostname
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#executing querys (connection: must call function create_db_connection,  query: string format)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

connection =create_db_connection("localhost", "root", '','nauka')


#opening json file with list of names & adding them to a list 
with open('DB/names.json') as json_file:
    data = json.load(json_file)

#adding records 100 times with random names and salaryes
for _ in range(100):

    ran1 = random.randint(1500,10000)
    
    query = f'INSERT INTO employee(FIRST_NAME, LAST_NAME, SALARY, DEPARTAMENT) VALUES ("{random.choice(data)}","{random.choice(data)}", {ran1}, "IT")'
    print(query)
    execute_query(connection, query)