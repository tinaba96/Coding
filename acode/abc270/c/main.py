N, X, Y = list(map(int, input().split()))

mp = [[] for i in range(N+1)]

for i in range(N-1):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)


seen = set()

seen.add(str(X))
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
        if len(ans) > 0:
            p = ans.pop()

count(ans)



