def Factorial(n):
     num = 1
     if n == 0:
         num = 1
     else:
         for i in range(n):
             i += 1
             num *= i
     print (num)

 if __name__ == "__main__":
     Factorial(100)
