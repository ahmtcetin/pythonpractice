# Create dictionary
employee = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(employee)

# Access a value using a key
print("Employee Name:", employee["name"])

# Add a new key-value pair to the dictionary
employee["profession"] = "Engineer"
print(employee)

# Update the value of an existing key
employee["age"] = 26
print(employee)

# Delete a key-value pair from the dictionary
del employee["city"]
print(employee)