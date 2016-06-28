#xWhile loop for finding factorial

number = int(raw_input("Enter the value you want to find the factorial : "))
answer = 1
counter = 1
while ( counter <= number):
    answer *= counter
    counter +=1
print ("The factorial of ", number , " is " , answer)



# Finding factorial using for loops
number = int(raw_input("Enter the value you want to find the factorial : "))
answer = 1
for factorial in range(1,number+1,1):
    answer *= factorial
print ("The factorial of ", number , " is " , answer)


    
    


