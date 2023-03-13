from itertools import combinations
line=input().split()
iterable,r=sorted(line[0]), int(line[1])
for i in range(1,r+1):
    value=list(combinations(iterable,i))
    for val in value:
        print(''.join(val))
        
