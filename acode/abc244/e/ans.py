n,m,k,s,t,x = map(int,input().split())
s,t,x = s-1,t-1,x-1

graph = [[] for i in range(n+1)]
mod = 998244353
for i in range(m):
  a,b = map(int,input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

dp = [[[0 for i in range(2)] for i in range(n)] for i in range(k+1)]
dp[0][s][1] = 1
for i in range(1,k+1):
  for j in range(n):
    for nxt in graph[j]:
      if j != x:
        dp[i][j][0] += dp[i-1][nxt][0]
        dp[i][j][1] += dp[i-1][nxt][1]
      else:
        dp[i][j][0] += dp[i-1][nxt][1]
        dp[i][j][1] += dp[i-1][nxt][0]
      dp[i][j][0] %= mod
      dp[i][j][1] %= mod
print(dp[-1][t][1])


