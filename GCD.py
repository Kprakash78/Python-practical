def gcd(a,b):
       while b!=0:
              a,b=b,a%b
       return a

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))

print(f"The GCD of the two numbers is:{gcd(num1,num2)}")