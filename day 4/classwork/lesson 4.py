# 1) Ask the user to enter a number. If it is even, print "even", and if it is odd, print "odd".
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

# 2) Check whether the number entered is negative, positive or 0. Set res accordingly.
if num > 0:
    res = 1
elif num < 0:
    res = -1
else:
    res = 0
print("The result is:", res)

# 3) Compare two numbers (14 and 17) and print the largest one.
num1, num2 = 14, 17
largest_num = max(num1, num2)
print("The largest number is:", largest_num)  # Output: 17

# 4) Number is set to 27 and checked for divisibility by 5.
num_div5 = 27
output_num = num_div5 if num_div5 % 5 == 0 else 0
print("Output:", output_num)  # Output: 05

# 5) Check if the entered number is a new century number (e.g., 100, 200, ..., 2000)
century_num = int(input("Enter a number to check for a new century: "))
if century_num % 100 == 0:
    print("New Century")
else:
    print("Not a New Century")