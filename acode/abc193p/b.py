N = int(input())
ans = 10**9
for n in range(N):
    A, P, X = list(map(int, input().split()))
    left = X - A
    if left > 0:
        ans = min(ans, P)
    

if ans == 10**9:
    print(-1)
else:
    print(ans)


