import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
d = defaultdict(int)


N, K = list(map(int, input().split()))

v = 0
step = []

for i in range(N):
    a, b = list(map(int, input().split()))
    v += b

    d[a] += b
    step.append(a)


ans = 1

#print(d)
#print(v)
s = set(step)

step2 = list(s)

lis = sorted(step2)
#print(lis)
if v <= K:
    print(ans)
    exit()

prev = 0
for i in lis:
    v -= d[i]
    day = i - prev
    ans += day
    prev = i
    if v <= K:
        break

print(ans)

