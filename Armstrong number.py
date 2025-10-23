def armstrong(a):
              b=0
              length = len(str(a))
              for x in str(a):
                     b = b + pow(int(x),length)
              if(a==b):
                      return "Armstrong"
              else:
                     return "Not Armstrong"
num = int(input("Enter the number:"))
print(f"The number is {armstrong(num)}")