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

ans = [-10 for j in range(N+1)]

answer = []

for i in range(3*N):
    if ans[A[i]] == -1:
        ans[A[i]] = i
        answer.append(A[i])
    if ans[A[i]] == -10:
        ans[A[i]] = -1


#ans = sorted(range(len(ans)), key=lambda x: ans[x])
#print(*ans[1:])
print(*answer)

