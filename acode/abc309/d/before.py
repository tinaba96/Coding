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


N1, N2, M = list(map(int, input().split()))


mp = [[] for i in range(N1+N2+1)]

for m in range(M):
    a, b = list(map(int, input().split()))
    mp[a].append(b)
    mp[b].append(a)


#print(mp)
ans1 = 0
ans2 = 0

#dfs

visit = [False for i in range(N1+N2+1)]
def dfs(i, node):
    global ans1
    ans1 = max(ans1, i)
    for n in node:
        if visit[n] == True:
            continue
        visit[n] = True
        dfs(i+1, mp[n])


def dfs2(i, node):
    global ans2
    ans2 = max(ans2, i)
    for n in node:
        if visit[n] == True:
            continue
        visit[n] = True
        dfs(i+1, mp[n])




dfs(0, mp[1])
dfs2(0, mp[N1+1])
print(ans1)
print(ans2)
print(ans1+ans2 - 2)
# ans globalにする必要ある？？ visitは？
# BFS??? じゃないとダメ？

