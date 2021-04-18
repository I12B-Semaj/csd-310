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


#Update a record within the students collection by using student_id
db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Danielson"}})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --") #Code borrowed from solution for styling

#find a student document with the find_one statement using student_id
joe = students.find_one({"student_id": "1007"})
print("  Student ID: " + joe["student_id"] + "\n  First Name: " + joe["first_name"] + "\n  Last Name: " + joe["last_name"] + "\n") #Code borrowed from solution for styling

input("\n\n  End of program, press any key to exit... ") #Code borrowed from solution for styling