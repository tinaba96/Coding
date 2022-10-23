import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


A, B = list(map(int, input().split()))

from decimal import Decimal, ROUND_HALF_UP

A = Decimal(str(A))
B = Decimal(str(B))

C =  B / A
X = Decimal(str(C)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

print(X)

