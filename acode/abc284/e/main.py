import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))


mp = [[] for n in range(N+1)]

for i in range(M):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)

pas = [False for f in range(N)]

al = set()

path = ''

def dfs(p, e):
    #print(p, e)
    if p in al:
        return # is this really correct? -> it will return even if the search is in the middile?
    al.add(p)
    if len(al) > 10**6:
        print(10**6)
        exit()
    for n in mp[e]:
        if str(n) in p:
            continue
        dfs(p+str(n), n)
    return

dfs('1', 1)
#print(al)
print(len(al))

# WA: 全探索ができていない？
# TLE: len(al)やstr(n) in p に時間を要している？　それともpythonの再帰だから？
