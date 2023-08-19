set1=set()
set2=set()
a=input()
n=list(map(int,input().split()))
b=input()
m=list(map(int,input().split()))
for i in n:
    set1.add(i)
for j in m:
    set2.add(j)
difference=set1.difference(set2)
print(len(difference))