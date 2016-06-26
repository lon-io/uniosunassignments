#Factorial Using For Loops


def Factorial(n):
    num = 1
    if n == 0:
        num = 1
    else:
        for i in range(1,(n+1)):
            num *= i
    print ("The factorial of " + str(n) + " is " + str(num))
if __name__ == "__main__":
    answer = input("Enter the number you want to find the factorial : ")
    Factorial(answer)
    

#Factorial Using  while Loops

def whileloops(n):
    answer = 1
    counter = 1
    if n == 0:
        num = 1
    else:
        while ( counter <= n):
            answer *= counter
            counter +=1
    print ("The factorial of " + str(n) + " is " + str(answer) )
if __name__ == "__main__":
    answer = input("Enter the number you want to find the factorial : ")
    whileloops(answer)
