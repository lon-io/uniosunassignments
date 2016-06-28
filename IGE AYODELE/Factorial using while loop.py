num = int(input("enter a number: "))
factorial = 1
if num < 0:
   print("factorial for a negative number? are you kidding me?")
elif num == 0:
   print("the factorial for 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("factorial of",num,"is" ,factorial)




