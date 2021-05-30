N, K = list(map(int, input().split()))
ans = 0
for n in range(N):
    for k in range(K):
        ans += (n+1)*100 + (k+1)


print(ans)


