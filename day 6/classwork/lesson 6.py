# 5! = 1*2*3*4*5
num = int(input("please input a number: ")) #5
result= 1
for i in range (1 , num+1):
    result *= i #result = result *i
    print(i, result)

s = input('input please: ') #Hello
res = ''
for i in s:
        res = i + res
        print(res)

#classwork
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Your number is not a prime")
            break
    else:
        print("Your number is a prime")
else:
    print("Your number is not a prime")