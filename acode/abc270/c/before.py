import sys
sys.setrecursionlimit(500005)

N, X, Y = list(map(int, input().split()))

mp = [[] for i in range(N+1)]

for i in range(N-1):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)


seen = set()

seen.add(str(X))
ans = [X]

def count(ans, seen):
    for k in range(len(mp[ans[-1]])):
        if str(mp[ans[-1]][k]) in seen:
            continue
        if mp[ans[-1]][k] == Y:
            ans.append(Y)
            print(*ans)
            exit()
        ans.append(mp[ans[-1]][k])
        seen.add(str(mp[ans[-2]][k]))
        count(ans, seen)
        p = ans.pop()
        seen.remove(str(p))
        #seen.remove(str(mp[ans[-1]][k]))

count(ans, seen)


