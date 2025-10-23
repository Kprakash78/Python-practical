num = [i for i in range(0,15,2)]
for x in num:
       print(x)
num2=int(input("Enter the position of the number to be removed:"))
num.pop(num2-1)
print(num)
