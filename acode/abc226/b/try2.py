from collections import defaultdict
N = int(input())
cnt = 0
#arr = defaultdict([])
a = set()
for i in range(N):
    L = list(map(int, input().split()))
    a.add(tuple(L))

print(len(a))



