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

A = []
B = []
C = []

a = ''
b = ''
x = ''

Ha, Wa = list(map(int, input().split()))
for i in range(Ha):
    A = str(input())
    for j in range(Wa):
        if A[j] == '.':
            a += '0'
        else:
            a += '1'

Hb, Wb = list(map(int, input().split()))
for i in range(Hb):
    B = str(input())
    for j in range(Wb):
        if B[j] == '.':
            b += '0'
        else:
            b += '1'

Hx, Wx = list(map(int, input().split()))
for i in range(Hx):
    X = str(input())
    for j in range(Wx):
        if X[j] == '.':
            x += '0'
        else:
            x += '1'

ans = 'No'

print(a)
print(b)
print(x)


# for binary solution, see ans3.py

