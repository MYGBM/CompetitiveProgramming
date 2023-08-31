from collections import Counter
N=int(input())
words=[]
for i in range(N):
    words.extend(input().split())
counter_words=Counter(words)
print(len(counter_words.keys()))
print(*counter_words.values())