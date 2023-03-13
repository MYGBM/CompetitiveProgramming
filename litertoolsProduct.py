from itertools import product
M=list(map(int,input().split()))
N=list(map(int,input().split()))

# prints a list of tuples
# print(list(product(M,N)))
#To get tuples separated by comma - use unpack operator *
print(*list(product(M,N)))


