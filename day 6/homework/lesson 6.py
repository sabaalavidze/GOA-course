num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1, 2):
    total += i

print("Sum of odd numbers:", total)


num = int(input("Enter a number: "))

print("Numbers divisible by", num, ":")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
    


attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == "sunsula":  # Replace "secret" with the actual correct password
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1

if attempts == 3:
    print("Too many incorrect attempts. Access denied!")



user_input = input("Enter a string: ")  # Ensure the variable is defined before using it

reversed_string = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_string += user_input[i]

print("Reversed string:", reversed_string)