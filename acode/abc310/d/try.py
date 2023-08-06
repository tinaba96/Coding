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

import itertools




N, T, M = list(map(int, input().split()))
mp = [[] for i in range(N+1)]

for i in range(M):
    A, B = list(map(int, input().split()))
    mp[A].append(B)
    mp[B].append(A)

l = []
for i in range(N):
    l.append(i+1)

cases = list(itertools.combinations(l, T))


visit = [0 for i in range(N+1)]

cnt = 0

def solv(vi, q):
    global cnt
    if len(q) == 0:
        return
    v = q.pop()
    if sum(vi) == N:
        cnt += 1
        return
    for i in range(1, N+1):
        if visit[i] == 1:
            continue
        if i != v and i not in mp[v]: # you have to check all the team member (not only v)
            visit[i] = 1
            q.append(i)
            #solv(vi, q)
            solv(visit, q)
            visit[i] = 0
    return


for c in cases:  # o(nCt) -> 10C5 = 252
    visit = [0 for i in range(N+1)]
    for i in c:
        visit[i] = 1
    solv(visit, list(c))
    '''
    for e in itertools.permutations(c): # O(T!) -> 10! = 3628800
        e = list(e)
        solv(visit, e)
    '''


print(cnt)

# we should also keep the data that which player is in which team in order to find "dislike" relations mp

# this implementation is BFS and not DFS. Therefore we miss some cases (ex. most of the players are in one team)
# simple DFS would count duplicate cases: 2->3->5->4 is same as 2->5->4->3    aproximately O(N!)

# BFS will provide players to each teams equally and DFS will provide most of the players to one team.
# this implementation will not consider the case between those cases.


