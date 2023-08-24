if __name__ == '__main__':
    li=list()
    N = int(input())
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        if op=="append":
            li.append(int(cmd[1]))
        if op=="print":
            print(li)
        if op=="reverse":
            li.reverse()
        if op=="remove":
            li.remove(int(cmd[1]))
        if op=="insert":
            li.insert(int(cmd[1]),int(cmd[2]))
        if op=="sort":
            li.sort()
        if op=="pop":
            li.pop()