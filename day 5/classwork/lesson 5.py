for num in range(2, 26):  # Loop through numbers from 2 to 25
    if num % 2 != 0:      # Check if the number is odd
        print(num)        # Print the odd number
# Get user input for name
name = input("Enter your name: ")

# Loop through each letter in the name and print it
for letter in name:
    print(letter)

# Set a correct password
correct_password = "sunsula"

# Prompt user to enter a password until it matches correct_password
while True:
    user_password = input("Enter the password: ")
    if user_password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password, try again.")