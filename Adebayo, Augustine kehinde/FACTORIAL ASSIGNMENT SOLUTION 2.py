NUMBER = int(raw_input('enter the number you want to find the factorial:'))
RESULT = 1
COUNTER = 1
while(COUNTER <= NUMBER):
    ANSWER *= COUNTER 
    COUNTER +=1
    
print('the factorial of',NUMBER,'is',ANSWER)

