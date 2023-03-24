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

for h in range(H):
    A = list(map(int, input().split()))
    ans = []
    for w in range(W):
        if A[w] == 0:
            ans.append('.')
        else:
            ans.append(chr(65+A[w]-1))
    print(''.join(ans))


