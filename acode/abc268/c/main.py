N = int(input())
p = list(map(int, input().split()))

mp = {}
ans = 0

for i in range(N):
    mp[p[i]] = i
    if abs(i-p[i]) <= 1:
        ans += 1

for t in range(N):
    a = 0
    for k in range(N):
        if abs(mp[p[k]]+t-p[k]) <= 1 or (p[k] == 0 and mp[p[k]]+t == N-1) or ((mp[p[k]]+t)%N == 0 and p[k] == N-1):
            a += 1
    ans = max(ans, a)

#print(mp)
print(ans)

