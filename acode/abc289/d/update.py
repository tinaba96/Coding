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
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

X = int(input())

mp = [0 for i in range(X+1)]

for b in B:
    mp[b] = -1

'''
for e in A:
    if e > X:
        continue
    if mp[e] == -1:
        continue
    else:
        mp[e] = 1
A.sort()
#print(A)
'''
mp[0] = 1

for j in range(X+1):
    if mp[j] == 1:
        for next in A:
            if j+next > X:
                break
            if mp[j+next] == -1:
                continue
            else:
                mp[j+next] = 1

if mp[X] == 1:
    print('Yes')
else:
    print('No')

# O(N^2)?? -> O(NX) N = 10
