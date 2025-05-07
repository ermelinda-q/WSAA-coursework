import mysql.connector
import pandas as pd

# Connection to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PabloTralee2003!",
    database="myFlutesDatabase"  
)

mycursor = mydb.cursor()

# Loading the CSV into a pandas DataFrame
csv_file_path = "data/flute_data.csv"  
df_flutes = pd.read_csv(csv_file_path)

# Insert data into the 'flutes' table
for i, row in df_flutes.iterrows():
    sql = """INSERT INTO flute (fluteMaker, fluteLevel, fluteModel, fluteHead, fluteBody, fluteMechanism, priceRange)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    val = (row['fluteMaker'], row['fluteLevel'], row['fluteModel'], row['fluteHead'], 
           row['fluteBody'], row['fluteMechanism'], row['priceRange'])
    mycursor.execute(sql, val)

# Commit & save
mydb.commit()

# Close the connection
mycursor.close()
mydb.close()

print("Data imported successfully into 'flutes' table.")
