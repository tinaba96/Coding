N, M = list(map(int, input().split()))

mp = [[] for i in range(N+1)]


for i in range(M):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)

ans = 0
#print(mp)
for p in range(N):
    for m in range(len(mp[p])):
        if p < mp[p][m]:
            for h in range(len(mp[mp[p][m]])):
                if mp[p][m] < mp[mp[p][m]][h]:
                    if p in mp[mp[mp[p][m]][h]]:
                        ans += 1

print(ans)



