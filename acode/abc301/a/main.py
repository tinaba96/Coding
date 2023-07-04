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
S = str(input())

A = 0
T = 0

S = list(S)

for i in S:
    if i == 'T':
        T += 1
    else:
        A += 1

if T > A:
    print('T')
    exit()
elif A > T:
    print('A')
    exit()


if S[-1] == 'T':
    print('A')
else:
    print('T')


