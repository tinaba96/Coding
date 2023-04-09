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


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

'''
for j in range(K):
    for a in range(N):
        A.append(A[a])

N = len(A)
'''

c = 2**N - 1
li = set()

heapq.heapify([])

for i in range(c):
    cost = 0
    for n in range(N):
        if i & (1<<n):
            cost += A[n]
    li.add(cost)


arr = list(li)
arr.sort()
#print(arr)
heapq.heapify(arr)

# heap 重複はどう扱ってる？

for k in range(K-1):
    heapq.heappop(arr)

ans = heapq.heappop(arr)

print(ans)




