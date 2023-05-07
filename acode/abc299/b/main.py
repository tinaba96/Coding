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


N, T = list(map(int, input().split()))
C = list(map(int, input().split()))
R = list(map(int, input().split()))

color = C[0]
if T in C:
    color = T

win = 0
for i in range(N):
    if color == C[i]:
        if R[i] > win:
            win = R[i]
            ans = i + 1


print(ans)

# you can also use points for 3 different color and use pair() to compare one by one like the video editorial
'''
3 different color
1. T
2. C[0]
3. others
'''


