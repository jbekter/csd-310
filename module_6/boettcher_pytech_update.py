#Josh Boettcher - module 6
#Used Professor Krasso's code in Github as reference

from pymongo import MongoClient

#my MongoDB url
url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/test"

#connection to MongoDB cluster
client = MongoClient(url)

#connection to pytech database
db = client.pytech

students = db.students

#find students
student_list = db.students.find({})

#print list of students found by query
print("The following students were found with the find query")
print("_____________________________________________________")
for student in student_list:
    print("\nStudent ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"])

#update last name of student 1007
new_name = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bobolobolonokis"}})

#find student 1007
student1007 = students.find_one({"student_id": "1007"})

#print student 1007
print("\nThe following is a print out of student 1007")
print("_____________________________________________________")
print("\nStudent ID: " + student1007["student_id"] + "\nFirst Name: " + student1007["first_name"] + "\nLast Name: " + student1007["last_name"])