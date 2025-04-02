from zstudentDAO import studentDAO

student = {
    "name":"Mark",
    "age": 31
}

# create
student = studentDAO.create(student)
studentid = student["id"]

# find by id
result = studentDAO.findById(studentid)
print("test create and find by id")
print(result)

# update
newstudentValues = {"name":"Fred", "age":18}
studentDAO.update(studentid, newstudentValues)
result = studentDAO.findById(studentid)
print("test update")
print(result)


# get all
print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

# delete
studentDAO.delete(studentid)

