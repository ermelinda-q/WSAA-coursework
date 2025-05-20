# WSAA - Project
# File to create the database in python.
# Author: E. Qejvani

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PabloTralee2003!"
)

mycursor = mydb.cursor()

Q1 = "CREATE DATABASE IF NOT EXISTS myFlutesDatabase"
Q2 = "USE myFlutesDatabase"
Q3 = '''CREATE TABLE flute(
    fluteID int UNSIGNED NOT NULL AUTO_INCREMENT,
    fluteMaker VARCHAR(25),
    fluteModel VARCHAR(25),
    fluteLevel VARCHAR(25),
    fluteHead VARCHAR(25),
    fluteBody VARCHAR(25),
    fluteMechanism VARCHAR(25),    
    flutePrice int UNSIGNED,
    PRIMARY KEY (fluteID)
    )'''

query_commands = [Q1, Q2, Q3]
for i in query_commands:
    mycursor.execute(i)

