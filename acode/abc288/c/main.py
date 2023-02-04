import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N, M = list(map(int, input().split()))

link = [[] for _ in range(N+1)]

for i in range(M):
    A, B = list(map(int, input().split()))
    link[A].append(B)
    link[B].append(A)



seen = [-1 for m in range(N+1)]

ans = 0

def dfs(n):
    global ans
    for e in link[n]:
        if seen[e] != 1:
            seen[e] = 1
            dfs(e)
        else:
            ans += 1
        seen[e] == 0


for a in range(N):
    if seen[a] == -1:
        dfs(a)
        seen[a] = 0

print(ans)





