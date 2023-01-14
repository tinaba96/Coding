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

al = set()
cnt = 0

def dfs(p, e):
    global cnt
    if p not in al:
        al.add(p)
    cnt += 1
    if len(al) > 10**6:
        print(10**6)
        exit()
    for n in mp[e]:
        if str(n) in p:
            continue
        dfs(p+str(n), n)
    return

dfs('1', 1)
print(cnt)

# WA: 全探索ができていない？
# TLE: len(al)やstr(n) in p に時間を要している？　それともpythonの再帰だから？
# len(al) can costs almost 10**6 specially at the end.
# str(n) in p costs O(len(p)) which is O(N) at maximum
