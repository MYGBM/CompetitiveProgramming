input()
line1=input().split() 
set1=set(line1)
input()
line2=input().split() 
set2=set(line2)
set3=set1.union(set2)
counter=0
for _ in set3:
    counter+=1
print(counter)


