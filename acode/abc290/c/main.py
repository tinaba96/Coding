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
A = list(map(int, input().split()))
A = list(set(A))
A.sort()
ans = 0
#print(A)

for i in range(min(len(A), K)):
    if i == A[i]:
        ans += 1
        continue
    else:
        print(ans)
        exit()
print(ans)
