""" 
    Title: pytech_update.py
    Author: James Smith
    Date: 4/18/2021
    Assignment: Module 6.2 Find and update Statements
"""

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.7qjgy.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#short-hand for students collection
students = db.students

#Construct Student List through find statement
docs = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --") #Code borrowed from solution for styling
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n") #Code borrowed from solution for styling


# John Doe data document
john = {
      "student_id": "1010",
      "first_name": "John",
      "last_name": "Doe",

      "enrollments": [
         {
            "term": "SP20",
            "student_id": "1010",
            "gpa": "4.0",
            "start_date": "3/11/2021",
            "end_date": "5/27/2021",
            
            "courses": [
               {
                  "course_id": "INFO_1010",
                  "term": "SP20",
                  "student_id": "1010",
                  "description": "Intro to computer basics.",
                  "instructor": "Daniel Wilwerding",
                  "grade": "A"
               },
               {
                  "course_id": "INFO_1020",
                  "term": "SP20",
                  "student_id": "1010",
                  "description": "Intro to programming logic.",
                  "instructor": "Denise Bishop",
                  "grade": "A"
               }
            ]
         }]
}

#All code below was borrowed from solution for styling
# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Doe into the students collection with document_id " + str(john_student_id))

#find a student document with the find_one statement using student_id
john = students.find_one({"student_id": "1010"})
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + john["student_id"] + "\n  First Name: " + john["first_name"] + "\n  Last Name: " + john["last_name"] + "\n") #Code borrowed from solution for styling

# call the delete_one method to remove the student_test_doc
students.delete_one({"student_id": "1010"})

#Construct a new Student List through find statement after the insertion and deletion of a document
new_docs = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --") #Code borrowed from solution for styling
for doc in new_docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n") #Code borrowed from solution for styling

input("\n\n  End of program, press any key to exit... ") #Code borrowed from solution for styling