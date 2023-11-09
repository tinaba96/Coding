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

y =  []
for i in range(1, 10):
    if N % i == 0:
        y.append(i)

#print(y)

ans = ''
for i in range(N+1):
    flg = False
    for e in y:
        if i % (N//e) == 0:
            ans += str(e)
            flg = True
            break
    if flg == False:
        ans += '-'

print(ans)
            

# see the video editorial for the reference
