# WSAA - Project
# Author: E.Qejvani
# Populating the flute table from the flute_data.csv file

import mysql.connector
import pandas as pd

# Connection to database
mydb = mysql.connector.connect(
    host="ermelinda.mysql.pythonanywhere-services.com",
    user="ermelinda",
    password="flutes123",
    database="ermelinda$myflutesdatabase"  
)

mycursor = mydb.cursor()

# Loading the CSV into a pandas DataFrame
csv_file_path = "data/flute_data.csv"  
df_flutes = pd.read_csv(csv_file_path)

# Insert data into the 'flute' table
for i, row in df_flutes.iterrows():
    sql = """INSERT INTO flute (fluteMaker, fluteLevel, fluteModel, fluteHead, fluteBody, fluteMechanism, flutePrice)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val = (row['fluteMaker'], row['fluteLevel'], row['fluteModel'], row['fluteHead'], 
           row['fluteBody'], row['fluteMechanism'], row['flutePrice'])
    mycursor.execute(sql, val)

# Commit & save
mydb.commit()

# Close the connection
mycursor.close()
mydb.close()

print("Data imported successfully into 'flutes' table.")
