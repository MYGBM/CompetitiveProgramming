if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr=sorted(arr)
    newArr=newArr[::-1]
    maxi=max(newArr)
    for i in newArr:
        if i<maxi:
            maxi=i
            break
    print(maxi)
