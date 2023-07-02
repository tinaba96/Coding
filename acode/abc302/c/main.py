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
import itertools

N, M = list(map(int, input().split()))

mp = []

for i in range(N):
    S = str(input())
    mp.append(S)

ans = 'No'

for v in itertools.permutations(mp):
    flag = True
    for n in range(N):
        if n+1 == N:
            if flag == True:
                #print(v, n)
                ans = 'Yes'
            break
        cnt = 0
        for m in range(M):
            if v[n][m] != v[n+1][m]:
                cnt += 1
        #print(cnt)
        if cnt != 1:
            flag = False
            break



print(ans)

