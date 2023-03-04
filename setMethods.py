N=int(input())
line=input().split() # 3 4 5 6 becomes ['3','4','5','6']
my_set=set(map(int,line)) # now {3,4,5,6}
M=int(input()) # number of commands
for command in range(M):
    cmd=input().split() #['remove','4']
    
    if cmd[0]=='pop':
        my_set.pop()
    elif cmd[0]=='remove':
         my_set.remove(int(cmd[1]))
    elif cmd[0]=='discard':
        my_set.discard(int(cmd[1]))
print(sum(my_set))



