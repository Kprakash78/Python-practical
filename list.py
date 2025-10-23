list1 = [1,2,3]
list2 = [2,3,4]
result=[]
for x in range(len(list1)):
       result.append(list1[x]+list2[x])

print(result)
print(f"Sorted list {sorted(list1)}")
print(f"Reversed list {list1[::-1]}")

