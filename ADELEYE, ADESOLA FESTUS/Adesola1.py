"""  Program to solve for Factorial
     Name:ADELEYE ADESOLA FESTUS
     Matric number:EEE/2011/0041
     Course:EEE512 Assignment I
     program to find the factorial of any number provided by the user."""

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("factorial for a negative number?")
elif num == 0:
    print("the factorial for 0 is 1")

else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(" The factorial of",num,"is",factorial)
