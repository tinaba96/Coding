import heapq
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


N, K, Q = list(map(int, input().split()))

A = [0 for k in range(N+1)]

hq = []
ans = 0
ma = set()

for q in range(2):
    X, Y = list(map(int, input().split()))
    A[X] = Y
    ma.add(X)
    hq.append(X)
    ans += Y
    print(ans)

heapq.heapify(hq)

for q in range(2, Q):
    X, Y = list(map(int, input().split()))
    old = heapq.heappop(hq)
    if old < Y:
        heapq.heappush(hq, Y)
        #ans += Y-old
    else:
        heapq.heappush(hq, old)

    if X in ma:


    
    A[X] = Y
    print(ans)


'''
using heapq, you can not remove the element.
so I thought I chould use set() but it is hard to keep the top K element using set()
it is hard to change the value that are already in heapq which is not minumun
'''


