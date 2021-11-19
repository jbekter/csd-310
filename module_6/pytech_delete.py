#Josh Boettcher - module 6.3
#Used Professor Krasso's code in Github as reference

from pymongo import MongoClient

#my MongoDB url
url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/test"

#connection to MongoDB cluster
client = MongoClient(url)

#connection to pytech database
db = client.pytech

students = db.students

#Call the find() method and display the results to the terminal window
student_list = db.students.find({})
print("The following students were found with the find query")
print("_____________________________________________________")
for student in student_list:
    print("\nStudent ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"])

#Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010
db.students.insert_one( { "student_id": "1010", "first_name": "Billy", "last_name": "McDonald" } );

#Call the find_one() method and display the results to the terminal window
student1010 = students.find_one({"student_id": "1010"})
print("\nThe following is a print out of student 1010")
print("_____________________________________________________")
print("\nStudent ID: " + student1010["student_id"] + "\nFirst Name: " + student1010["first_name"] + "\nLast Name: " + student1010["last_name"])

#Call the delete_one() method by student_id 1010
db.students.delete_one( { "student_id": "1010" } );

#Call the find() method and display the results to the terminal window
student_list = db.students.find({})
print("\nThe following students were found with the find query")
print("_____________________________________________________")
for student in student_list:
    print("\nStudent ID: " + student["student_id"] + "\nFirst Name: " + student["first_name"] + "\nLast Name: " + student["last_name"])
