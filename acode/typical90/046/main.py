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
B = list(map(int, input().split()))
C = list(map(int, input().split()))


for i in range(N):
    A[i] %= 46
    sA = set(A)
    B[i] %= 46
    sB = set(B)
    C[i] %= 46
    sC = set(C)





'''
cntA = [0, 0] # 2, 23
cntB = [0, 0] # 2, 23
cntC = [0, 0] # 2, 23

for a in range(len(A)):
    if A[a] % 2 == 0:
        cntA[0] += 1
    elif A[a] % 23 == 0:
        cntA[1] += 1

for b in range(len(B)):
    if B[b] % 2 == 0:
        cntB[0] += 1
    elif B[b] % 23 == 0:
        cntB[1] += 1

for c in range(len(C)):
    if C[a] % 2 == 0:
        cntC[0] += 1
    elif C[a] % 23 == 0:
        cntC[1] += 1

ans = 0
#print(cntA)

ans += cntA[0]*cntB[1]*N
ans += cntA[1]*cntB[0]*N

ans += cntB[0]*cntC[1]*N
ans += cntB[1]*cntC[0]*N

ans += cntA[0]*cntC[1]*N
ans += cntA[1]*cntC[0]*N
'''

print(ans)
