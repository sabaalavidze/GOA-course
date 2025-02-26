# Output numbers from 1 to 10 using a for loop
for num in range(1, 11):
    print(num)

# Output numbers from 5 to 25 using a for loop
for num in range(5, 26):
    print(num)

# Output numbers from 10 to 100 in steps of 5 using a for loop
for num in range(10, 101, 5):
    print(num)

# Ask the user to enter any word
word = input("Enter a word: ")

# Output only the letters 'A' from the word (case insensitive)
a_letters = [letter for letter in word if letter.upper() == 'A']
print("".join(a_letters))

# Commenting on the logical expression
# True or True and False or True and False and False and True or False
# The expression evaluates as follows:
# True or (True and False) or (True and False and False and True) or False
# True or False or False or False
# True or False
# True
# Final output: True