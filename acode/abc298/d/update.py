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

from collections import deque


Q = int(input())
ans = 1
deq = deque()
deq.append(1)

for q in range(Q):
    x = list(map(int, input().split()))
    ans %= 998244353 # this is needed. otherwise, the ans will be too big to calculate
    #ans %= 998244353*998244353 # 多倍長ではないのでこれでもAC
    if x[0] == 1:
        deq.append(x[1])
        ans = 10*ans+x[1] # this is heavy if you don't take the mod every loop -> 10**(6*10**5) maximum 多倍長は思い　10**19(2**63)以下にするべき。
    if x[0] == 2:
        v = deq.popleft()
        ans -= v*pow(10, len(deq), 998244353)
    if x[0] == 3:
        print(ans%998244353)



