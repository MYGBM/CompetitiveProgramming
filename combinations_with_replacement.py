from itertools import combinations_with_replacement
line=input().split()
iterable=sorted(line[0])
r=int(line[1])

val=list(combinations_with_replacement(iterable,r))
for i in val:
    print(''.join(i))