import sys
input = sys.stdin.readline

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
MOD = 998244353

dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
  for pre in range(2):
    for nxt in range(2):
      if AB[i - 1][pre] != AB[i][nxt]:
        dp[i][nxt] += dp[i - 1][pre]
  dp[i][0] %= MOD
  dp[i][1] %= MOD
        
print((dp[N - 1][0] + dp[N - 1][1]) % MOD)


