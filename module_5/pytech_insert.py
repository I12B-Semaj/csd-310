""" 
    Title: pytech_insert.py
    Author: James Smith
    Date: 4/10/2021
    Assignment: Module 5.3 Insert Statements
"""

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7qjgy.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Joe Watson data document
joe = {
      "student_id": "1007",
      "first_name": "Joe",
      "last_name": "Watson",

      "enrollments": [
         {
            "term": "SP20",
            "student_id": "1007",
            "gpa": "4.0",
            "start_date": "3/11/2021",
            "end_date": "5/27/2021",
            
            "courses": [
               {
                  "course_id": "INFO_1010",
                  "term": "SP20",
                  "student_id": "1007",
                  "description": "Intro to computer basics.",
                  "instructor": "Daniel Wilwerding",
                  "grade": "A+"
               },
               {
                  "course_id": "INFO_1020",
                  "term": "SP20",
                  "student_id": "1007",
                  "description": "Intro to programming logic.",
                  "instructor": "Denise Bishop",
                  "grade": "A+"
               }
            ]
         }]
}

# Dan Jackson data document
dan = {
      "student_id": "1008",
      "first_name": "Dan",
      "last_name": "Jackson",

      "enrollments": [
         {
            "term": "SP20",
            "student_id": "1008",
            "gpa": "3.52",
            "start_date": "3/11/2021",
            "end_date": "5/27/2021",
            
            "courses": [
               {
                  "course_id": "INFO_1010",
                  "term": "SP20",
                  "student_id": "1008",
                  "description": "Intro to computer basics.",
                  "instructor": "Daniel Wilwerding",
                  "grade": "B+"
               },
               {
                  "course_id": "INFO_1020",
                  "term": "SP20",
                  "student_id": "1008",
                  "description": "Intro to programming logic.",
                  "instructor": "Denise Bishop",
                  "grade": "A-"
               }
            ]
         }]
}

# Josh Smith data document
josh = {
      "student_id": "1009",
      "first_name": "Josh",
      "last_name": "Smith",

      "enrollments": [
         {
            "term": "SP20",
            "student_id": "1009",
            "gpa": "2.5",
            "start_date": "3/11/2021",
            "end_date": "5/27/2021",
            
            "courses": [
               {
                  "course_id": "INFO_1010",
                  "term": "SP20",
                  "student_id": "1009",
                  "description": "Intro to computer basics.",
                  "instructor": "Daniel Wilwerding",
                  "grade": "C"
               },
               {
                  "course_id": "INFO_1020",
                  "term": "SP20",
                  "student_id": "1009",
                  "description": "Intro to programming logic.",
                  "instructor": "Denise Bishop",
                  "grade": "B"
               }
            ]
         }]
}

# get the students collection
students = db.students

#All code below was borrowed from solution for styling
# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
joe_student_id = students.insert_one(joe).inserted_id
print("  Inserted student record Joe Watson into the students collection with document_id " + str(joe_student_id))

dan_student_id = students.insert_one(dan).inserted_id
print("  Inserted student record Dan Jackson into the students collection with document_id " + str(dan_student_id))

josh_student_id = students.insert_one(josh).inserted_id
print("  Inserted student record Josh Smith into the students collection with document_id " + str(josh_student_id))

input("\n\n  End of program, press any key to exit... ")