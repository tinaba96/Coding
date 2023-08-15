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

mp = []

N = int(input())
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    mp.append(A)

X = int(input())

ans = 100000

for i in range(N):
    if X in mp[i]:
        ans = min(ans, len(mp[i]))
answ = []
for j in range(N):
    if len(mp[j]) == ans and X in mp[j]:
        answ.append(j+1)
answ.sort()

if len(answ) == 0:
    print(0)
else:
    print(len(answ))
    print(*answ)



# 問題文確認
#  This was AC if spaces and newlines were ignored. Please use --ignore-spaces (-S) option or --ignore-spaces-and-newline (-N) option.
