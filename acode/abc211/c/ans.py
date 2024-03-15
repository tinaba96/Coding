S = input()
T = 'chokudai'

N = len(S)
M = len(T)

MOD = 10**9 + 7
DP = []
for _ in range(N+1):
    DP.append([0] * (M+1))

for i in range(N+1):
    DP[i][0] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if S[i-1] == T[j-1]:
            DP[i][j] = (DP[i-1][j] + DP[i-1][j-1])%MOD
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][M]%MOD)




