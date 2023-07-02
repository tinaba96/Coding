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


N, M, H, K = list(map(int, input().split()))
S = str(input())

item = set()

R = (1, 0)
L = (-1, 0)
U = (0, 1)
D = (0, -1)

for m in range(M):
    x, y = list(map(int, input().split()))
    item.add((x, y))


x = 0
y = 0

for i in range(N):
        
    if S[i] == 'R':
        x += 1
    if S[i] == 'L':
        x -= 1
    if S[i] == 'U':
        y += 1
    if S[i] == 'D':
        y -= 1

    H -= 1

    if H == -1:
        print('No')
        exit()

    if (x,y) in item:
        if H < K:
            item.remove((x,y))
        H = max(K, H)


print('Yes')

