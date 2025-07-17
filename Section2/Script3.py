student = {
    "name": "Ahmet",
    "age": 30,
    "major": "Embedded Coding"
}

print("Name: ", student["name"])
print("Age: ", student["age"])
print("Major: ", student["major"])

student["gpa"] = 3.15
student["age"] = student["age"] + 1

print("Name: ", student["name"])
print("Age: ", student["age"])
print("Major: ", student["major"])
print("GPA: ", student["gpa"])

for keys in student.keys():
    print(f"{keys} is {student[keys]}")