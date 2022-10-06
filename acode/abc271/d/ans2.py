N,S = map(int,input().split())
ab = [ list(map(int,input().split())) for _ in range(N)]

dp = [[ '' ]*100001 for _ in range(N+1) ]

dp[0][0] = 'S'
#print(dp)
for i in range(N):
    for j in range(1,100001):
        a,b = ab[i]
        #print(i,j,a)
        if j>=a and len(dp[i][j-a]) != 0:
            dp[i+1][j] = dp[i][j-a]+'H'
        if j>=b and len(dp[i][j-b]) != 0:
            dp[i+1][j] = dp[i][j-b]+'T'

#print(dp)
if len(dp[N][S])==0:
    print('No')
else:
    print('Yes')
    print(dp[N][S][1:])
