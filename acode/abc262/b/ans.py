N,M=map(int,input().split())
dp=[[0]*N for _ in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    dp[u][v]=1
    dp[v][u]=1

cnt=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            # (1,4) (4,5) (1,5) 
            if dp[i][j] and dp[j][k] and dp[i][k]:
                cnt+=1
print(cnt)

                






