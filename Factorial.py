# def factorial(a):
#        if(a==0):
#               return 1
#        else:
#               return a*factorial(a-1)
def factorial(a):
       b=1
       for x in range(a,1,-1):
              b = b*x
       return b

num = int(input("Enter the number:"))
print(f"The factorial of the number is:{factorial(num)}")
