print("Hello, Fukcer!")

A = "Hello"
B = "Fucket"
C = " "
D = "!"
result = A + C + B + 3 * D
print(result)

A = "Hello Fucker!!!"
length = len(A)
print("Length of A: ", length)

upper = A.upper()
lower = A.lower()
print("UPPER: ", upper)
print("LOWER: ", lower)

B = A.replace("Fucker","Motherfucker")
print(B)

C = A.split( )
print("Split Result: ",C)
print(C[0])
print(C[1])
print(A.split( )[0])
print(A.split( )[1])

# List is mutable but taple is not
# List -> [], Taple -> ()
servers = ["192.182.1.1", "192.182.1.2"]
print("Servers:", servers)
servers.append("192.182.1.3")
print("Extended Servers:", servers)

db_config = ("localhost", 5432, "admin", "password")
print("Data Base:", db_config)

# Sets -> {}
# Unordered unique items (No dublicate)
# Add or remove is possible but modify not
fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)
fruits = {"apple", "banana", "cherry", True, 1, 2}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)

# Dictionary unordered collection of key-value pairs -> {}
# Mutable
# Keys are unique and immutable
employee = {
    "name": "XXXXX",
    "age": "YY",
    "position": "ZZZZZZ",
    "salary": "QQQQ"
}
print("Employee Name:", employee["name"])
employee["departmant"] = "WWWWW"
print("Employee Department:", employee["departmant"])
print(employee)