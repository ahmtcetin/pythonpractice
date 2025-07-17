age = 30
height = 170
name = "Jake"
is_student = False

print("name: ", name)
print("age: ", age)
print("height: ", height)
print("is_student: ", is_student)

global_var = 5

print(global_var)


def print_global_variables():
    print(global_var)

def modify_global_variable():
    global_var = 10
    print(global_var)

print_global_variables()
modify_global_variable()