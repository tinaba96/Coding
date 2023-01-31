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

cnt = 0

N, M = list(map(int, input().split()))

arr = []

for i in range(N):
    s = str(input())
    arr.append(s[3:])

d = set()

for j in range(M):
    s = str(input())
    d.add(s)
    
for e in arr:
    if e in d:
        cnt += 1

print(cnt)
