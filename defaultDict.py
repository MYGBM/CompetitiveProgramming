from collections import defaultdict
n,m=map(int,input().split())
groupA=defaultdict(list)
groupB=[]
for i in range(n):
    word=input()
    groupA[word].append(i+1)
for i in range(m):
    word=input()
    groupB.append(word)
for word in groupB:
    if word in groupA:
        print(*groupA[word])
    else:
        print(-1)
    