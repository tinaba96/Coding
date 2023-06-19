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


N, M, K = list(map(int, input().split()))

mp = [[] for i in range(N)]

for m in range(M):
    a, b = list(map(int, input().split()))
    mp[a].append(b)
    mp[b].append(a)

# if you do DFS or BFS for each N, it would be O(N^2)


