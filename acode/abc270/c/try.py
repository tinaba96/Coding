import sys
sys.setrecursionlimit(500005) # this makes RE -> TLE

N, X, Y = list(map(int, input().split()))
mp = [[] for i in range(N+1)]
for i in range(N-1):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)
ans = [X]
def count(ans):
    for k in range(len(mp[ans[-1]])):
        if mp[ans[-1]][k] in ans:
            continue
        if mp[ans[-1]][k] == Y:
            ans.append(Y)
            print(*ans)
            exit()
        ans.append(mp[ans[-1]][k])
        count(ans)
        p = ans.pop()
count(ans)



