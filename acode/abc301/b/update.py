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


N = int(input())
A = list(map(int, input().split()))


ans = [A[0]]
i = 1

while True:
    if A[i] > ans[-1]:
        for a in range(A[i]-ans[-1]):
            ans.append(ans[-1]+1)
    if A[i] < ans[-1]:
        for a in range(ans[-1]-A[i]):
            ans.append(ans[-1]-1)
    i += 1
    if i == N:
        break


print(*ans)
