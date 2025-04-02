import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "xxxx"
    database = "wsaa"
)

cursor = db.cursor()
sql = "delete from student where id = %s"
values = (3,)

cursor.execute(sql, values)

db.commit()
print("delete row done")

cursor.close()
db.close()