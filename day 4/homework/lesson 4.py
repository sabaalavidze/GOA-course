# 1) Determine if the user should go to kindergarten, school, or work
age = int(input("Enter your age: "))
if age > 2 and age < 6:
    print("Kindergarten")
elif age >= 6 and age < 18:
    print("School")
else:
    print("Work")

# 2) Check which programming academy the user attends
academy = input("Enter the programming academy you go to: ")
if academy.lower() == "goa":
    print("U r a real chad!")
else:
    print("Join Goa, become a chad")
    
    # 3) Determine grade based on project score
score = int(input("Enter your project score: "))
if score > 90:
    grade = "A"
elif score > 75:
    grade = "B"
elif score > 60:
    grade = "C"
elif score > 50:
    grade = "D"
elif score > 40:
    grade = "E"
elif score > 30:
    grade = "F"
else:
    grade = "Fail"

print("Your grade is:", grade)