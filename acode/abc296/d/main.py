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

import math


N, M = list(map(int, input().split()))

ans = -1

if N**2 < M:
    print(ans)
    exit()

start = int(math.sqrt(M))

v = start**2

while v < M:
    start += 1
    v = start**2

ans = v

left = start
right = start

#print('v: ', v)
#print('start: ', start)

#1
while True:
    left -= 1
    right += 1
    if right > N or left < 1:
        break
    val = left*right
    if val < M:
        break
    else:
        ans = min(ans, val)

#2
l = start
while True:
    l -= 1
    if l < 1:
        break
    va = l*start
    if va < M:
        break
    else:
        ans = min(ans, va)


print(ans)


# No.1, 2 will not cover everything.
'''
ex) if start = 8
#1 will check 7*9=63, 6*10=60, 5*11=55, ....
#2 will check 7*8=56, 6*8=48, ....
However,
you should check also
6*9=54, 5*9=45, 5*10=50, and so on
which takes a lot of time
'''
# approach of video tutorial is needed to have AC


