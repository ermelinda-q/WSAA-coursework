import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "xxxxxxx",
    database = "wsaa"
)

cursor = db.cursor()
sql = "update student set name=%s, age=%s where id = %s"
values = ("Joe", 33, 2)

cursor.execute(sql, values)

db.commit()
print("Update done")

cursor.close()
db.close()
