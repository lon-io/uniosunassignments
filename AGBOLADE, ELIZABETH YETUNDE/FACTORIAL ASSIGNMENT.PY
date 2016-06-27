#program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("factorial for a negative number?")
elif num == 0:
    print("the factorial for 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("factorial of",num,"is",factorial)
