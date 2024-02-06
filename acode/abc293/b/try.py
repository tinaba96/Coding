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


K = int(input())
X = list(map(int, input().split()))

sX = set()
for i in range(K):
    sX.add(i+1)

for i in range(K):
    if i+1 in sX and X[i] in sX:
        sX.remove(X[i])


ans = list(sX)

ans.sort()

print(len(ans))
print(*ans)



