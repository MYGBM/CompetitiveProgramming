from itertools import combinations
line=input().split()
s=sorted(line[0])
keyy=int(line[1])
for i in range(1,keyy+1):
    x=list(combinations(s,i))
    for val in x:
        print(''.join(val))