from collections import defaultdict
N = int(input())
cnt = 0
#arr = defaultdict([])
a = set()
for i in range(N):
    L = list(map(int, input().split()))
    #print(a[L[0]])
    if L in list(a):
            cnt += 1
    else:
        a.add(list(L))

print(N-cnt)




