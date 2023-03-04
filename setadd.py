N=input()
my_set=set()
for i in range(int(N)):
    line=input()
    my_set.add(line)
count=0
for i in my_set:
    count+=1
print(count)


