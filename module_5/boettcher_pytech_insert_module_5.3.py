
from pymongo import MongoClient

#MongoDB url
url = "mongodb+srv://admin:admin@cluster0.qcdpi.mongodb.net/test"

#connect to MongoDBcluster 
client = MongoClient(url)

#connect pytech database
db = client.pytech

#insert 3 student names

josh = {
    "student_id": "1007",
    "first_name": "Josh",
    "last_name": "Boettcher",
    "enrollments": [
        {
            "term": "fall",
            "gpa": 4,
            "start_date": "10/14/2021",
            "end_date": "12/21/2021",
            "courses": [
                {
                    "course_id": "965",
                    "description": "Java",
                    "instructor": "Professor Payne",
                    "grade": "A"
                },
                {
                    "course_id": "978",
                    "description": "Database Development",
                    "instructor": "Professor Shelanskey",
                    "grade": "A"
                }
            ]
        }
    ]

}

jim = {
    "student_id": "1008",
    "first_name": "Jim",
    "last_name": "Gatkins",
    "enrollments": [
        {
            "term": "summer",
            "gpa": 3.8,
            "start_date": "7/1/2021",
            "end_date": "9/30/2021",
            "courses": [
                {
                    "course_id": "716",
                    "description": "Art History",
                    "instructor": "Professor Hawthorne",
                    "grade": "B"
                },
                {
                    "course_id": "768",
                    "description": "Painting",
                    "instructor": "Professor Mondo",
                    "grade": "A"
                }
            ]
        }
    ]
}

peter = {
    "student_id": "1009",
    "first_name": "Peter",
    "last_name": "Thomas",
    "enrollments": [
        {
            "term": "fall",
            "gpa": 3,
            "start_date": "10/14/2021",
            "end_date": "12/21/2021",
            "courses": [
                {
                    "course_id": "876",
                    "description": "Algebra",
                    "instructor": "Professor Smith",
                    "grade": "B"
                },
                {
                    "course_id": "950",
                    "description": "Stastics",
                    "instructor": "Professor Fielder",
                    "grade": "B"
                }
            ]
        }
    ]
}

#get student collections
students = db.students

josh_student_id = students.insert_one(josh).inserted_id
print("  Inserted student record Josh Boettcher into the students collection with document_id " + str(josh_student_id))

jim_student_id = students.insert_one(jim).inserted_id
print("  Inserted student record Jim Gatkins into the students collection with document_id " + str(jim_student_id))

peter_student_id = students.insert_one(peter).inserted_id
print("  Inserted student record Peter Thomas into the students collection with document_id " + str(peter_student_id))

