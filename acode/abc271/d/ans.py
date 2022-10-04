N, S = map(int, input().split())

dp = [[False] * (S + 1) for _ in range(N + 1)]
A = [0] * N
B = [0] * N
dp[0][0] = True

for i in range(N):
    a, b = map(int, input().split())
    for v in range(S+1):
        if dp[i][v]:
            if (v+a) <= S:
                dp[i+1][v+a] = True
            if (v+b) <= S:
                dp[i+1][v+b] = True
    A[i] = a
    B[i] = b

if not dp[N][S]:
    print("No")
    exit()
print("Yes")

now = S

ans = []

for i in range(N, 0, -1):
    a, b = A[i-1], B[i-1]
    if dp[i-1][now-a]:
        ans.append("H")
        now -= a
    else:
        ans.append("T")
        now -= b

#print(now)
print(''.join(ans[::-1]))
