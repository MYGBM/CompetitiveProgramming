setA = set(map(int, input().split()))
N = int(input())

is_superset = True

for _ in range(N):
    setBC = set(map(int, input().split()))
    if not setA.issuperset(setBC):
        is_superset = False
        break

print(is_superset)