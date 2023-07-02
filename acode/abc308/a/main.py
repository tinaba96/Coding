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


S = list(map(int, input().split()))

ans = 'Yes'
prev = 0

for i in S:
    if i%25 != 0 or i > 675 or 100 > i or prev > i:
        ans = 'No'
    prev = i

print(ans)

