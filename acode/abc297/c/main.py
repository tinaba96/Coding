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


H, W = list(map(int, input().split()))
ans = []

for h in range(H):
    S = list(str(input()))
    for s in range(1, W):
        if S[s-1] == 'T' and S[s] == 'T':
            S[s-1] = 'P'
            S[s] = 'C'
    ans.append(S)

for a in ans:
    print(''.join(a))







