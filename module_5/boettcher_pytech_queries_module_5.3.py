from pymongo import MongoClient

#my MongoDB url
url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/test"

#connection to MongoDB cluster
client = MongoClient(url)

#connection to pytech database
db = client.pytech

students = db.students

#find students
students = db.students.find({})

#find and print list of all students
print("\nThis is an example of pulling all student records from the database: ")
for student in students:
    print("\n\tStudent ID: " + student["student_id"] + "\n\tFirst Name: " + student["first_name"] + "\n\tLast Name: " + student["last_name"])

#find and print one student
student1 = db.students.find_one({'student_id': "596"})
print("\nThis is an example of pulling one student record from the database: ")
print("\n\tStudent ID: " + student1["student_id"] + "\n\tFirst Name: " + student1["first_name"] + "\n\tLast Name: " + student1["last_name"])