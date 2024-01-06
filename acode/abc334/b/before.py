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


A, M, L, R = list(map(int, input().split()))

'''
# a < L
if (A < L):




left = max(0, a-L)
right = max(0, R-a)
'''

L -= A
R -= A

st = 0
en = 0
while True:
    if st == 0:
        if st*M < L:
            st += 1
            continue
        else:
            st *= M
            en = st
    else:
        if en*M <= R:
            en += 1
            continue
        else:
            en *= M

print(en-st)

