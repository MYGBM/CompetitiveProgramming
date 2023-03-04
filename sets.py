#input
N=input()
line1=input().split()
for i in range(int(N)):
    set1=set(map(int,line1))
    
M=input()
line2=input().split()
for i in range(int(M)):
    set2=set(map(int,line2))
    
#logic
union=set1.union(set2)
intersect=set1.intersection(set2)
#symmetric difference
difference=union.difference(intersect)
#sort the symmetric difference
sorted_difference=sorted(difference)
print(sorted_difference)

#Output print all numbers in the set

for _ in sorted_difference:
    print(_)
    

