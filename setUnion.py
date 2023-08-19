set1=set()
set2=set()
input()
m=list(map(int,input().split()))
input()
n=list(map(int,input().split()))
for i in n:
    set1.add(i)
for i in m:
    set2.add(i)
union=set1.union(set2)
print(len(union))