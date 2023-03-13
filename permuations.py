from itertools import permutations
line=input().split()
s=sorted(line[0])
keyy=int(line[1])
# print(*list(map(''.join,permutations(s,keyy))),sep='\n')
val=list(permutations(s,keyy))
for i in val:
    print(''.join(i))

