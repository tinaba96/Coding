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
S = str(input())
C = list(map(int, input().split()))

mp = [[] for j in range(M+1)]
ans = [[] for j in range(N)]

for i in range(N):
    mp[C[i]].append(i) 

for m in range(M):
    l = len(mp[C[m]])
    mp[C[m]] = [mp[C[m]][-1]] + mp[C[m]][:l-1]

for i in range(1, M+1):
    v = mp[i]
    for a in range(len(v)):
        if a+1 == len(v):
            b = v[0]
        else:
            b = v[a+1]
        ans[b] = S[v[a]]
            
    #print(v)

print(''.join(ans))

