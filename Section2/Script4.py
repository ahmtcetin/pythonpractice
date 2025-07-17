user_input = int(input("Welcome to the Grade Calculator! Please enter your score (0-100): "))

if (user_input <= 59) and (user_input >= 0):
    print("F")
elif user_input <= 69:
    print("D")
elif user_input <= 79:
    print("C")
elif user_input <= 89:
    print("B")
elif user_input <= 100:
    print("A")
else:
    print("Inpu is out of range!")