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

from copy import deepcopy


N, M = list(map(int, input().split()))

#mp = [[] for k in range(N+1)]

mp = [[] for j in range(N+1)]

start = 1
Q = []
for i in range(M):
    X, Y = list(map(int, input().split()))
    Q.append((X, Y))

Q = list(set(Q))

for X, Y in Q:

    if start == Y:
        start = X

    mp[X].append(Y)
    #mp[Y].append(X)

#for g in range(len(mp)): # takes time
    #mp[g] = list(set(mp[g]))

ans = [0 for _ in range(N)]
path = []

flg = False
answer = []

def dfs(check, path, cur):
    global flg
    global answer
    if len(path) == N:
        if flg:
            print('No')
            exit()
        flg = True
        answer = deepcopy(path)
        #print('path', path)
        '''
        print('Yes')
        #print(*path)
        for p in range(len(path)):
            ans[path[p]-1] = p+1
        print(*ans)
        exit()
        '''

    for e in mp[cur]:
        if e not in check:
            path.append(e)
            check.add(e)
            dfs(check, path, e)
            path.pop()
            check.remove(e)

check = set()
dfs(check, [start], start)

if flg == True:
    print('Yes')
    #print(*path)
    for p in range(len(answer)):
        ans[answer[p]-1] = p+1
    print(*ans)
    exit()

print('No')



