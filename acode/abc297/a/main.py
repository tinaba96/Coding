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


N, D = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = -1

s = -10**18

for i in T:
    if i-s <= D:
        print(i)
        exit()
    s = i

print(ans)


