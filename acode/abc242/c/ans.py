import sys

N = int(input())
MOD =  998244353
# dp[i][j] i桁目の数字がj 

dp = [[0]* 10 for _ in range(N+1)]

for i in range(1,10):
    dp[0][i] = 1

for i in range(N-1):
    for j in range(1,10):
        
        if j == 1: 
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1]%=MOD
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %=MOD
        elif j == 9:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1]%=MOD
            dp[i+1][j] += dp[i][j]
            dp[i+1][j]%=MOD
        else:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1]%=MOD
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1]%=MOD
            dp[i+1][j] += dp[i][j]
            dp[i+1][j]%=MOD
            

print(sum(dp[N-1])%MOD)
            
        
'''
# reusing the fp array
n=int(input())
mod=998244353
a=[0]+[1]*9+[0]
for _ in range(n-1):
    a=[0]+[(a[i-1]+a[i]+a[i+1])%mod for i in range(1,10)]+[0]
print(sum(a)%mod)
'''




