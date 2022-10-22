import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

import copy

N = int(input())
A = list(map(int, input().split()))

B = copy.copy(A)
B.sort()

#print(B)

h = set(A)

mp = {}

ind = 0
for i in range(len(B)):
    if i > 0 and B[i] == B[i-1]:
        continue
    
    if len(h) - 1 - ind < 0:
        mp[B[i]] = 0
    mp[B[i]] = len(h) - 1 - ind
    ind += 1

#print(mp)

#for g in A:
    #print(mp[g])

ans = [0 for i in range(N)]

for a in B:
    ans[mp[a]] += 1

for l in ans:
    print(l)
