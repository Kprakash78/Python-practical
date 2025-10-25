class student:
       def __init__(self,name,college_name,branch,roll_num):
              self.name=name
              self.college_name=college_name
              self.branch=branch
              self.roll_num=roll_num

       def info(self):
              print(f"Name:{self.name}")
              print(f"College name:{self.college_name}")
              print(f"Branch:{self.branch}")
              print(f"Roll number:{self.roll_num}")

std1=student("Kshiteej","USAR","AIML",1312345)
std1.info()