# Create List
numbers = [10, 20, 30, 40, 50]
print(numbers)
# Add a new member
numbers.append(60)
print(numbers)
# Remove third elemet
#numbers.remove(numbers[2])
numbers.pop(2)
print(numbers)
# Update the value of the second element
numbers[1] = 21
print(numbers)
# Print the list and its length
length = len(numbers)
print("List of numbers: ", numbers)
print("Length of list", length)
