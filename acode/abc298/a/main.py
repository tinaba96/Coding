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

flg1 = False
flg2 = True

for i in range(N):
    if S[i] == 'o':
        flg1 = True
    elif S[i] == 'x':
        flg2 = False

if flg1 and flg2:
    print('Yes')
else:
    print('No')


