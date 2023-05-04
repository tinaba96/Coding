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

left = 0
right = N
while True:
    if abs(left-right) <= 1:
        break
    m = (left+right)//2
    print('?', m)
    a = int(input())
    if a == 0:
        left = m
    else:
        right = m

print('!', left)
exit()


