import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

s = sum(A)

T %= s

cum = [0]
tmp = 0
for i in A:
    cum.append(tmp+i)
    tmp += i

#print(cum)

import bisect

pos = bisect.bisect(cum, T)

#print(pos)

print(pos, T-cum[pos-1])



