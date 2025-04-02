import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "xxxxx",
    database = "wsaa"
)

cursor = db.cursor()
sql = "create table student (id int auto_increment primary key, name varchar(250), age int)"

cursor.execute(sql)

db.close()
cursor.close()