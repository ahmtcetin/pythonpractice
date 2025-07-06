# Prompt the user for their age and whether they have a valid driver’s license
user_age = int(input("Enter age: "))
user_license = input("Do you have a valid driver's license (Yes/No)? :")
if user_license == "Yes":
    isLicenseValid = True
elif user_license == "No":
    isLicenseValid = False
else:
    print("No valid response given for driver lcense !")

if (user_age >= 18) and (True == isLicenseValid):
    print("You can drive")
elif (user_age < 18):
    print("You are too young to drive")
elif (user_age >= 18) and (False == isLicenseValid):
    print("You cannot drive without a license")
else:
    print("Not proper inputs given")


can_drive = (user_age >= 18) and (True == isLicenseValid)
print("can_drive: ", can_drive)

if (user_age >= 18) and (True == isLicenseValid):
    userWantToDrive = input("Do you want to drive today (Yes/No)? :")