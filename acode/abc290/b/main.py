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


N, K = list(map(int, input().split()))

S = str(input())

cnt = 0
ans = ''

for i in range(N):
    if cnt < K and S[i] == 'o':
        ans += 'o'
        cnt += 1
    else:
        ans += 'x'
        continue

print(ans)


