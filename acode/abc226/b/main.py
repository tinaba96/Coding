from collections import defaultdict
N = int(input())
cnt = 0
#arr = defaultdict([])
a = [[] for i in range(N+1)]
for i in range(N):
    L = list(map(int, input().split()))
    #print(a[L[0]])
    if L in a[L[0]]:
            cnt += 1
    else:
        a[L[0]].append(L)

print(N-cnt)




