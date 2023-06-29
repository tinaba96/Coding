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

strN = str(N)
l = len(strN)

if l <= 3:
    print(N)
if l == 4:
    print('{:0<{}}'.format(strN[:l-1], l))
if l == 5:
    print('{:0<{}}'.format(strN[:l-2], l))
if l == 6:
    #print(strN[:l-3])
    print('{:0<{}}'.format(strN[:l-3], l))
if l == 7:
    print('{:0<{}}'.format(strN[:l-4], l))
if l == 8:
    print('{:0<{}}'.format(strN[:l-5], l))
if l >= 9:
    print('{:0<{}}'.format(strN[:l-6], l))


