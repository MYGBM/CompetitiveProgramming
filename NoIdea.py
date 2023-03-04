happiness=0
input()
array=input().split()
set1=set(input().split())
set2=set(input().split())
for i in array:
    if i in set1:
     happiness+=1
    elif i in set2:
     happiness-=1
    happiness+=0
print(happiness)