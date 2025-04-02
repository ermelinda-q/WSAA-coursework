import mysql.connector

class studentDAO:
    host = ""
    user = ""
    password = ""
    database = ""
    
    connection = ""
    cursor = ""
    
    def __init__(self):
        # this should be read from a config file
        self.host = "localhost"
        self.user = "root"
        self.password = "xxxxxxxxx
        self.database = "wsaa"
    
    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
        
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
        
    def getAll(self):
        cursor = self.get_cursor()
        sql = "select * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        studentlist = []
        for row in result:
            studentlist.append(self.convertToDict(row))
        self.closeAll()
        return studentlist
    
    def findById(self, id):
        cursor = self.get_cursor()
        sql = "select * from student where id = %s"
        values = (id,)
        
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)
    
    def create(self, student):
        cursor = self.get_cursor()
        sql = "insert into student (name, age) values (%s, %s)"
        values = (student.get("name"), student.get("age"))
        cursor.execute(sql, values)
        
        self.connection.commit()
        newid = cursor.lastrowid
        student["id"] = newid
        self.closeAll()
        return student
    
    def update(self, id, student):
        cursor = self.get_cursor()
        sql = "update student set name = %s, age=%s, where id =%s"
        
        values = (student.get("name"), student.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        
        self.closeAll()
        return student
    
    def delete(self, id):
        cursor = self.get_cursor()
        sql = "delete from student where id = %s"
        values = (id,)
        
        cursor.execute(sql, values)
        
        self.connection.commit()
        self.closeAll()
        return True
    def convertToDict(self, resultline):
        studentKeys = ["id", "name", "age"]
        currentKey = 0
        student ={}
        for atttrib in resultline:
            student[studentKeys[currentKey]] = atttrib
            currentKey = currentKey + 1
        return student
studentDAO = studentDAO()
    